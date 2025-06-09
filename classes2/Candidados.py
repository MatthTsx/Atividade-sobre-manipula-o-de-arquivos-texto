

class Candidados:
    candsVotes = {}
    candsNames = {}
    
    def Candidados(this):
        pass
    
    def appendCand(this, code: str):
        code = code.replace("\n", "").split("-")
        number = int(code[0])
        name = code[1]
        
        this.candsNames[number] = name
        this.candsVotes[number] = 0
    
    
    def isValidVote(this, vote: str):
        vote = vote.replace(" ", "").replace("\n", "")
        
        if not vote or int(vote) not in this.candsNames.keys():
            # Do stuff
            # voto em branco
            return 0
        
        this.RegisterVote(int(vote))
        return 1
    
    def RegisterVote(this, vote: int):
        this.candsVotes[vote] += 1