import argparse

from conway_python import __version__, patterns, views

def get_command_line_args():
    parser = argparse.ArgumentParser(
        prog="conway_python",
        description="A Python implementation of Conway's Game of Life."
    )

    parser.add_argument(
        "--version", action="version", version=f"%(prog)s v{__version__}"
    )

    parser.add_argument(
        "-p",
        "--pattern",
        choices=[pat.name for pat in patterns.get_all_patterns()],
        default="Blinker",
        help="Choose a pattern for the Game of Life (default: %(default)s)"
    )

    parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="Show all available patterns in a sequence"
    )

    parser.add_argument(
        "-v",
        "--view",
        choices=views.__all__,
        default="CursesView",
        help="Display the life grid in a specific view (default: %(default)s)"
    )

    parser.add_argument(
        "-g",
        "--gen",
        metavar="NUM_GENERATIONS",
        type=int,
        default=10,
        help="Number of generations (default: %(default)s)"
    )

    parser.add_argument(
        "-f",
        "--fps",
        metavar="FRAMES_PER_SECOND",
        type=int,
        default=7,
        help="Frames per second (default: %(default)s)"
    )

    return parser.parse_args()