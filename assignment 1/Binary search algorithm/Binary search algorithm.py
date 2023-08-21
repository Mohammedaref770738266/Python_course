def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

arr = [90, 56, 7, 1, 23, 43, 87]

num = input("Enter a number you want to search ")

result = binary_search(arr, int(num))

if result != -1:
    print("Number in array at index:", result)
else:
    print("Number not found in array")