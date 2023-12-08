c = int(input())

jedinica = c % 10

stotica = c // 100 * 100

desetica = c - (jedinica * stotica)

print(jedinica)
print(desetica)
print(stotica)
