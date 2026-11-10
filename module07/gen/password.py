import string
import random

# generate 100 passwords


def generate_strong_password(length=16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ""
        for _ in range(length):
            password += random.choice(alphabet)
            
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_spec  = any(c in string.punctuation for c in password)
        
        if has_lower and has_upper and has_digit and has_spec:
            yield password

i = 0
for password in generate_strong_password():
    print(password)
    if i == 10:
        break
    i += 1
