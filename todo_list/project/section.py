from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        searched_task = [t for t in self.tasks if t.name == task_name]
        if not searched_task:
            return f"Could not find task with the name {task_name}"
        searched_task[0].completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        completed_tasks = 0
        for task in self.tasks:
            if task.completed:
                completed_tasks += 1
                self.tasks.remove(task)
        return f"Cleared {completed_tasks} tasks."

    def view_section(self):
        resulst = f"Section {self.name}:\n"
        for task in self.tasks:
            resulst += f"{task.details()}\n"
        return resulst
