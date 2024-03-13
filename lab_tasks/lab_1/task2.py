def sum_of_current_prev_number():
    previous_number = 0
    for current_number in range(1, 11):
        sum_of_numbers = current_number + previous_number
        print(f"Current number: {current_number}, Previous number: {previous_number}, Sum: {sum_of_numbers}")
        previous_number = current_number

# Call the function to execute its code
sum_of_current_prev_number()
