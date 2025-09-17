# Example:
# input
a = [-3, -2, 0, 1, 3, 5]
# result [0, 1, 2, 3, 3, 5]

p1 = 0
p2 = pp2 = len(a) - 1

ls = list()
while p1 != p2:
    if abs(a[p1]) >= abs(a[p2]):
        ls.insert(0, abs(a[p1]))
        p1 += 1
    else:
        ls.insert(0, abs(a[p2]))
        p2 -= 1
ls.insert(0, abs(a[p1]))

print("Solution with list:", f"{ls=}")
