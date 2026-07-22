class Task:

    def __init__(self, title):
        self.title = title
        self.done = False
        self.subtasks = []
    
    def add_subtask(self, subtask):
        self.subtasks.append(subtask)
    
    def remove_subtask(self, index):
        del self.subtasks[index]
    
class Subtasks(Task):

    def __init__(self, title):
        super().__init__(title)
    