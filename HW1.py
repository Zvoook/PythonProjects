# Example:
# input
a = [-3, -2, 0, 1, 3, 5]
# result [0, 1, 2, 3, 3, 5]
if len(a) > 0:
    p1, p2 = 0, len(a) - 1
    result = list()
    while p1 != p2:
        if abs(a[p1]) >= abs(a[p2]):
            result.insert(0, abs(a[p1]))
            p1 += 1
        else:
            result.insert(0, abs(a[p2]))
            p2 -= 1
    result.insert(0, abs(a[p1]))
    print(f"{result}")
else:
    print("Array is empty!")
