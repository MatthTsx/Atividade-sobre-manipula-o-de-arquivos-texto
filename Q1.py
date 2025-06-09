from classes1.MatricesC import MatricesC

fileName = input()

M = MatricesC()

with open(fileName) as file:
    # lines = file.readlines()
    print("A matriz de entrada é: \n")
    
    for line in file:
        M.AppendCollumn(line)
        print(line.replace("\n", ""), end="\n")
    print()


    if M.Csize == len(M.matriz):
        M.GetSimmentry()
        t = "simetrica"
        if not M.Sym:
            t = "não é " + t
        print("A matriz é quadrada e", t)
    else:
        print("A matriz não é quadrada")
    M.getModa()
    print("A moda da matriz é",M.moda)