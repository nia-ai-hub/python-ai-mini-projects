
import secrets
import string
from pathlib import Path


chars = string.ascii_letters + string.digits + "!@#$%&*"


website = input("Where is this password for? ")
length = int(input("Password length: "))


password = "".join(
    secrets.choice(chars) for _ in range(length)
)


print("\nYour password:", password)


file_path = Path(__file__).with_name("passwords.txt")

with open(file_path, "a", encoding="utf-8") as file:
    file.write(f"Website: {website}\n")
    file.write(f"Password: {password}\n")
    file.write("-" * 30 + "\n")

print("Password saved to passwords.txt")