from asyncio import run
import argparse

import app
from utils.index import set_args


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-P',
        '--priority',
        help='Execute tasks of specific priority (0 to 10).',
    )
    parser.add_argument(
        '-S',
        '--silent',
        action='store_true',
        help='Runs application in silent mode. Only shows error logs.',
    )
    set_args(parser)

    # execute a Coroutine object
    run(app.process_queue_by_priority())


if __name__ == '__main__':
    main()
