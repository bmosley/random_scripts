import string

def _make_path_safe_file_name(file_name, is_screenshot=True):
    """
    Take a non-safe string and convert to something that can be used for file name

    * truncate strings over 240 characters
    * append file type to string if it's not already specified

    :param file_name: str
    :return:
    """
    new_file_name = "screen_shot"

    try:
        file_safe_chars = string.letters + string.digits + "_-." + " "
        new_file_name = filter(lambda x: x in file_safe_chars, file_name)
        new_file_name = new_file_name.replace(" ", "_")

        # Truncate filename if longer than 240 characters
        if len(new_file_name) > 240:
            new_file_name = new_file_name[:200]

        if is_screenshot:
            file_type = ".png"

            if not new_file_name.endswith(file_type):
                new_file_name += file_type

    except AttributeError as atr_e:
        print("A problem occurred while attempting to rename file. {}".format(atr_e))

    finally:
        return new_file_name

x = 'Verify Subscribe syncs on iOS Device\nuuioiuoiuioiouuoiiououioiu&&&&((*(*(*)(*uiooiuoiuopiuougoibgtkjuyfnjufbjhytfhjvytdfhtyrdvhtyrdvhtrsdvhtrsdrtybsdhtrdshbtrdhbtrdbthyrd'
print(_make_path_safe_file_name(x))

