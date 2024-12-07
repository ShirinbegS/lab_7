def count(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):  # Если элемент — это список
            total += count(item)
            total +=1  # Рекурсивно считаем элементы в этом подсписке
        else:
            total += 1  # Увеличиваем счётчик для обычных элементов
    return total
print(count([1, 2, [3, 4, [5]]]))