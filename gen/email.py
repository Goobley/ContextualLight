def reversed_rot13(s):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    lower = s.lower()
    encoded_lower = "".join([alpha[(alpha.index(a) + 13) % 26] if a in alpha else a for a in lower])
    encoded = "".join([a.upper() if s[i].isupper() else a for i, a in enumerate(encoded_lower)])
    return encoded[::-1]