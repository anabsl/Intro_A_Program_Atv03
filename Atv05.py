def calculadora():
    while True:
        print("\nOperações disponíveis:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        escolha = int(input("Digite o número da operação desejada: "))

        if escolha == 0:
            print("Saindo da calculadora. Até mais!")
            break
        elif escolha in range(1, 5):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == 1:
                resultado = num1 + num2
            elif escolha == 2:
                resultado = num1 - num2
            elif escolha == 3:
                resultado = num1 * num2
            elif escolha == 4:
                # Verifica se o segundo número não é zero para evitar a divisão por zero
                resultado = num1 / num2 if num2 != 0 else "Erro: Divisão por zero"
            
            print(f"Resultado: {resultado}")
        else:
            print("Essa opção não existe. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    calculadora()