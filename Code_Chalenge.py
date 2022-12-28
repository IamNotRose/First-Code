# criar uma array "numbers = [1, 4, 6, 8, 20, 50]".
# desenvolver uma forma de verificação de número específico dentro da array e mostrar a mensgem "x número existe".
# mostrar mensagem de erro caso o número especificado não exista na array.

busca = int(input('Insira o número a verificar:'))

numbers = [1, 4, 6, 8, 20, 50]

def verificacao(num):
    for i in numbers:
        if i == num:
            print(f"{busca} existe")
            return
    print(f"{busca} não existe")
verificacao(busca)