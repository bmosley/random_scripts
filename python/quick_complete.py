import os
import re
import readline

RE_SPACE = re.compile('.*\s+$', re.M)


class QuickAutoComplete(object):

    def __init__(self, quick_verbs, ui_elements):
        self.quick_verbs = quick_verbs
        self.ui_elements = ui_elements

    def _listdir(self, root):
        res = []
        for name in os.listdir(root):
            path = os.path.join(root, name)
            if os.path.isdir(path):
                name += os.sep
            res.append(name)
        return res

    def _complete_path(self, path=None):

        if not path:
            return self._listdir('.')
        dir_name, rest = os.path.split(path)
        tmp = dir_name if dir_name else '.'
        res = [os.path.join(dir_name, p) for p in self._listdir(tmp) if p.startswith(rest)]

        # more than one match, or single match which does not exist (typo)
        if len(res) > 1 or not os.path.exists(path):
            return res

        # resolved to a single directory, so return list of files below it
        if os.path.isdir(path):
            return [os.path.join(path, p) for p in self._listdir(path)]
        
        # exact file match terminates this completion
        return [path + ' ']

    def complete_extra(self, args):

        if not args:
            return self._complete_path('.')

        # treat the last arg as a path and complete it
        return self._complete_path(args[-1])

    def complete(self, text, state):
        buffer = readline.get_line_buffer()
        line = readline.get_line_buffer().split()

        # show all commands
        if not line:
            return [cmd + ' ' for cmd in self.quick_verbs][state]

        # account for last argument ending in a space
        if RE_SPACE.match(buffer):
            line.append('')

        # resolve command to the implementation function
        cmd = line[0].strip()

        if cmd in self.quick_verbs:
            impl = getattr(self, 'complete_{}'.format(cmd))
            args = line[1:]
            if args:
                return (impl(args) + [None])[state]

            return [cmd + ' '][state]

        results = [i + ' ' for i in self.quick_verbs if i.startswith(cmd)] + [None]
        return results[state]
