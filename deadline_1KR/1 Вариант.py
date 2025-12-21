from typing import List, Union
def parse_expression(expression: str) -> tuple[List[Union[int, float]], List[str]]:
    expr = expression.replace(' ', '')
    numbers = []
    operators = []
    current_num = ''
    for char in expr:
        if char.isdigit() or char == '.':
            current_num += char
        elif char in '+-*/':
            if current_num == '':
                raise ValueError('Выражение начинается с оператора')
            if '.' in current_num:
                numbers.append(float(current_num))
            else:
                numbers.append(int(current_num))
            current_num = ''
            operators.append(char)
        else:
            raise ValueError(f'Недопустимый символ: {char}')
    if current_num == '':
        raise ValueError('Выражение заканчивается оператором')
    if '.' in current_num:
        numbers.append(float(current_num))
    else:
        numbers.append(int(current_num))
    return numbers, operators
def calculate(numbers: List[Union[int, float]], operators: List[str]) -> Union[int, float]:
    if len(operators) < 1 or len(operators) > 2:
        raise ValueError('Должно быть 1 или 2 оператора')
    if len(operators) == 1:
        return _execute_operation(numbers[0], numbers[1], operators[0])
    if operators[0] in '*/':
        temp_result = _execute_operation(numbers[0], numbers[1], operators[0])
        return _execute_operation(temp_result, numbers[2], operators[1])
    elif operators[1] in '*/':
        temp_result = _execute_operation(numbers[1], numbers[2], operators[1])
        return _execute_operation(numbers[0], temp_result, operators[0])
    else:
        temp_result = _execute_operation(numbers[0], numbers[1], operators[0])
        return _execute_operation(temp_result, numbers[2], operators[1])
def _execute_operation(a: Union[int, float], b: Union[int, float], op: str) -> Union[int, float]:
    match op:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            if b == 0:
                raise ZeroDivisionError('Деление на ноль')
            result = a / b
            if isinstance(a, int) and isinstance(b, int) and a % b == 0:
                return int(result)
            return result
        case _:
            raise ValueError(f'Неподдерживаемый оператор: {op}')
def main() -> None:
    print('Калькулятор математических выражений')
    print('Поддерживаются выражения с 1 или 2 операторами')
    print('Примеры: "2 + 3", "2 + 3 * 4", "9 / 3"')
    print('Для выхода введите "exit"')
    print('=' * 50)
    while True:
        try:
            expression = input('\nВведите выражение: ').strip()
            if expression.lower() == 'exit':
                print('Выход из программы')
                break
            if not expression:
                print('Ошибка: введите выражение')
                continue
            numbers, operators = parse_expression(expression)
            result = calculate(numbers, operators)
            print(f'Результат: {result}')
        except ValueError as e:
            print(f'Ошибка: {e}')
        except ZeroDivisionError as e:
            print(f'Ошибка: {e}')
        except Exception as e:
            print(f'Неизвестная ошибка: {e}')
if __name__ == '__main__':
    main()