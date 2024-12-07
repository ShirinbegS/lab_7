def calculate_x(i):
    if i == 1:
        return 1
    if i == 2:
        return -1 / 8
    x_prev2 = 1  # x_1
    x_prev1 = -1 / 8  # x_2
    for n in range(3, i + 1):
        x_current = ((n - 1) * x_prev1) / 3 + ((n - 2) * x_prev2) / 4
        x_prev2, x_prev1 = x_prev1, x_current
    return x_prev1
