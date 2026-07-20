class TaskList:

    """
    '_instance' - атрибут класса, а не объекта. То есть он существует в единственном
    экземпляре для всего класса 'TaskList'. 
    Пока в нём хранится 'None' -> объект еще не создан.
    """
    _instance = None
    task_count = 5

    """
    'cls' - ссылка на класс (Обшепринятое название переменной).
    '__new__()' - создает объект.
    'instance' - позволяет проверять принадлежность классу.
    """
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        
        return cls._instance

    """
    'hasattr' проверяет, есть ли у объекта атрибут '_initialized'.
    Если нет - значит объект создается впервые. Создаем список и ставим метку 'self._initialized = True'
    Если есть - значит объект был запущен раньше, поэтому сразу выходим из '__init__()'.
    """
    def __init__(self):
        if hasattr(self, "_initialized"):
            return

        self._tasks = []
        self._initialized = True
    
    """Добавление задачи"""
    def add_task(self, task):
        if len(self._tasks) < self.task_count:
            self._tasks.append(task)
        else:
            self._tasks.pop()
            self._tasks.insert(0, task)

    """Удаление задачи"""
    def remove_task(self, index):
        del self._tasks[index]
    
    """Получение задачи"""
    def get_task(self, index):
        return self._tasks[index]

    """Получение всех задач"""
    def get_tasks(self):
        return self._tasks
    
    """Проверка на пустоту"""
    def is_empty(self):
        return len(self._tasks) == 0
    
task_list = TaskList()
