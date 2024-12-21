A = {x for x in range(1, 41) if x % 2 == 0}

B = {x for x in range(1, 41) if x % 3 == 0}

C = {x for x in A if x % 3 == 0}

D = {x for x in A.union(B) if x % 12 == 0}

print("Множина A:", A)
print("Множина B:", B)
print("Множина C (діляться на 2 і на 3):", C)
print("Множина D (діляться на 12):", D)
