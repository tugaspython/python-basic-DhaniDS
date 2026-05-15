def validasi_password(password):
    if len(password) < 8 or len(password) > 20:
        return False

    has_upper = False
    has_digit = False
    has_symbol = False
    has_space = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in "!@#$%^&*":
            has_symbol = True
        elif char == " ":
            has_space = True

    if has_space:
        return False

    if has_upper and has_digit and has_symbol:
        return True
    else:
        return False
