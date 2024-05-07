import numpy as np

def decimal_para_binario(decimal):
    return np.binary_repr(decimal)

def decimal_para_hexadecimal(decimal):
    return np.base_repr(decimal, base=16).upper()

def decimal_para_octal(decimal):
    return np.base_repr(decimal, base=8)

def binario_para_decimal(binario):
    return int(binario, 2)

def hexadecimal_para_decimal(hexadecimal):
    return int(hexadecimal, 16)

def octal_para_decimal(octal):
    return int(octal, 8)

def menu():
    print("1. Decimal para Binário")
    print("2. Decimal para Hexadecimal")
    print("3. Decimal para Octal")
    print("4. Binário para Decimal")
    print("5. Hexadecimal para Decimal")
    print("6. Octal para Decimal")
    print("0. Sair")

def main():
    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '0':
            print("Obrigado por utilizar a calculadora!")
            break
        elif escolha == '1':
            decimal = int(input("Digite o número decimal: "))
            print("Binário:", decimal_para_binario(decimal))
        elif escolha == '2':
            decimal = int(input("Digite o número decimal: "))
            print("Hexadecimal:", decimal_para_hexadecimal(decimal))
        elif escolha == '3':
            decimal = int(input("Digite o número decimal: "))
            print("Octal:", decimal_para_octal(decimal))
        elif escolha == '4':
            binario = input("Digite o número binário: ")
            print("Decimal:", binario_para_decimal(binario))
        elif escolha == '5':
            hexadecimal = input("Digite o número hexadecimal: ")
            print("Decimal:", hexadecimal_para_decimal(hexadecimal))
        elif escolha == '6':
            octal = input("Digite o número octal: ")
            print("Decimal:", octal_para_decimal(octal))
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
