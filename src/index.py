from asyncio import run

import app


def main():
    # execute a Coroutine object
    run(app.process_queue_by_priority())


if __name__ == '__main__':
    main()
