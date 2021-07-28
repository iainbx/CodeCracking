def shiftChar(char, shift):
    charCode = ord(char) + shift
    charCode = (charCode % 90) + (65 * (charCode // 90))
    return chr(charCode)

print(shiftChar('a',3))