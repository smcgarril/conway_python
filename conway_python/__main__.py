import sys

from conway_python import patterns, views
from conway_python.cli import get_command_line_args

# Main method recieves args and renders program view
def main():
    args = get_command_line_args()
    View = getattr(views, args.view)
    if args.all:
        for pattern in patterns.get_all_patterns():
            _show_pattern(View, pattern, args)
    else:
        _show_pattern(
            View,
            patterns.get_pattern(name=args.pattern),
            args
        )

# Helper function to render View
def _show_pattern(View, pattern, args):
    try:
        View(pattern=pattern, gen=args.gen, frame_rate=args.fps).show()
    except Exception as error:
        print(error, file=sys.stderr)

if __name__ == "__main__":
    while True:
        main()