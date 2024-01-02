def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        # Verifica se o segundo número não é zero para evitar a divisão por zero
        return num1 / num2 if num2 != 0 else 0
    else:
        print("Operação não reconhecida. Resultado: 0")
        return 0

# Exemplo de uso:
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = int(input("Escolha a operação (1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão): "))

resultado = calculadora(numero1, numero2, operacao)
print(f"O resultado da operação é: {resultado}")
