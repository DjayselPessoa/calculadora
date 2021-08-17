ativo = True;

while ativo:
    try:
        num1 = float(input("Número 1: "))
        if not -999999 <= num1 <= 999999:
            raise ValueError(" - número inválido!")
        num2 = float(input("Número 2: "))
        if not -999999 <= num2 <= 999999:
            raise ValueError(" - número inválido!")
        op = str(input("Operação ou s para sair: "))
        if op == "+" :
            print(f"{num1}  +  {num2}  =  {num1 + num2}")
        elif op == "-":
            print(f"{num1}  -  {num2}  =  {num1 - num2}")
        elif op == "/":
            print(f"{num1}  /  {num2}  =  {num1 / num2}")
        elif op == "*":
            print(f"{num1}  *  {num2}  =  {num1 * num2}")
        elif op == "s":
            print("Desligando calculadora!")
            break;
        else:
            raise ValueError("OP não reconhecido!")
    except ValueError as e:
        print("Inválido!", e)

    else:
        break



