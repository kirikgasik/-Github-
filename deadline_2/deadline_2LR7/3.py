
call_counter = 0
def increment_counter():
    """
    Увеличивает глобальную переменную call_counter на 1 при каждом вызове.
    """
    global call_counter
    call_counter = call_counter + 1
print(f"Начальное значение счетчика: {call_counter}")
increment_counter()
print(f"После 5 вызова: {call_counter}")
increment_counter()
print(f"После 15 вызова: {call_counter}")
increment_counter()
print(f"После 25 вызова: {call_counter}")
print(f"\nИтоговое значение счетчика: {call_counter}")
