def decimal_para_binario(decimal):
    return bin(decimal)[2:]

def decimal_para_hexadecimal(decimal):
    return hex(decimal)[2:]

def decimal_para_octal(decimal):
    return oct(decimal)[2:]

def binario_para_decimal(binario):
    return int(binario, 2)

def hexadecimal_para_decimal(hexadecimal):
    return int(hexadecimal, 16)

def octal_para_decimal(octal):
    return int(octal, 8)

def main():
    while True:
        print("\nSelecione a operação:")
        print("1. Decimal para Binário")
        print("2. Decimal para Hexadecimal")
        print("3. Decimal para Octal")
        print("4. Binário para Decimal")
        print("5. Hexadecimal para Decimal")
        print("6. Octal para Decimal")
        print("7. Sair")

        escolha = input("Digite o número da operação desejada: ")

        if escolha == '7':
            print("Encerrando o programa.")
            break

        if escolha in ['1', '2', '3']:
            decimal = int(input("Digite o número decimal: "))
            if escolha == '1':
                resultado = decimal_para_binario(decimal)
                print("Binário:", resultado)
            elif escolha == '2':
                resultado = decimal_para_hexadecimal(decimal)
                print("Hexadecimal:", resultado)
            elif escolha == '3':
                resultado = decimal_para_octal(decimal)
                print("Octal:", resultado)
        elif escolha in ['4', '5', '6']:
            numero = input("Digite o número: ")
            if escolha == '4':
                resultado = binario_para_decimal(numero)
                print("Decimal:", resultado)
            elif escolha == '5':
                resultado = hexadecimal_para_decimal(numero)
                print("Decimal:", resultado)
            elif escolha == '6':
                resultado = octal_para_decimal(numero)
                print("Decimal:", resultado)
        else:
            print("Escolha inválida.")

if __name__ == "__main__":
    main()
