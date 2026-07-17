from utils import TASK_COUNT

class TaskList:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        
        return cls._instance

    def __init__(self):
        if hasattr(self, "_initialized"):
            return

        self._tasks = []
        self._initialized = True
    
    def add_task(self, task):
        if len(self._tasks) < TASK_COUNT:
            self._tasks.append(task)
        else:
                self._tasks.pop()
                self._tasks.insert(0, task) 

    def remove_task(self, index):
        del self._tasks[index]
    
    def get_task(self, index):
        return self._tasks[index]

    def get_tasks(self):
        return self._tasks

    def is_empty(self):
        return len(self._tasks) == 0

task_list = TaskList()
