import os

test_content_dir = os.path.expanduser('~/Desktop/test')

def _list_dir_files():
    return [os.path.join(test_content_dir, f) for f in os.listdir(test_content_dir) if not f.startswith('.')]

# Remove any spaces. Thank you Python 2.7
for fn in _list_dir_files():
    fn_basename = os.path.basename(fn)
    if ' ' in fn_basename:
        new_basename = fn_basename.replace(' ', '_')
        new_filename = os.path.join(test_content_dir, new_basename)
        print('Renaming file with space from {} to {}'.format(fn, new_filename))
        os.rename(fn, new_filename)

print(_list_dir_files())