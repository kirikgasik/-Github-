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
        print("\nСписок задач:")
        print("-" * 30)
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
    def remove_task(self, description):
        for i, task in enumerate(self.tasks):
            if task.description == description:
                removed_task = self.tasks.pop(i)
                print(f"Удалена задача: {removed_task.description}")
                return True
        print(f"Задача '{description}' не найдена")
        return False
    def sort_by_priority(self, reverse=True):
        self.tasks.sort(key=lambda task: task.priority, reverse=reverse)
        order = "по убыванию" if reverse else "по возрастанию"
        print(f"Задачи отсортированы {order} приоритета")
    def get_high_priority_tasks(self, threshold=5):
        high_priority = [task for task in self.tasks if task.priority >= threshold]
        return high_priority
    def clear_all_tasks(self):
        self.tasks.clear()
        print("Все задачи удалены")
    def get_task_count(self):
        return len(self.tasks)
print()
work_manager = TaskManager()
work_manager.add_task("Подготовить отчет", 8)
work_manager.add_task("Встреча с клиентом", 9)
work_manager.add_task("Позвонить поставщику", 3)
work_manager.add_task("Проверить почту", 2)
work_manager.add_task("Запланировать отпуск", 5)
work_manager.show_tasks()