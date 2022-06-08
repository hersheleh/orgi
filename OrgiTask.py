import time
from enum import Enum

class TaskStatus(Enum):
    BACKLOG = 1
    TO_DO = 2
    IN_PROGRESS = 3
    DONE = 4
        

class OrgiTask:
        
    def __init__(self, description=""):
        
        self.description = description
        
        self.created_unix = time.time()
        self.created = time.localtime(self.created_unix)
        self.created_tz = time.tzname

        self.status = TaskStatus.BACKLOG

    def __str__(self):
        return f'Task({self.description}, {self.created}, {self.created_tz})'



