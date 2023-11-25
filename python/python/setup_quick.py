#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import stat

"""
Convenience script for creating a symbolic link to quick.py
<rdar://problem/45593989> Hardcoded paths in setup.sh creates problems when using pipenv

Usage: sudo python setup_quick.py

"""

QUICK_PY = "quick.py"

try:
    from quickscript.util.quickUtils import get_quick_directory


    quick_dir = get_quick_directory()
    quick_py_path = os.path.join(quick_dir, QUICK_PY)

    if not os.path.exists(quick_py_path):
        print("Unable to find {} in {} \nThis script must be run in the same location as Quick.\n".format(QUICK_PY, quick_dir))
        sys.exit(1)

    src_path = quick_py_path
    dst_path = "/usr/local/bin/quick"

    # Make the file executable
    os.chmod(src_path, stat.S_IEXEC)
    # Create the symlink
    os.symlink(src_path, dst_path)

    print("Done - you can now run 'quick' from any directory to run Quick")

except OSError as os_error:
    print("{}\n\n*** You must run this script with sudo to create symlinks to /usr/local/bin/ ***\n".format(os_error))

except ImportError as import_error:
    print("{}\n\nQuickscript was not 'pip' installed. Symbolic links will not work.\n"
          "To install Quick, please visit https://quick.apple.com/ for instructions.\n".format(import_error))