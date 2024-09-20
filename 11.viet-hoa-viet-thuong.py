s = input()

def convert_string(s: str) -> str:
    lower_str_cnt = sum(1 for c in s if c.islower())
    upper_str_cnt = sum(1 for c in s if c.isupper())
    if lower_str_cnt >=  upper_str_cnt:
        return s.lower()
    else: return s.upper()

print(convert_string(s))