from operator import itemgetter

from utils.index import debug_log


class PriorityQueue(object):
    """
    Creates a PriorityQueue that queues and dequeues based on priority using FIFO
    """
    def __init__(self):
        self.queue = {}


    def is_empty(self):
        """
        Check if queue is empty
        """
        return len(self.queue.keys()) == 0


    def add_to_queue(self, task):
        """
        Adding a task to the queue
        Args:
            task: (dict) of { "priority": int, "task": str }
        """
        priority, command = itemgetter('priority', 'command')(task)
        if (self.queue.get(priority)):
            self.queue[priority].append(command)
        else:
            self.queue[priority] = [command]


    def dequeue(self):
        """
        Popping a task based on priority
        Returns:
            task: (dict) of { "priority": int, "task": str }
        """
        if (not self.is_empty()):
            priority_index = min(self.queue.keys())
            first_item = self.queue[priority_index].pop(0)
            if (len(self.queue[priority_index]) == 0):
                del self.queue[priority_index]
            return {
                'priority': priority_index,
                'command': first_item,
            }
        else:
            debug_log('Queue is empty')
            return None