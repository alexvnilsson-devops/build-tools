import argparse
from argparse import ArgumentParser
import sys
import os
from sys import exit
from string import Template

from .arg_parser import handle_args
from ..lib import git
from ..lib.commands import CommandGroup, SubCommandGroup


class Git(CommandGroup):
    def __init__(self, parser: ArgumentParser):
        self.parser = argparse.ArgumentParser()
        self.register(self.parser)
        self.register_subparsers()
        self.add_subparser("repo", GitRepo)


class GitRepo(CommandGroup):
    def __init__(self, parser: ArgumentParser):
        self.parser = argparse.ArgumentParser()
        self.register(self.parser)
        self.register_subcommand_listener()

        handle_args(self, self.parser)

    def verify(self):
        print("verify")
