#!/usr/bin/env python
# -*- coding: utf-8 -*-
"SSH Helper functions for the RSD Resource module"

from __future__ import absolute_import, division, print_function, unicode_literals

from builtins import str  # pylint:disable=redefined-builtin

import re
import subprocess


REMOTECTL_PATH = "/usr/libexec/remotectl"
SSH_DEFAULT_ARGS = [
    "-o",
    "ProxyUseFdpass=yes",
    "-o",
    "UserKnownHostsFile=/dev/null",
    "-o",
    "StrictHostKeyChecking=no",
    "-o",
    "BatchMode=yes",
    "-o",
    "ConnectTimeout=60",
    # These args are to exit the ssh connection if the other end
    # hangs up or disconnects
    "-o",
    "ServerAliveInterval=30",
    "-o",
    "ServerAliveCountMax=4",
]
ZERO_UUID = "00000000-0000-0000-0000-000000000000"


def _get_ssh_options_for_service(ssh_ncm_service):
    """Return a list of ssh arguments for the given service."""
    if not ssh_ncm_service:
        # Fallback to the default for now and fail later
        ssh_ncm_service = "com.apple.internal.ssh"

    proxy_command = [
        "-o",
        "ProxyCommand={remotectl_path} netcat -F %h {ssh}".format(remotectl_path=REMOTECTL_PATH, ssh=ssh_ncm_service),
    ]
    return SSH_DEFAULT_ARGS + proxy_command


def _find_ssh_ncm_service_from_uuid(uuid):
    """Use remotectl with the resource's uuid to determine if we should use
    ssh or com.apple.internal.ssh."""
    try:
        command = [REMOTECTL_PATH, "show", uuid]
        output = subprocess.check_output(command, universal_newlines=True).strip()
    except subprocess.CalledProcessError:
        # That call may fail when querying a cached remote_device_uuid
        # and the device is unavailable (down / rebooted / unplugged)
        return None

    ssh_services = ["ssh", "com.apple.internal.ssh"]
    for service in ssh_services:
        if re.search("\t\t{service}".format(service=service), output):
            return service

    return None


def _remote_device_uuid_matches_ecid(remote_device_uuid, ecid):
    if remote_device_uuid == ZERO_UUID:
        return False

    command = [
        REMOTECTL_PATH,
        "get-property",
        remote_device_uuid,
        "UniqueChipID",
    ]

    try:
        device_ecid = subprocess.check_output(command, universal_newlines=True).strip()
    except subprocess.CalledProcessError:
        return False
    return device_ecid == str(ecid)


def _remote_device_uuid_from_ecid(ecid):
    command = [REMOTECTL_PATH, "list"]
    try:
        remotectl_list_output = subprocess.check_output(command, universal_newlines=True)
    except subprocess.CalledProcessError:
        return None
    try:
        remote_device_uuids = [t.split()[0] for t in remotectl_list_output.strip().split("\n")]
    except IndexError:
        return None

    for remote_device_uuid in remote_device_uuids:
        if _remote_device_uuid_matches_ecid(remote_device_uuid, ecid):
            return remote_device_uuid
    return None


print(_find_ssh_ncm_service_from_uuid("B8BB0D8A-07DE-483C-9563-C479DDC1C9A6"))

print(_get_ssh_options_for_service(None))
