"""
Check that the list is monotonically growing, decreasing
"""

arr = [input(), input(), input(), input()]

flag = None
for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1] and (flag is None or flag == 1 or flag == 3):
        flag = 1
        continue
    elif arr[i] > arr[i + 1] and flag == 2:
        flag = False

    if arr[i] < arr[i + 1] and (flag is None or flag == 2 or flag == 3):
        flag = 2
        continue
    elif arr[i] < arr[i + 1] and flag == 1:
        flag = False

    if arr[i] == arr[i + 1] and (flag is None or flag == 1 or flag == 2 or flag == 3):
        flag = 3
        continue
    else:
        flag = False

if flag in [1, 2, 3]:
    print('YES')
else:
    print('NO')
