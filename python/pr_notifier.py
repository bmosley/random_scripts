#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import json
import argparse
import requests

"""
This script is used in combination with Jenkins for CI

USAGE: python3 pr_notifier.py -j <json>
or have Jenkins store json as environment variable.

2020.01.29
"""

# User variables
PROJECT = ""
REPO = ""
TOKEN = ""

# Enviroment variables keys (passed down by Jenkins or json.loads)
pull_request = "pull_request"
pull_request_id = f"{pull_request}_PR_ID"
pull_request_email = f"{pull_request}_AUTHOR_EMAIL"  # might need ACTION_AUTHOR_EMAIL
pull_request_sha = f"{pull_request}_TO_REF_ref_sha"
pull_request_ref_id = f"{pull_request}_FROM_REF_ref_id"

# [Stashweb base URL]
base_url = "https://stashweb.sd.apple.com"
url = f"{base_url}/rest/api/1.0/projects/{PROJECT}/repos/{REPO}/pull-requests"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TOKEN}"
}

msg = {
    "text": "requests module"
}


def post_url(pl):
    return f"{url}/{pl[pull_request_id]}"


def POST_to_stash(payload):
    response = requests.post(f"{post_url(payload)}/comments", json=msg, headers=headers)
    if not response.ok:
        print(f"ERROR: Requests post to {base_url} failed. Status: {response.status_code}")


def GET_changed_files(payload):
    response = requests.get(f"{post_url(payload)}/changes", headers=headers)
    if not response:
        return
    
    # returns a list of content changes with hash
    content_ids = response.get("values", None)
    content_ids = content_ids.json()

    if not content_ids:
        return

    file_changes = [x["path"]["toString"] for x in content_ids if x["path"]["toString"]]
    return file_changes


def main():
    payload = args.j

    # If a json string isn't passed in, grab it from env vars
    if not payload:
        payload = os.environ

    # Debug
    for k, v in payload.items():
        print(f"key: {k} --> val: {v}")

    POST_to_stash(payload)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-j", help="JSON payload", type=json.loads)
    args = parser.parse_args()
    main()

