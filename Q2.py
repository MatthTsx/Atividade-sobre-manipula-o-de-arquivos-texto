from classes2.Candidados import Candidados
from classes2.utils import Verify

votosFileName = input()
TSEFileName = input()
# votosFileName = "Votes.txt"
# TSEFileName = "TSE.txt"
C = Candidados()


with open(TSEFileName) as file:
    print("Candidados:\n")
    
    for i in file.readlines():
        print(i, end="")
        C.appendCand(i)
    
    print()

votes = 0
valids = 0

with open(votosFileName) as file:
    print("Votos:\n")
    
    for i in file:
        print(i.replace("\n", ""))
        votes += 1
        valids += C.isValidVote(i)
        pass
    
    print()

print("Votos registrados:", votes)
print("Votos válidos:", valids)

Verify(C)