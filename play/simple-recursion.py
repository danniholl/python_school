import os
import sys


def print_simple_dir_tree(directory: str):
    """
    Indented print to console of all files and directories below directory
    :param directory: starting directory
    :return: no return value
    """

    def go(current_dir: str, level: int):
        """
        Recursive function that does the work for print_simple_dir_tree
        :param current_dir: current directory
        :param level: level to determine indentation amount
        :return: no return value
        """
        spaces = '    '
        for file in os.listdir(current_dir):
            print('{}{}'.format(level * spaces, file))
            full_path = os.path.join(current_dir, file)
            if os.path.isdir(full_path):
                go(full_path, level + 1)

    go(directory, 0)


if __name__ == u'__main__':
    # default value if no argument provided
    start_dir = '.'

    # argument provided?
    if len(sys.argv) > 1:
        start_dir = sys.argv[1]
        # abort if arg is not a valid directory
        if not os.path.isdir(start_dir):
            sys.exit('{} is not a valid directory.'.format(start_dir))

    # transform to absolute path if necessary
    if not os.path.isabs(start_dir):
        start_dir = os.path.abspath(start_dir)

    # finally ready to go
    print_simple_dir_tree(start_dir)
