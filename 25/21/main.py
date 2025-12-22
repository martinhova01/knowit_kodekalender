c = "VEFZSPIUHRZ"
p = "RØDTOGGRØNT"

alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"
assert len(alph) == 29


key = []
for i in range(len(c)):
    key.append((alph.index(c[i]) - alph.index(p[i])) % len(alph))


print(key)

KEY = [4, 6, 2, 6, 4, 9, 2, 3, 9]

cipher = "JUTGRPCUJWPGTXRNQRWYGT"


res = ""
for i in range(len(cipher)):
    res += alph[(alph.index(cipher[i]) - KEY[i % len(KEY)]) % len(alph)]

print(res)
