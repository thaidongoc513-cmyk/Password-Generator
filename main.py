from generator import generate_password

length = int(input("Password length: "))

password = generate_password(length)

print("\nGenerated Password:")
print(password)
