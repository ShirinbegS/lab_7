def calculate_x_recursive(i):
    if i == 1:
        return 1
    if i == 2:
        return -1 / 8
    return ((i - 1) * calculate_x_recursive(i - 1)) / 3 + ((i - 2) * calculate_x_recursive(i - 2)) / 4
