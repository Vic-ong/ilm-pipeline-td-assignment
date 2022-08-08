from utils.index import debug_log, get_args
from services.api import fetch_queue_data
from models.Queue import PriorityQueue


async def process_queue_by_priority():
    # Get priority filter if exist
    priority_filter_args = get_args('priority')
    priority_filter = []
    if (priority_filter_args):
        try:
            debug_log(f'Querying for priority {priority_filter_args}')
            if len(priority_filter_args) == 1:
                priority_filter.append(int(priority_filter_args))
            else:
                filtered = priority_filter_args.split(',')
                for item in filtered:
                    priority_filter.append(int(item))
        except:
            raise ValueError('Invalid priority value. Expects a number from 1 to 10.')

    # Fetch queue data and add to priority queue
    queue = await fetch_queue_data(filter=priority_filter)
    pq = PriorityQueue()
    for item in queue:
        pq.add_to_queue(item)
    
    # Execute commands based on priority until queue is empty
    while not pq.is_empty():
        task = pq.dequeue()
        # Execute command from task
        debug_log(f'Executing priority {task["priority"]} task: {task["command"]}')

    debug_log('Exiting application...')
