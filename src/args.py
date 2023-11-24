import argparse


def parse_args():
    # Create the parser
    parser = argparse.ArgumentParser(description="Welcome to myGPT!")

    parser.add_argument(
            '-m', '--mode',  # The flag of the argument
            action='store',  # Action to store the argument's value
            nargs=1,  # Number of arguments to consume
            default='default.txt',  # Default value if the argument is absent
            type=str,  # Type to which argument is converted
            choices=['chat', 'assistant', 'image'],  # Allowable values
            required=True,  # Whether it's a required argument
            help='Which mode to run?',  # Help message
            metavar='MODE',  # Display name for the argument in usage
            dest='mode'  # The attribute name to store the value
            )

    args = parser.parse_args()
    return args
