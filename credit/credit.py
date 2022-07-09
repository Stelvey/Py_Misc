import re
import sys

# Get a number from user (as a string)
while True:
    input = input("Number: ")
    if not re.search("\D", input):
        break

# Check network & length
if re.match("34|37", input) and len(input) == 15:
    network = "AMEX"
elif re.match("5[1-5]", input) and len(input) == 16:
    network = "MASTERCARD"
elif re.match("4", input) and len(input) in (13, 16):
    network = "VISA"
else:
    print("INVALID")
    sys.exit(1)

# Checksum
sum = 0
for i in range(len(input) - 1, -1, -1):
    # Check if it is "every other digit"
    if (len(input) % 2 == 0 and i % 2 == 0) or (len(input) % 2 == 1 and i % 2 == 1):
        # Multiply "every other digit" by 2
        digit = int(input[i]) * 2
        # If we get 2 digits, we add them to sum
        if digit > 9:
            digit = str(digit)
            sum += int(digit[0]) + int(digit[1])
        # Otherwise, we just add the number
        else:
            sum += digit
    # Add the non-"every other digit"
    else:
        sum += int(input[i])

# Only print a legit card
if sum % 10 == 0:
    print(network)
else:
    print("INVALID")