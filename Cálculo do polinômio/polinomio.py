def Calculo(n):
    num_raiz = []
    for i in range (n-1, -1, -1):
        elementos = float(input('Informe o elemento:'))
        num_raiz.append(elementos)
    coef = [0] * (n + 1)
    coef[n] = 1
    print(num_raiz)
    for i in range(1, n + 1):
        for j in range(n - i - 1, n):
            coef[j] += ((-1) * num_raiz[i-1] * coef[j+1])
    coef = coef[::-1]
    print("Polinomio:")
    for i in coef:
        print(i)
def main():
    quant = int(input('Informe a quantidade de raize(s) que tera o polinomio:'))
    Calculo(quant)
if __name__ == "__main__":
        main()