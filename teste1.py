verdade = True;

while verdade:
    try:
        num1 = float(input("Número 1: "))
        if not -999999 <= num1 <= 999999:
            raise ValueError(" - Erro1")
        num2 = float(input("Número 2: "))
        if not -999999 <= num2 <= 999999:
            raise ValueError(" - Erro2")
        op = str(input("Operação ou s para sair: "))
        if op == "+" :
            print("O resultado da soma é: ", num1 + num2)
        elif op == "-":
            print("O resultado da subtração é: ", num1 - num2)
        elif op == "/":
            print("O resultado da divisão é: ", num1 / num2)
        elif op == "*":
            print("O resultado da multiplicação é: ", num1 * num2)
        elif op == "s":
            break;
        else:
            raise ValueError("OP não reconhecido!")
    except ValueError as e:
        print("Inválido!", e)

    else:
        break




