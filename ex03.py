lista = [["", 0], ["", 0], ["", 0]]

for l in range(3):
    lista[l][0] = input(f"Digite o nome para pessoa [{l+1}]: ")
    lista[l][1] = int(input(f"Digite a idade para pessoa [{l+1}]: "))

for l in range(3):
    print(f"Pessoa [{l+1}] - {lista[l]}")
