def somar(a=0, b=0, c=0):

    s = a + b + c

    print(f"A soma vale: {s}")

somar(5)




def teste(b):
    a = 8
    b += 4
    c = 2
    print(f"A dentro vale {a}")
    print(f"B dentro vale {b}")
    print(f"C dentro vale {c}")

a = 5
teste(a)

print(f"A fora vale {a}")
