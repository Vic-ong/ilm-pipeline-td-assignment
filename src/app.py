from services.api import fetch_queue_list


async def process_queue_by_priority():
    queue_list = await fetch_queue_list()

    # sort by priority while keeping the order they are received
    queue_list.sort(key=lambda queue: queue["priority"])

    # process queue
    for queue in queue_list:
        print(f'Executing command "{queue["task"]}" of priority {queue["priority"]}')


"""
Expected result:
[
    {
        "priority": 1,
        "task": "test-a"
    },
    {
        "priority": 1,
        "task": "migrate-a"
    },
    {
        "priority": 1,
        "task": "deploy-a"
    },
    {
        "priority": 1,
        "task": "deploy-ab"
    },
    {
        "priority": 2,
        "task": "exec-b"
    },
    {
        "priority": 2,
        "task": "run-b"
    },
    {
        "priority": 4,
        "task": "test-c"
    },
    {
        "priority": 4,
        "task": "migrate-c"
    },
    {
        "priority": 5,
        "task": "exec-d"
    },
    {
        "priority": 5,
        "task": "deploy-d"
    }
]
"""
