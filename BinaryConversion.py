# Function to convert decimal to binary using nested loops
def decimal_to_binary(decimal_num):
    binary_num = ""
    
    # Outer loop to find binary digits
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num = str(remainder) + binary_num
        decimal_num //= 2
    
    # If the number is 0, binary representation is 0
    if binary_num == "":
        binary_num = "0"
    
    return binary_num

# Input from the user
decimal_num = int(float(input("Enter a decimal number = ")))

# Call the function and display the result
binary_representation = decimal_to_binary(decimal_num)
print(f"Binary representation of the number is {decimal_num}.")