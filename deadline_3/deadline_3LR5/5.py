class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
    def __str__(self):
        return f"{self.description} - {self.priority}"
    def __repr__(self):
        return f"Task('{self.description}', {self.priority})"
class TaskManager:
    def __init__(self):    
        self.tasks = []
    def add_task(self, description, priority):
        task = Task(description, priority)
        self.tasks.append(task)
        print(f"Добавлена задача: {description} (приоритет: {priority})")
    def show_tasks(self):
        if not self.tasks:
            print("Список задач пуст")
            return
        print("\nВсе задачи:")
        print("-" * 30)
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
    def get_high_priority_tasks(self, min_priority):
        high_priority_tasks = [task for task in self.tasks if task.priority >= min_priority]
        return high_priority_tasks
    def show_high_priority_tasks(self, min_priority):
        high_priority = self.get_high_priority_tasks(min_priority)
        if not high_priority:
            print(f"\nНет задач с приоритетом {min_priority} и выше")
            return
        print(f"\nЗадачи с приоритетом {min_priority}+:")
        print("-" * 30)
        for i, task in enumerate(high_priority, 1):
            print(f"{i}. {task}")
        print()
        print()
manager = TaskManager()
manager.add_task("Купить хлеб", 1)
manager.add_task("Сделать домашку", 10)
manager.add_task("Почистить зубы", 3)
manager.add_task("Сдать проект", 8)
manager.add_task("Позвонить маме", 5)
print("\n" + "="*40)
manager.show_tasks()
print("\n" + "="*40)
important = manager.get_high_priority_tasks(5)
print("Важные задачи (приоритет 5+):")
for task in important:
    print(f"  - {task.description}")

