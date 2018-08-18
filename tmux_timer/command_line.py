import argparse
import functools
import os
import tempfile
import time


tempfile.tempdir = os.environ.get('XDG_RUNTIME_DIR')


def with_data_path(f):
    @functools.wraps(f)
    def inner(args):
        path = os.path.join(tempfile.gettempdir(), 'tmux_timer-{}'.format(os.getuid()))
        if args.id:
            path += '-{}'.format(args.id)
        return f(path, args)
    return inner


@with_data_path
def start(path, args):
    with open(path, 'w') as f:
        f.write(str(int(time.time())))


@with_data_path
def stop(path, args):
    try:
        os.remove(path)
    except OSError:
        pass


@with_data_path
def toggle(path, args):
    if os.path.exists(path):
        stop(args)
    else:
        start(args)


@with_data_path
def show(path, args):
    try:
        with open(path) as f:
            start = int(f.read())
    except IOError:
        return
    dt = time.time() - start
    print(round(dt, 0))


def main():
    parser = argparse.ArgumentParser(description='''
        Command-line timer for tmux.
        ''')
    parser.add_argument('--id', help='''
        Optional id to distinguish different timers.
        ''')
    subparsers = parser.add_subparsers()
    toggle_cmd = subparsers.add_parser('toggle')
    toggle_cmd.set_defaults(func=toggle)

    start_cmd = subparsers.add_parser('start')
    start_cmd.set_defaults(func=start)

    stop_cmd = subparsers.add_parser('stop')
    stop_cmd.set_defaults(func=stop)

    show_cmd = subparsers.add_parser('show')
    show_cmd.set_defaults(func=show)

    args = parser.parse_args()
    args.func(args)