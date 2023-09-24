import argparse
import sys


def get_check_int_greater_than(val_min):
    """
    Higher order function that returns a valid argparse type Callable that checks
    if a provided string is an integer >= val_min
    """

    def check_int_greater(val_str):
        try:
            val_int = int(val_str)
            if val_int < val_min:
                raise argparse.ArgumentTypeError(
                    f"{val_int} is not >= {val_min}")
            return val_int
        except ValueError:
            raise argparse.ArgumentTypeError(f"{val_str} is not an int")
    return check_int_greater


def get_one_argument(argument, argument_help, description):
    """
    Sets up ArgumentParser to parse a single command line argument

    Parameters:
        argument: str
            The name of the argument 

        argument_help: str
            The help text for said argument

        description: str
            The help text for the program

    Returns:
        The parsed argument
    """

    parser = argparse.ArgumentParser(
        description=description, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        argument, type=str, help=argument_help)
    return next(iter(vars(parser.parse_args()).values()))


def check_no_arguments(description):
    """Handles scripts that take no arguments, but still will display a help message"""

    if len(sys.argv) == 2 and sys.argv[1] in {"-h", "--help"}:
        print(f"{sys.argv[0]}: {description}")
        sys.exit(0)
    elif len(sys.argv) != 1:
        print(f"{sys.argv[0]} takes no arguments")
        sys.exit(1)
