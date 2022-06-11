class Solution:
    def interpret(self, command: str) -> str:
        a=""
        i=0
        while (i<len(command)):
            if command[i]=="G":
                a+=command[i]
            elif command[i]=="(" and command[i+1]==')':
                a+="o"
                i+=1
            else:
                a+="al"
                i+=3
            i+=1
        return a