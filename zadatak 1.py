c_b, c_j, c_k = list(map(int, input().split()))
k_b, k_j, k_k = list(map(int, input().split()))

ukupna_cijena = c_b * k_b * c_j * k_j * c_k * k_k

print(ukupna_cijena)
