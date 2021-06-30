#!/usr/bin/python3
"""HBNB"""

import cmd


class HBNBCommand(cmd.Cmd):

    """Simple command processor example."""

    prompt = '(hbnb)'

    def do_EOF(self, line):
        """EOF"""
        return True

    def do_quit(self, args):
        """ Close cmd """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
