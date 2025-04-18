import re

def check_password_strength(password):
    length_error = len(password) < 8
    uppercase_error = re.search(r'[A-Z]', password) is None
    lowercase_error = re.search(r'[a-z]', password) is None
    digit_error = re.search(r'\d', password) is None
    special_char_error = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is None

    errors = [length_error, uppercase_error, lowercase_error, digit_error, special_char_error]
    score = errors.count(False)

    # Score breakdown:
    # 0-2: Weak, 3-4: Moderate, 5: Strong
    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Moderate"
    else:
        return "Strong"

password = input("Enter your password: ")
strength = check_password_strength(password)
print(f"Password Strength: {strength}")
