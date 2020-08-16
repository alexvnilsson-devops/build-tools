from argparse import ArgumentParser
from .commandsubparser import CommandSubparser


class CommandParser:
    def __init__(self, parser: ArgumentParser):
        print("CommandParser")
        self.parser: ArgumentParser = parser

    def add_subparser(self, instance: CommandSubparser, **kwargs):
        print(f"{self.__class__.__name__} add_subparser")
        i: CommandSubparser = instance()
        i.register_subparser(self.parser.add_subparsers(**kwargs))
