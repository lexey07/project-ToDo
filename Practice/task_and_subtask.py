tasks = []
task_count = 5

class Tasks:

    def __init__(self, title):
        self.title = title
        self.done = False
        self.subtasks = []
    
    def add_task(self, task):
        if len(self.tasks) < task_count:
            self.tasks.append(task)
        else:
            self.tasks.pop()
            self.tasks.insert(0, task)
    
    def remove_task(self, task_number):
        if 1 <= task_number <= task_count:
            del task_number - 1
    
    def marker_task(self, task_number):
        if 1 <= task_number <= task_count:
            self.done = not self.done

        for subtask in self.subtasks:
            subtask.done = self.done
    
    

class Subtasks(Tasks):

    def __init__(self, title):
        super().__init__(title)
        self.done = False
    
    def add_subtask(self, subtask, user_input, current_subtask):
        if user_input.startswith("-"):
            if current_subtask is None:
                return
            else:
                self.subtasks.append(subtask)

