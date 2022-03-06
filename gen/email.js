function reversed_rot13(s) {
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    encoded = s.replace(/[a-z]/gi, a => alpha[(alpha.indexOf(a) + 13) % 26 + ((alpha.indexOf(a) >= 26) ? 26 : 0)])
    return encoded.split("").reverse().join("")
}