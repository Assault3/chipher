in_text = hello world  #-> catca tcatc -> jeeno pqref
key = cat
in_text = list(in_text)
key = list(key)
key_len = len(key)
count = 0
key_text = []
for i in range(len(in_text)):
    if not 97 <= ord(in_text[i]) <= 122:
        key_text.append(in_text[i])
        count += 1
    else:
        key_text.append(key[(i - count) % key_len])
vigenere = 
for i in range(len(in_text)):
    if not 97 <= ord(in_text[i]) <= 122:
        char = in_text[i]
    else:
        char = chr(97 + (ord(in_text[i]) + ord(key_text[i]) - 97 - 97) % 26)
    vigenere += char
print(vigenere)
