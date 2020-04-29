"""Command line interface with nice terminal output."""
import argparse

from bremer_abfallkalender.parser import get_from_website, print_nice


def get_arguments():  # pragma: no cover
    """Get arguments from command line."""
    parser = argparse.ArgumentParser(
        description='Print the Abfallkalender for Bremen.')
    parser.add_argument(
        '-s', '--street', type=str,
        help='Street name of the address. E.g. Bahnhofstraße.')
    parser.add_argument(
        '-n', '--number', type=int,
        help='Street number of your address. E.g. 1')

    return parser.parse_args()


def main():  # pragma: no cover
    """Print current calendar based on website data."""
    args = vars(get_arguments())
    data = get_from_website(args['street'], args['number'])
    print(print_nice(data))


if __name__ == '__main__':  # pragma: no cover
    main()
