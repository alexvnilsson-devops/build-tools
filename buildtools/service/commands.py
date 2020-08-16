from argparse import ArgumentParser, _SubParsersAction
from string import Template


class SubCommandGroup:
    def register(self, parser: ArgumentParser, title: str):
        self.parser = parser
        self.subparsers.add_parser(title)


class CommandGroup:
    def register(self, parser: ArgumentParser):
        self.__log_method_event("register", parser)

        self.parser: ArgumentParser = parser
        self.subparsers = None

        self.parsers = {}

    def add_subparser(self, title: str, class_object: object):
        self.parsers[title] = class_object(title)

    def register_subparsers(self, help: str = "sub-commands help"):
        self.__log_method_event("register_subparsers", help)

        if self.parser is None:
            raise Exception("No parser.")

        if hasattr(self, "subparsers") and self.subparsers is not None:
            raise Exception("Subparsers already enabled.")

        self.subparsers = self.parser.add_subparsers(help=help)

    def register_subcommand_listener(self):
        self.parser.add_argument("command", help="command")

    def get_subparser(self) -> _SubParsersAction:
        if self.subparsers is None:
            raise Exception("Subparsers not enabled.")

        return self.subparsers

    # Private methods

    def __log_method_event(self, method_name: str, log_str: str = ""):
        print(Template("$class_name.$method_name $log_str").safe_substitute(
            class_name=self.__class__.__name__,
            method_name=method_name,
            log_str=log_str))
