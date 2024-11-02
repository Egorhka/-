def find_first_index(items, item):
    try:
        return items.index(item)
    except ValueError:
        return None

# Данные
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

# Проверка для каждого товара в списке поиска
for find_item in ['банан', 'груша', 'персик']:
    index_item = find_first_index(items_list, find_item)  # Вызов функции
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")