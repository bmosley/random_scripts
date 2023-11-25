#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess

def send_to_clipboard(unicode_char):
    """
    Copy a non-ASCII character to pasteboard on macOS.
    Useful for inserting emoji and/or alternate language characters.

    :param unicode_char: any ASCII/non-ASCII string or character
    :return:
    """

    process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(unicode_char.encode('utf-8'))

    # Check that unicode_char is in pasteboard
    unicode_char_return = subprocess.check_output('pbpaste', env={'LANG': 'en_US.UTF-8'}).decode('utf-8')
    assert unicode_char_return == unicode_char, 'character was not copied properly to pasteboard'

send_to_clipboard(u'🤬')