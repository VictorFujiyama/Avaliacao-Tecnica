def fibonacci(position):
    if position <= 1:
        return position
    else:
        return fibonacci(position - 1) + fibonacci(position - 2)
n = int(input("Digite a posição para o valor Fibonacci: "))
res = fibonacci(n)
print("\033[1;033m%d" %(res))