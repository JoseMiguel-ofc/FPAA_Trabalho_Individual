def karatsuba(x, y):

    # Caso base: verifica se os números são pequenos. Nesse caso, faz a multiplicação direta
    if x < 10 or y < 10:
        return x * y
    
    # Determinar o tamanho dos números
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    
    # Dividir os números em duas partes
    high1, low1 = divmod(x, 10**m)
    high2, low2 = divmod(y, 10**m)
    
    # Recursivamente calcular os três produtos
    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)
    
    # Combina os resultados obtidos anteriormente para calcular o resultado final
    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0


if __name__ == "__main__":
    # Teste do algoritmo
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    resultado = karatsuba(num1, num2)
    print(f"Resultado da multiplicação: {resultado}")
