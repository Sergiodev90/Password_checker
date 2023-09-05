import random


lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "123456789"
symbols = "!@#$%^&*()_+[]|;:,.<>?~"

unionPassword = lowercase + uppercase + numbers + symbols
maxiumlenghtPassword = 12

password = "".join(random.sample(unionPassword,maxiumlenghtPassword))

print(f"your passwords is: {password}") 