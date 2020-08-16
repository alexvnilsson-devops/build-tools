from sys import argv
from argparse import ArgumentParser
from string import Template


def handle_args(instance: object, parser: ArgumentParser, argv_index: int = 2, args_command_name: str = "command"):
    instance.args = parser.parse_args(argv[argv_index:(argv_index+1)])

    print(c_name)

    if not hasattr(args, args_command_name):
        print(Template("Unrecognized command \"$command\"").safe_substitute(
            command=c_name))
        parser.print_help()
        exit(1)

    getattr(instance, args.command)()
