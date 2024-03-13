def remove_first_n_chars(string, n):
    return string[n:]

if __name__ == "__main__":
    string = input("Enter a string: ")
    n = int(input("Enter the number of characters to remove: "))
    print("String after removing first", n, "characters:", remove_first_n_chars(string, n))
