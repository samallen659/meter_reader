import os


def exit_if_none(*args):
    """Checks whether values are None and exits if they are"""
    for a in args:
        if a is None:
            os._exit(1)
