from asyncio import sleep
import json

from utils.index import debug_log


async def fetch_queue_data(filter=[]):
    """
    Request for queue data
    Args:
        filter: (list) of int. Filter by priority
    Returns:
        (list) of dict { priority: int, command: str }
    """
    with open('src/services/data.json', 'r') as f:
        data = json.load(f)
        if len(filter) > 0:
            data = [d for d in data if d["priority"] in filter]
    # Mock an async process
    await sleep(0.3)
    debug_log(f'Found {len(data)} tasks in queue')
    return data
