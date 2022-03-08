
arr = [1, 2, 21, 4, 41]
print(arr)
def minimum(arr):
    arr.sort()
    print(arr[0])
    return arr[0]
def maximum(arr):
    arr.sort()
    print(arr[-1])
    return arr[-1]

minimum(arr)
maximum(arr)