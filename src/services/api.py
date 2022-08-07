from asyncio import sleep
import json

async def fetch_queue_list():
    """
    Request for queue data
    Returns:
        (list) of dict { priority: int, task: str }
    """
    print('Fetching data...')
    with open('src/services/data.json', 'r') as f:
        data = json.load(f)
    # Mock an async process
    await sleep(0.2)
    return data
