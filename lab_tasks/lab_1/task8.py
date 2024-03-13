def remove_duplicates(arr):
    return list(set(arr))

if __name__ == "__main__":
    array_with_duplicates = [1, 2, 2, 3, 3, 4, 5]
    print("Unique elements:", remove_duplicates(array_with_duplicates))
