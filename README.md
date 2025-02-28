# Algoritmo de Karatsuba

## Descrição do Projeto

Este projeto implementa o algoritmo de Karatsuba para multiplicação eficiente de dois números inteiros. O algoritmo reduz a complexidade da multiplicação tradicional, dividindo os números em partes menores e combinando os resultados de forma mais eficiente.

### Lógica do Algoritmo

1. **Caso base:** Se os números forem pequenos, realiza a multiplicação diretamente.
2. **Divisão:** Divide os números em partes superiores e inferiores.
3. **Recursão:** Aplica a multiplicação de Karatsuba em três subproblemas menores.
4. **Combinação:** Usa os produtos intermediários para calcular o resultado final.

O código está implementado no arquivo `main.py`.

### Explicação linha a linha do código

```python
    if x < 10 or y < 10:
        return x * y
```
Caso base: se um dos números for menor que 10, a multiplicação é feita diretamente.

```python
    n = max(len(str(x)), len(str(y)))
    m = n // 2
```
Determina o número de dígitos do maior número e divide esse valor por 2 para separar os números.

```python
    high1, low1 = divmod(x, 10**m)
    high2, low2 = divmod(y, 10**m)
```
Divide os números `x` e `y` em duas partes: `high` (parte alta) e `low` (parte baixa).

```python
    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)
```
Realiza chamadas recursivas para multiplicar as partes divididas.

```python
    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0
```
Combina os resultados intermediários para formar o produto final.

```python
if __name__ == "__main__":
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    resultado = karatsuba(num1, num2)
    print(f"Resultado da multiplicação: {resultado}")
```
Bloco principal do script: solicita dois números ao usuário, chama a função `karatsuba` e exibe o resultado.

## Como Executar o Projeto

1. Clone este repositório:
   ```sh
   git clone https://github.com/JoseMiguel-ofc/FPAA_Trabalho_Individual.git
   ```
2. Acesse o diretório do projeto:
   ```sh
   cd FPAA_trabalho_individual
   ```
3. Execute o script:
   ```sh
   python main.py
   ```
4. Insira dois números inteiros para multiplicação.

## Relatório Técnico

### Análise da Complexidade Ciclomática

O fluxo de controle da função `karatsuba` pode ser representado por um grafo com os seguintes elementos:

- **N (nós):** 7
- **E (arestas):** 8
- **P (componentes conexos):** 1

A complexidade ciclomática é calculada como:

\[ M = E - N + 2P \]

\[ M = 8 - 7 + 2(1) = 3 \]

### Análise da Complexidade Assintótica

- **Complexidade temporal:** O algoritmo de Karatsuba tem complexidade \( O(n^{\log_2 3}) \approx O(n^{1.585}) \).
- **Complexidade espacial:** \( O(n) \) devido às chamadas recursivas e armazenamento temporário.
- **Melhor caso:** Quando os números têm apenas um dígito, o algoritmo executa em \( O(1) \).
- **Caso médio e pior caso:** Ambos seguem \( O(n^{1.585}) \) devido às chamadas recursivas sucessivas.

---

