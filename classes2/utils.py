from classes2.Candidados import Candidados
from enum import Enum

class Defined(Enum):
    NOT=-1

def Verify(c: Candidados):
    all = 0
    first = Defined.NOT
    second = Defined.NOT
    
    for i,j in c.candsVotes.items():
        all += j
        if first == Defined.NOT:
            first = (i,j)
            continue
        
        if first[1] < j:
            second = first
            first = (i,j)
            continue
        
        if second == Defined.NOT:
            second = (i,j)
            continue
        
        if second[1] < j:
            second = (i,j)
    
    if float(first[1]/all)*100 > 50:
        return print("Não haverá segundo turno. Candidato eleito:", c.candsNames[first[0]], f"({first[0]})")
    print(f"Haverá segundo turno entre os candidatos {c.candsNames[first[0]]} {(first[0])} e {c.candsNames[second[0]]} {(second[0])}")
            