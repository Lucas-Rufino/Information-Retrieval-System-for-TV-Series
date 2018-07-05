import sys

class Node:
    def __init__(self):
        self.next = {}
        self.word_marker = False

    def add_item(self, string):
        if len(string) == 0:
            self.word_marker = True
            return

        key = string[0]
        string = string[1:]

        if key in self.next:
            self.next[key].add_item(string)
        
        else:
            node = Node()
            self.next[key] = node
            node.add_item(string)

    def dfs(self, sofar = None):
        if self.next.keys() == []:
            print("MATCH:" +  sofar)
        if self.word_marker == True:
            print("MATCH:" + sofar)

            for key in self.next.keys():
                self.next[key].dfs(sofar+key)
    def search(self,string,sofar =""):
        if len(string) > 0:
            key = string[0]
            string = string[1:]
            if key in self.next:
                sofar = sofar+key
                self.next[key].search(string, sofar)
            else:
                print ("NO MATCH")
        else:
            if self.word_marker == True:
                print("MATCH: " + sofar)
            for key in self.next.keys():
                self.next[key].dfs(sofar+key)
    
def fileparse(filename):

    fd = open(filename)
    root = Node()	
    line = fd.readline().strip('\r\n') # Remove newline characters \r\n


    while line !='':
        root.add_item(line)
        line = fd.readline().strip('\r\n')

    return root



# if __name__ == '__main__':
        
#     root  = fileparse("dic.txt")

#     print ("Input:")
#     input=input()
#     root.search(input)
x = Node()
fd = open("dic.txt")
line = fd.readlines() # Remove newline characters \r\n
for item in line:
    x.add_item(item.replace("\n",""))
x.search("su")

    