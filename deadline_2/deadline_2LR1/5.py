input_string = "Гасилов Король!"
vowels = "аеёиоуыэяaeiouy"
output_string = ""

i = 0
while i < len(input_string):
    char = input_string[i]
    if char.lower() not in vowels:
        output_string += char
    i += 1
print(output_string)