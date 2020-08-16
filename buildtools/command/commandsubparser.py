from argparse import _SubParsersAction


class CommandSubparser:
    subparser = None
    subparser_metadata: dict = None

    def __init__(self):
        print(f"{self.__class__.__name__} init")
        self.subparser = None

    def register_subparser(self, subparser: _SubParsersAction):
        self.subparser = subparser
        print(self.subparser)

        if hasattr(self, "install_parsers"):
            print(f"Calling {self.__class__.__name__}.install_parsers")
            self.install_parsers(self.subparser)
        else:
            print(f"install_parsers not in {self.__class__.__name__}.")
