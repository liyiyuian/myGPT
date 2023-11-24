import argparse


# Create the parser
def parse_args():
    parser = argparse.ArgumentParser(description="Welcome to myGPT!")

    parser.add_argument(
            '-m', '--mode',  # The flag of the argument
            action='store',  # Action to store the argument's value
            nargs=1,  # Number of arguments to consume
            default='Others',  # Default value if the argument is absent
            type=str,  # Type to which argument is converted
            choices=['chat', 'assistant', 'image'],  # Allowable values
            required=False,  # Whether it's a required argument
            help='Which mode to run?',  # Help message
            metavar='MODE',  # Display name for the argument in usage
            dest='mode'  # The attribute name to store the value
            )
    parser.add_argument(
            '--delete_all',
            action='store_true',
            required=False,
            help='Delete all running assistants',
            dest="delete_all",
            )
    args = parser.parse_args()
    return args
