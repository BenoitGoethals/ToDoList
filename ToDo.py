class ToDoItem:

    def __init__(self, id_todo, description, start, end, done) -> object:
        self.id_todo = id_todo
        self.description = description
        self.start = start
        self.end = end
        self.done = done

    def __str__(self) -> str:
        return f"{self.id_todo} {self.description}"
