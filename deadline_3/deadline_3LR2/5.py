def flat_gen(nested_list):
    for sublist in nested_list:
        yield from sublist
nested = [
     ['a', 'b', 'c'],
    [10, 20],
    ['x', 'y', 'z', 'w']
]
for item in flat_gen(nested):
    print(item, end= " ")
