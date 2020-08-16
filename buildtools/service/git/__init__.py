import subprocess
from ..shell import popen, PResult


def is_repo(cwd: str) -> bool:
    p = popen("git", ["rev-parse", "--is-inside-work-tree"])

    if not isinstance(p, PResult):
        raise TypeError()

    return p.exit_code == 0
