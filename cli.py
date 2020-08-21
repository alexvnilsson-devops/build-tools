import click
import os
import importlib
import pkgutil

from core import modules


def get_module_group_name(module: pkgutil.ModuleInfo, instance: pkgutil.ModuleType) -> str:
    if not hasattr(instance, "cli"):
        raise Exception(f"Need attribute 'cli' in {module.name}.")

    if not hasattr(instance.cli, "name"):
        raise Exception(f"Need attribute 'name' in {module.name}.cli.")

    return instance.cli.name


def get_pkg_commands(pkg):
    pkg_instance = importlib.import_module(pkg)
    pkg_path = os.path.dirname(pkg_instance.__file__)

    pkg_commands = {}

    for module in pkgutil.iter_modules([pkg_path]):
        module_name = module.name
        module_instance = importlib.import_module(f"{pkg}.{module_name}")

        if not module.ispkg:
            module_command_name = get_module_group_name(
                module, module_instance)
            cli_name = module_instance.cli.name
            pkg_commands[module_instance.cli.name] = module_instance.cli
        else:
            module_command_name = get_module_group_name(
                module, module_instance)
            pkg_commands[module_command_name.replace("_", "-")] = click.Group(
                context_settings={'help_option_names': ['-h', '--help']},
                help=module_instance.__doc__,
                commands=get_pkg_commands(f"{pkg}.{module.name}")
            )

    return pkg_commands


@click.group(context_settings={'help_option_names': ['-h', '--help']}, help="Your CLI",
             commands=get_pkg_commands('modules'))
# INIT_SCRIPT_NAME = "__init__.py"
# def make_module(path: str, relative_to=None):
#     if os.path.exists(path) == False:
#         raise IOError(f"{path} doesn't exist.")
#     if os.path.isdir(path) == False:
#         raise NotADirectoryError(f"{path} is not a directory.")
#     init_script = os.path.join(path, INIT_SCRIPT_NAME)
#     if os.path.exists(init_script) == False:
#         raise IOError(f"{init_script} doesn't exist.")
#     if relative_to is None:
#         return init_script
#     else:
#         print(
#             f"path: {path}, relative_to: {relative_to}: result: {os.path.relpath(path, relative_to)}")
#         return os.path.relpath(path, relative_to)
# class MyCLI(click.MultiCommand):
#     def list_commands(self, ctx):
#         rv = []
#         for item in os.listdir(plugin_folder):
#             try:
#                 print(item)
#                 module_path = os.path.join(plugin_folder, item)
#                 item_module = make_module(module_path, plugin_folder)
#                 rv.append(item_module)
#             except Exception as e:
#                 print(e)
#         rv.sort()
#         print(rv)
#         return rv
#     def get_command(self, ctx, name):
#         ns = {}
#         fn = os.path.join(plugin_folder, name, '__init__.py')
#         with open(fn) as f:
#             code = compile(f.read(), fn, 'exec')
#             eval(code, ns, ns)
#         return ns['cli']
# cli = MyCLI(help='This tool\'s subcommands are loaded from a '
#             'plugin folder dynamically.')
def cli():
    pass


if __name__ == '__main__':
    cli()
