print("Sequencia de Fibonacci")
n = int(input("Qual N-ésimo valor correspondente da sequencia deseja visualizar?: "))
x = 0
y = 1
cont = 2

if n == 1:
    print("{}".format(x), end="")

if n == 2:
    print("{}".format(y), end="")


if cont <= n:
    while cont <= n:
        z = x + y
        cont += 1
        x = y
        y = z

    else:
        print("{}".format(z), end="")
