def voto(idade):
    ano = 2022
    idade = ano - nascimento
    
    if idade <= 15:
        return print(f"Com {idade} anos: NÃO VOTA!")
    elif idade >= 16 and idade <= 17:
        return print(f"Com {idade} anos: VOTO OPCIONAL!")
    elif idade >= 18 and idade <= 64:
        return print(f"Com {idade} anos: VOTO OBRIGATÓRIO!")
    elif idade >= 65:
        return print(f"Com {idade} : VOTO OPCIONAL!")
    else:
        return True




nascimento = int(input("Qual é o seu ano de nascimento?: "))

print(voto(nascimento))