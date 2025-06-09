from enum import Enum

class Defined(Enum):
    NOT= -1

class MatricesC:
    
    modas = {}
    moda = 0
    quadradic = True
    Sym = True
    Csize = Defined.NOT
    matriz = []
    
    def MatricesC(this):
        pass
    
    def GetSimmentry(this):
        for i in range(this.Csize):
            for j in range(i, this.Csize):
                if this.matriz[i][j] != this.matriz[j][i]:
                    this.Sym = False
                    break
            if not this.Sym: break
    
    def getModa(this):
        j = list(this.modas.keys())[0]
        i = this.modas[j]
        
        for k, l in this.modas.items():
            if l > i:
                j = k
                i = l
        this.moda = j
    
    def AppendCollumn(this, line: str):
        line = list(map(int, line.split()))
        if this.Csize is Defined.NOT:
            this.Csize = len(line)
        
        for i in line:
            if i not in this.modas.keys():
                this.modas[i] = 0
            this.modas[i] += 1
        
        this.matriz.append(line)
    pass