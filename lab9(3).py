element_masses = {
    "Гідроген": 1.008,
    "Гелій": 4.0026,
    "Літій": 6.94,
    "Берилій": 9.0122,
    "Бор": 10.81,
    "Карбон": 12.011,
    "Нітроген": 14.007,
    "Оксиген": 15.999,
}

N = int(input("Введіть кількість додаткових елементів: "))
for _ in range(N):
    element_name = input("Введіть назву елемента: ")
    atomic_mass = float(input(f"Введіть атомну масу для {element_name}: "))
    element_masses[element_name] = atomic_mass

sorted_element_masses = dict(sorted(element_masses.items(), key=lambda item: item[1]))
print("Відсортований словник атомних мас:")
for element, mass in sorted_element_masses.items():
    print(f"{element}: {mass}")
