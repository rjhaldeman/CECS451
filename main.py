# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
 #   print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
 #   print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from queue import PriorityQueue



file1 = open('map.txt', 'r')
map = file1.readlines()
file2 = open('distances.txt', 'r')
dist = file2.readlines()


#Node Class
class Node():
    def __init__(self, name, d):
        self.name = name
        self.d = d
        self.pointer = 1000000
        self.which = []
        self.gn = 0
        #self.hn = 0

    def __init__(self, name, d):
        self.name = name
        self.d = int(d)
        self.pointer = 1000000
        self.which = []
        self.gn = 0
        #self.hn = 0

    #def __init__(self, name):
     #   self.name = name

    def setD(self, d):
        self.d = d
    def getName(self):
        return str(self.name)
    def setName(self, d):
        self.d = d
    def addN(self, n):
        self.neighbors = n

    def findNext(self, totalD):
        which = []
        self.pointer = 999999
        for i in range(len(self.neighbors)):
            #which.append( self.neighbors[i][1] + distances.index(self.neighbors[i])[1] )
            which.append(int(self.neighbors[i][1]) + self.neighbors[i][0].d)
            if(closedNodes.__contains__(self.neighbors[i][0])):
                which[i] = -1
            else:
                which[i] = 0
        for j in range(len(self.neighbors)):
            if(which[j] != -1):
                if(which[j] < self.pointer):
                    self.pointer = j
        self.which = which
        #return self.pointer
        #you evaluate with Node.neighbors[j][0] for the closest node i think
    def getLastD(self):
        return self.which[self.pointer]
    def getF(self):
        self.fn = self.gn+ self.d

#list of all city nodes
nodes = []
distances = []
#fills nodes[] with cities and sets their distances.txt data
for i in range(len(dist)):
    l = dist[i].split('-')
    nodes.append(Node(l[0], int(l[1])))
    distances.append([l[0], int(l[1])])


#This checks to see that the user entered a valid location
names = []
for a in range(len(nodes)):
    names.append(nodes[a].name)
copynames = names

#This for loop gives neighbor lists and distances to each node.
for loop in range(len(map)):
    n = map[loop].split('-')
    nn = n[1].split(')')
    nn.pop(nn.__len__() - 1)
    test = []
    act = []
    city = Node
    for x in range(len(nn)):
        nnn = nn[x].split('(')
        test.append([nnn[0].strip(','), int(nnn[1])])
    for y in range(len(test)):
        city = nodes[names.index(test[y][0])]
        act.append([city, test[y][1]])
    nodes[loop].addN(act)





                        # in .neighbors[1][0]  the 1 is which neighbor you want to look at and the second [] is 0 for node or 1 for distance between.

#print(nodes[0].neighbors[1][0].name)
#nodes[0].findNext()
#print(nodes[0].neighbors[nodes[0].pointer][0].name)

# while prompt != 'Bucharest':
#     nodes[names.index(prompt)].findNext()
#
#     print(nodes[names.index(prompt)].neighbors[nodes[names.index(prompt)].pointer][names.index(prompt)].name)
#     nodePath.append(prompt)
#     print(prompt)
#     totalD = totalD + nodes[names.index(prompt)].getLastD()
#     prompt = nodes[names.index(prompt)].neighbors[nodes[names.index(prompt)].pointer][names.index(prompt)].name



#beginning of assignment
prompt = input("Enter the starting City: ")


#openNodes = PriorityQueue()
#openNodes.put(nodes[names.index(prompt)], nodes[names.index(prompt)].d)
nodePath = []
totalD = 0
gN = 0
#openNodes = []
#openNodes = [nodes[names.index(prompt)]]
closedNodes = []

var = 0 #temp f(n)

#temp tuple
t = ("",)

for a in range(len(nodes)):

    if names.__contains__(prompt):
       continue
    else:
        print("Invalid City")
        break



goal = nodes[1]
current = nodes[names.index(prompt)]
currentCostNext = 0
print(nodes[names.index(prompt)])
#print(int(len(openNodes)))
#print(openNodes. )
print(current.neighbors[0][0].name)
print(current.neighbors[0][1])

openNodes = [( nodes[names.index(prompt)].d, nodes[names.index(prompt)], 0)]


while len(openNodes) != 0:

    openNodes.sort(key=lambda x: x[0])
    print("line 176")
    current = openNodes[0][1]
    current.getF

    if current == goal:
        break
    for i in range(len(current.neighbors)):
        print(current.neighbors)
        print(i)
        print('line 185')
        currentCostNext = current.gn + current.neighbors[i][1]
        print(currentCostNext)
        for ii in range(len(openNodes)):        #tuple variation
            #if openNodes.__contains__(current.neighbors[i][0]):
            if current.neighbors[i][0] in openNodes[ii]:
                print(i)
                print("line 89")
                if current.neighbors[i][0].gn <= currentCostNext: #line 10
                    continue
            #elif 1:#closedNodes.__contains__(current.neighbors[i][0]):
                for k in range(len(closedNodes)):
                    if current.neighbors[i][0] in closedNodes[k]: #line
                        if current.neighbors[i][0].gn <= currentCostNext:
                            print(i)
                            print("line 165")
                            t = closedNodes[k]
                            #closedNodes.pop(current.neighbors[i][0])
                            closedNodes.remove(closedNodes[k])
                            current.neighbors[i][0].getF()
                            var = current.neighbors[i][0].fn
                            current.neighbors[i][0].gn = current.neighbors[i][0].gn + currentCostNext
                            t = (var , current.neighbors[i][0], current.neighbors[i][0].gn)
                            #openNodes.append(current.neighbors[i][0])
                            openNodes.append(t)
                            continue
            else:

                current.neighbors[i][0].getF()
                var = current.neighbors[i][0].fn
                t = (var, current.neighbors[i][0], current.neighbors[i][0].gn)
                openNodes.append(t)
                print(i)
                print("line 171")
    current.getF()
    current.gn = current.gn +currentCostNext
    var = current.fn
    t = (var, current, current.gn)
    closedNodes.append(t)

if(current != goal):
    print("ERROR")

print(closedNodes)

for plz in range(len(closedNodes)):
    print(closedNodes[plz][1].name)

#x = nodes[names.index(prompt)].findNext()
#for i in range(len(nodes[names.index(prompt)].neighbors)):
 #   print(nodes[names.index(prompt)].neighbors[i][1]) + nodes[{names.index(nodes[names.index(prompt)]).neighbors[i][0]}].d


# while prompt != 'Bucharest':
#     nodePath.append(names.index(prompt))
#     nodes[names.index(prompt)].findNext()
#     nodeP = nodeP + nodes[names.index(prompt)].neighbors[ nodes[names.index(prompt)].pointer ][1]
#     print(nodeP)
#     openNodes.pop(names.index(prompt))
#     prompt = nodes[names.index(prompt)].neighbors[nodes[names.index(prompt)].pointer][0]
