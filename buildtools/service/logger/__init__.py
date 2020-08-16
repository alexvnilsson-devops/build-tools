log_filename = 'az-error.log'


def dump_stderr(stderr: bytes):
    stderr_str = stderr.decode('UTF-8')

    with open(f"{log_filename}", "a+") as fo:
        fo.write(stderr_str)
