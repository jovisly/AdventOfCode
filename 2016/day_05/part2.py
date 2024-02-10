import hashlib
import utils


def get_pswd(start):
    pswd = "*" * 8
    i = 0
    while pswd.count("*") > 0:
        combo = start + str(i)
        hashed = hashlib.md5(combo.encode("utf-8"))
        hashed_str = hashed.hexdigest()
        if hashed_str.startswith("00000"):
            char = hashed_str[6]
            ind = hashed_str[5]
            if ind.isdigit() and int(ind) >= 0 and int(ind) < 8 and pswd[int(ind)] == "*":
                pswd_chars = list(pswd)
                pswd_chars[int(ind)] = char
                pswd = "".join(pswd_chars)
                print(pswd)
        i += 1
    return pswd



# start = "abc"
start = "ugkcyxxp"
pswd = get_pswd(start)
print(pswd)
