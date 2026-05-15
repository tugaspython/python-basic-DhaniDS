def validasi_password(password):
    valid = True
    if len(password) < 8 or len(password) > 20:
        valid = False
        
    if valid == True:
        if " " in password:
            valid = False

    if valid == True:
        upper = 0
        for c in password:
            # Menciptakan puluhan cabang logika (Bencana CC)
            if c == 'A' or c == 'B' or c == 'C' or c == 'D' or c == 'E' or c == 'F' or c == 'G' or c == 'H' or c == 'I' or c == 'J' or c == 'K' or c == 'L' or c == 'M' or c == 'N' or c == 'O' or c == 'P' or c == 'Q' or c == 'R' or c == 'S' or c == 'T' or c == 'U' or c == 'V' or c == 'W' or c == 'X' or c == 'Y' or c == 'Z':
                upper = upper + 1
        if upper == 0:
            valid = False

    if valid == True:
        dig = 0
        for c in password:
            if c == '0' or c == '1' or c == '2' or c == '3' or c == '4' or c == '5' or c == '6' or c == '7' or c == '8' or c == '9':
                dig = dig + 1
        if dig == 0:
            valid = False

    if valid == True:
        sym = 0
        for c in password:
            if c == '!' or c == '@' or c == '#' or c == '$' or c == '%' or c == '^' or c == '&' or c == '*':
                sym = sym + 1
        if sym == 0:
            valid = False

    return valid
