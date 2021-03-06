#!/usr/bin/env python
from urllib2 import unquote

delim = '\n'
delims = '\n' + chr(0)


def test(examples=None):
    if examples is None:
        examples = ['file:///media/sda1/ssd/home/hobs/Pictures/ofHobsonLinks/Isla%20Mujeres%20to%20Panama%20052.jpg']
    for example in examples:
        stdout.write(get_path(example) + delim)


def get_path(string):
    stripped = string.strip()
    if stripped.startswith('file://') and string[-1] in delims:
        return unquote(stripped)[7:] + string[-1]
    return string


if __name__ == "__main__":
    from sys import argv, stdout, stdin
    import os.path


    # TODO: check to see if it's a file and do like grep (read the file and process it as one argument per line)
    #       -0 and -1 option like xargs and grep to output "args" delimited by null or newline
    if len(argv) > 1:
        args = argv[1:]
        for arg in args:
            stdout.write(get_path(arg) + delim)
            if os.path.isfile(arg):
                raise RuntimeError('Not implemented.')
                exit(1)
    else:
        for line in stdin:
            stdout.write(get_path(line))
    exit(0)
