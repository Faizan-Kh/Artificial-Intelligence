def element_wise_addition(arr1, arr2):
    return [x + y for x, y in zip(arr1, arr2)]

if __name__ == "__main__":
    array1 = [1, 2, 3]
    array2 = [4, 5, 6]
    print("Element-wise addition:", element_wise_addition(array1, array2))
