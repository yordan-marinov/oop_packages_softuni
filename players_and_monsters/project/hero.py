class Hero:
    def __init__(self, username: str, level: int):
        self.username: str = username
        self.level: int = level

    def __repr__(self):
        return f"{self.username} of type {type(self).__name__} has level {self.level}"
