from subprocess import Popen, PIPE
from ..logger import dump_stderr, log_filename

from .presult import PResult
from .formatting import bcolors, text


def decode(std: bytes):
    return std.decode("UTF-8")


def popen(cmd: str, args: list, raise_exception: bool = False) -> PResult:
    p_cmd = [cmd]

    p_cmd.extend(args)

    p = Popen(p_cmd, stdout=PIPE, stderr=PIPE)

    p_stdout, p_stderr = p.communicate()
    p_ecode = p.returncode

    if p_ecode != 0:
        if raise_exception:
            dump_stderr(p_stderr)
            raise Exception(
                f"Command exited with code {p_ecode}. See {log_filename} for details.")

    return PResult(p_ecode, decode(p_stdout).strip(), decode(p_stderr).strip())


def print_ok(msg: str):
    print(f"{bcolors.OKGREEN}Done.{bcolors.ENDC}")

    #
