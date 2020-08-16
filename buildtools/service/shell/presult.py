from string import Template


class PResult(object):
    def __init__(
            self,
            exit_code: int,
            stdout: str,
            stderr: str):
        self.exit_code = exit_code
        self.stdout = stdout
        self.stderr = stderr

    def __repr__(self):
        presult_repr = Template(
            '$module(exit_code=$exit_code, stdout=$stdout, stderr=$stderr)')
        return presult_repr.safe_substitute(
            module=self.__class__.__name__,
            exit_code=self.exit_code,
            stdout=self.stdout,
            stderr=self.stderr
        )
