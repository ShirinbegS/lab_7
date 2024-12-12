def count(lst):
    n = 0
    for item in lst:
        if isinstance(item,list):  # Если элемент — это список
            n += count(item)
            n+=1  # Рекурсивно считаем элементы в этом подсписке
        else:
            n += 1 
    return n
print(count([1, 2, [3, 4, [5]]]))