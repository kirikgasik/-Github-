import random
temperatures_celsius = [random.randint(-10,30) for _ in range(14)]
print(f"Исходный список температур за 14 дней (C°): {temperatures_celsius}\n")

max_temp = max(temperatures_celsius)
min_temp = min(temperatures_celsius)
print(f"Самая высокая температура: {max_temp}°C")
print(f"Самая низкую температура:  {min_temp}°C")

average_temp = sum(temperatures_celsius) / len(temperatures_celsius)
print(f"Средняя температура за период: {average_temp:.2f}°C")
days_above_average = sum(1 for temp in temperatures_celsius if temp > average_temp)
print(f"Количество дней с температурой выше средней: {days_above_average}")
sorted_temperatures = sorted(temperatures_celsius)
print(f"Отсортированный список температур: {sorted_temperatures}")

temperatures_fahrengeit = [(celsius * 9/5 + 32) for celsius in temperatures_celsius]
print(f"\nСписок температур в Фаренгейтах (F°): {temperatures_fahrengeit}")