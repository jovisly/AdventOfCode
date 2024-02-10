import hashlib
import utils

# Based on 2015 day 4.
def get_pswd(start):
    pswd = ""
    i = 0
    while len(pswd) < 8:
        combo = start + str(i)
        hashed = hashlib.md5(combo.encode("utf-8"))
        hashed_str = hashed.hexdigest()
        if hashed_str.startswith("00000"):
            pswd += hashed_str[5]
            # print(hashed_str)
        i += 1
    return pswd


# start = "abc"
start = "ugkcyxxp"
pswd = get_pswd(start)
print(pswd)
