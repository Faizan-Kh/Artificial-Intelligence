def calculate(num1, num2):
    product= num1 * num2
    if product <= 1000:
        return product
    else: 
        return num1+num2
    
# tesing the funtion

num1= 10
num2= 5

result= calculate(num1, num2)
print("result:", result)