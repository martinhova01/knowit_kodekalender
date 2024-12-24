
cipher = open("kryptert.txt", "rb").read()
known_prefix = "Da-"
plaintext = list(known_prefix.encode("utf-8"))
start = 0

for i in range(len(known_prefix), len(cipher) - len(known_prefix)):
    section = []
    for j in range(1, 3):
        section.append(cipher[i + j] ^ plaintext[j - 1])
    
    decoded = bytes(section).decode(errors="replace")
    if decoded == "a-":
        start = i
        break
    
for i in range(start + len(known_prefix), len(cipher)):
    plain_i = i - (start + len(known_prefix)) + 2
    plaintext.append(cipher[i] ^ plaintext[plain_i])
print(bytes(plaintext).decode("utf-8", errors="replace"))