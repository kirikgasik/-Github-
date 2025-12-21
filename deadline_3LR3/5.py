def deep_flatten(lst):
    result = []
    for element in lst:
        if isinstance(element, list):
            result.extend(deep_flatten(element))
        else:
            result.append(element)
    return result
mixed_lst = [1, [2.5, [True, 'hello']], None, [[['world']]]]
print(f"Исходный список: {mixed_lst}")
print(f"Плоский список:  {deep_flatten(mixed_lst)}")