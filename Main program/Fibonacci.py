# Escreva um script Python que recebe como parametro um número n inteiro positivo e imprime no console o n-ésimo valor correspondente da sequencia de Fibonacci. 
# Obs.: O problema deve ser resolvido utilizando recursão.
# fibonacci sequence = 0,1,1,2,3,5,8,13,21,34...

def fibonacci(position):
    if position <= 1:
        return position
    else:
        return fibonacci(position - 1) + fibonacci(position - 2)
n = int(input("Digite a posição para o valor Fibonacci: "))
res = fibonacci(n)
print("\033[1;033m%d" %(res))
