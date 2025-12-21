class SmartList(list):
    def __getitem__(self, index):
        if isinstance(index, int) and index < 0:
            new_index = -index - 1
            if new_index >= len(self):
                raise IndexError("list index out of range")
            return super().__getitem__(new_index)
        return super().__getitem__(index)
    def __setitem__(self, index, value):
        if isinstance(index, int) and index < 0:
            new_index = -index - 1
            if new_index >= len(self):
                raise IndexError("list assignment index out of range")
            super().__setitem__(new_index, value)
        else:
            super().__setitem__(index, value)
            print()
normal_list = [100, 200, 300, 400, 500]
smart_list = SmartList([100, 200, 300, 400, 500])
print("Индексы для сравнения:")
indices = [0, 1, -1, -2, -3, -4, -5]
print("Индекс | Обычный список | SmartList")
print("-" * 40)
for idx in indices:
    try:
        normal_val = normal_list[idx]
    except IndexError:
        normal_val = "IndexError"
    try:
        smart_val = smart_list[idx]
    except IndexError:
        smart_val = "IndexError"
    print(f"{idx:6} | {normal_val:14} | {smart_val}")