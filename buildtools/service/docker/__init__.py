import subprocess
from sys import exit
from ..shell import popen, PResult, print_ok
from ..shell.formatting import bcolors, text, glyphs


def add_image_tag(image: str, tag: str, registry: str = None) -> bool:
    p_args = ["tag", image]

    if registry is not None:
        p_args.extend([f"{registry}/{image}:{tag}"])
    else:
        p_args.extend([f"{image}:{tag}"])

    p = popen("docker", p_args)

    if not isinstance(p, PResult):
        raise Exception("Something went wrong.")

    if p.exit_code == 0:
        if registry is not None:
            print(
                f"{bcolors.GREEN}{glyphs.OK}{bcolors.ENDC} {text.BOLD}Tagged{text.RESET} {registry}/{image}:{tag}")
        else:
            print(
                f"{bcolors.GREEN}{glyphs.OK}{bcolors.ENDC} {text.BOLD}Tagged{text.RESET} {image}:{tag}")
    else:
        print(f"{bcolors.RED}{p.stderr}{bcolors.ENDC}")


def publish_image(image: str, registry: str):
    p_args = ["push"]

    if registry is not None:
        p_args.extend([f"{registry}/{image}"])
    else:
        p_args.extend([f"{image}"])

    p = popen("docker", p_args)

    if not isinstance(p, PResult):
        raise Exception("Something went wrong.")

    if p.exit_code == 0:
        if registry is not None:
            print(
                f"{bcolors.GREEN}{glyphs.OK}{bcolors.ENDC} {text.BOLD}Published{text.RESET} {image} to {registry}")
        else:
            print(
                f"{bcolors.GREEN}{glyphs.OK}{bcolors.ENDC} {text.BOLD}Published{text.RESET} {image}")
    else:
        print(f"{bcolors.RED}{p.stderr}{bcolors.ENDC}")
