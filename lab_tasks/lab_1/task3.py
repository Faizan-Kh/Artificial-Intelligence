def print_even_indices(input_string):
    even_indices_characters= input_string[::2]
    print("Characters at even indices:", even_indices_characters)

# testing the function
input_string= "Hello, World!"
print_even_indices(input_string)