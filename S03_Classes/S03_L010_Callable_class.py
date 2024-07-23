class MemoryClas:
    def __init__(self, list):
        self.list_of_items = list

    def __call__(self, item):
        self.list_of_items.append(item)

mem = MemoryClas([])
print("List of items in memory", mem.list_of_items)

mem.list_of_items.append('buy sugar')
print("List of items in memory", mem.list_of_items)

mem('buy milk')
print("List of items in memory", mem.list_of_items)

print('This class is callable:', callable(MemoryClas)) #domyślnie jest callable
print('This class is callable:', callable(mem)) #domyślnie nie jest callable - staje się callable jak się doda obsługę predefiniowanej funkcji __call__