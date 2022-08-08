import argparse


ARGS = None

def set_args(parser: argparse.ArgumentParser):
    global ARGS
    ARGS = parser.parse_args()


def get_args(key) -> str | argparse.Namespace:
    global ARGS
    if (key):
        return ARGS.__getattribute__(key)
    return ARGS


def debug_log(msg):
    if (not ARGS.silent):
        print(msg)