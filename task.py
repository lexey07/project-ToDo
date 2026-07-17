class Task:

    def __init__(self, title):
        self.title = title
        self.done = False
        self.subtasks = []

    def add_subtask(self, subtask):
        self.subtasks.append(subtask)
    
    def toggle_done(self):
        self.done = not self.done

        for subtask in self.subtasks:
            subtask.done = self.done
        
    def toggle_subtask(self, index):
        subtask = self.subtasks[index]
        subtask.done = not subtask.done

        self.done = all(subtask.done for subtask in self.subtasks)
    
    def remove_subtask(self, index):
        del self.subtasks[index]

        if self.subtasks:
            self.done = all(subtask.done for subtask in self.subtasks)
        else:
            self.done = False