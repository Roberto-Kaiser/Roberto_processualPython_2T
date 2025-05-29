def validar_nome(nome):
    for caractere in nome:
        if not (caractere.isalpha() or caractere.isspace()):
            return False
    return True

nomes = []
print("Insira 10 nomes:")
for i in range(1, 11):
    while True:
        nome = input(f"Nome{i}:")
        
        if not validar_nome(nome):
            print("Caracter inválido na lista. Usa só letra bobão!")
            exit()
        nomes.append(nome)
        break

nomes_ordenados = sorted(nomes)
print("Nomes em ordem alfabética:")
for nome in nomes_ordenados:
    letras = len([c for c in nome if c.isalpha()])
    print(f"{nome} - {letras} letras")
