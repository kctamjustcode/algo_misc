graph_v = [[1,2,3],[2,1,4,5],[3,1,6],[4,2,7],[5,2],[6,3,8,9],[7,4],[8,6],[9,6]]
NV = len(graph_v)
graph_in = [[0]*NV for _ in range(NV)]
min_len = NV
for i in range(NV):
    min_len = min(min_len, len(graph_v[i]))
    for j in range(1,len(graph_v[i])):
        graph_in[i][graph_v[i][j]-1] = 1
#print("mininum of edges: ", min_len-1)
#graph_in = [[0,1,1,0], [1,0,1,1], [1,1,0,1], [0,1,1,0]] #minicut==2


def isequal(que, graph): #assumed to be a connected graph
    total = []
    for q in que:
        for itm in q:
            total.append(itm)
    return sorted(list(set(total))) == list(range(len(graph)))


def BFS(graph, i): #indice here starts from 0
    que = [[i]]
    ttlque = [i]
    while not isequal(que, graph):
        nls = []
        for k in que[-1]:
            for l in range(len(graph)):
                if graph[k][l] != 0 and l not in ttlque:
                    nls.append(l)
                    ttlque.append(l)
        que.append(nls)
    return que

print(BFS(graph_in, 0))

depth = [0]*len(graph_in)
visited = []
def DFST(tree, i): # tree as graph approach
    visited.append(i)
    for j in range(len(tree)):
        if tree[i][j] != 0 and j not in visited:
            depth[j] = depth[i] + 1
            DFST(tree, j)

DFST(graph_in,0)
print(depth)


directed_graph = [[0,1,1,0],[0,0,0,1],[0,0,0,1],[0,0,0,0]]

gc = [1]*len(directed_graph)
vp = [None]*len(directed_graph)
st = [0]*len(directed_graph)
nt = [0]*len(directed_graph)
t = [0]

def DFSG(dir_graph):
    for i in range(len(dir_graph)):
        if gc[i] == 1:
            DFS_VISIT(dir_graph,i)

def DFS_VISIT(dir_graph, u):
    t[0] += 1
    st[u] = t[0]
    gc[u] = 0
    for k in range(len(dir_graph[u])):
        if dir_graph[u][k] != 0 and gc[k] == 1:
            vp[k] = u
            DFS_VISIT(dir_graph,k)
    gc[u] = -1
    t[0] += 1
    nt[u] = t[0]

DFSG(directed_graph)
print(st)
print(nt)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

leaf1=TreeNode(6)
leaf2=TreeNode(7)
leaf3=TreeNode(8)
n21=TreeNode(3)
n21.left = leaf1
n22=TreeNode(4)
n23=TreeNode(5)
n23.left=leaf2
n23.right=leaf3
n11=TreeNode(1)
n11.left=n21
n11.right=n22
n12=TreeNode(2)
n12.right=n23
root=TreeNode(0)
root.left=n11
root.right=n12

paths=[]
def DFST(tree,path,par):
    if par:
        pat = [tree.val]
        if tree.left:
            DFST(tree.left, pat, False)
        if tree.right:
            DFST(tree.right, pat, False)
        if not tree.left and not tree.right:
            paths.append(pat)
    if not par and tree.left:
        if tree.val not in path:
            path.append(tree.val)
        DFST(tree.left, path, False)
    if not par and tree.right:
        if tree.val not in path:
            path.append(tree.val)
        DFST(tree.right, path, False)
    if not tree.left and not tree.right:
        if not par:
            #print('it is leaf: {tree.val}')
            #path.append(tree.val)
            paths.append(path+[tree.val])

DFST(root,[],True)
print(paths)



### connectivity of graphs

def ifconnected(A):
    elements = set()
    for edge in A:
        elements.add(edge[0])
        elements.add(edge[1])
    graphlen = len(list(elements))
    sv = sorted(list(elements))
    graph = [[0]*graphlen for _ in range(graphlen)]
    for i in range(graphlen):
        for j in range(graphlen):
            if [sv[i],sv[j]] in A or [sv[j],sv[i]] in A:
                graph[i][j] = 1
    ###
    vx = [0]
    for _ in range(1,graphlen):
        for k in range(graphlen):
            if graph[vx[-1]][k] != 0 and k not in vx:
                vx += [k]
                break
    return len(vx) == graphlen

'''
def ifpathexist(A, s, t):
    elements = set()
    for edge in A: 
        elements.add(edge[0]) #unweighted
        elements.add(edge[0]) #unweighted
    graphlen = len(list(elements))
    sv = sorted(list(elements))
    graph = [[0]*graphlen for _ in range(graphlen)]
    for i in range(graphlen):
        for j in range(graphlen):
            if [sv[i],sv[j]] in A or [sv[j],sv[i]] in A:
                graph[i][j] = 1
    return t in component(graph,s)
'''

def ifpathexist_g(graph, s, t):
    return t in component(graph,s)


A = [[1,2],[3,2],[4,5],[5,6]]
print('edges A is connected: ',ifconnected(A))
#print(ifpathexist(A,1,3))

dA = [[[0,1],4], [[1,2],8], [[2,3],7], [[2,5],4], [[2,8],2], [[3,4],9], [[3,5],14], [[4,5],10], [[5,6],2], [[6,7],1], [[6,8],6], [[7,8],7], [[7,1],11], [[7,0],8]]
dB = sorted(dA, key=lambda x: x[1])
#print(dB)


import copy

def firstlayer(graph,i): 
    if i not in list(range(len(graph))): 
        return [i]
    fl = [i]
    for k in range(len(graph)):
        if graph[i][k] != 0:
            fl += [k]
    return sorted(fl)

def proccomponent(graph,init_component):
    proc_component = copy.deepcopy(init_component)
    for j in init_component:
        proc_component += firstlayer(graph,j)
    return sorted(list(set(proc_component)))

def component(graph,i):
    comp = firstlayer(graph,i)
    while comp != proccomponent(graph,comp):
        comp = proccomponent(graph,comp)
    return comp

#G = [[0, 1, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 1, 0]]
#print(component(G,0))
#print(ifpathexist(G,2,1)) #i.e. index 2 and 3


def edgegengraph(A,Glen): 
    E = [a[0] for a in A] 
    graphlen = Glen
    graph = [[0]*graphlen for _ in range(graphlen)]
    for i in range(graphlen):
        for j in range(graphlen):
            if [i,j] in E or [j,i] in E:
                graph[i][j] = 1
    return graph

#print(edgegengraph([dA[0],dA[1]],9))

def MST_Kruskal(A): 
    elements = set()
    for edge in A:
        elements.add(edge[0][0])
        elements.add(edge[0][1])
    graphlen = len(list(elements))
    sv = sorted(list(elements))
    graph = [[0]*graphlen for _ in range(graphlen)]
    for i in range(graphlen):
        for j in range(graphlen):
            if [sv[i],sv[j]] in A or [sv[j],sv[i]] in A:
                graph[i][j] = 1
    MST = []
    vrtx = []
    for b in A:
        if not ifpathexist_g(edgegengraph(MST,graphlen), sv.index(b[0][0]), sv.index(b[0][1])):
            MST += [b]
            vrtx += [b[0][0],b[0][1]]
    assert len(list(set(vrtx))) == len(sv)
    return MST

#print(MST_Kruskal(dB))
print('length of MST by Kruskal: ', len(MST_Kruskal(dB)))


def edgestograph(A): 
    elements = set()
    for edge in A:
        elements.add(edge[0])
        elements.add(edge[1])
    graphlen = len(list(elements))
    sv = sorted(list(elements))
    graph = [[0]*graphlen for _ in range(graphlen)]
    for i in range(graphlen):
        for j in range(graphlen):
            if [sv[i],sv[j]] in A or [sv[j],sv[i]] in A:
                graph[i][j] = 1
    return graph

#A = [[1,2],[3,2],[4,5],[5,6]]
#print(edgestograph(A))

def wedgestowgraph(A): 
    elements = set()
    E = [a[0] for a in A]
    for edge in E:
        elements.add(edge[0])
        elements.add(edge[1])
    graphlen = len(list(elements))
    sv = sorted(list(elements))
    graph = [[0]*graphlen for _ in range(graphlen)]
    for i in range(graphlen):
        for j in range(graphlen):
            if [sv[i],sv[j]] in E or [sv[j],sv[i]] in E:
                try:
                    ind = E.index([sv[i],sv[j]])
                except:
                    ind = E.index([sv[j],sv[i]])
                graph[i][j] = A[ind][1]
    return graph

#GdA = wedgestowgraph(dA)
#print(GdA)


import math

GdB = [[0,10,0,5,0],[0,0,1,2,0],[0,0,0,0,4],[0,3,9,0,2],[7,0,6,0,0]]


def STP_Dijkstra(wgraph, s):
    #S = []
    vd = [math.inf]*len(wgraph)
    vp = [None]*len(wgraph)
    Q = [s]
    vd[s]=0
    #visited = []
    completed= []
    while len(Q) != 0:
        u = Q.pop(0)
        #visited += [u]
        #S += [u]
        temp = []
        for k in range(len(wgraph)):
            if wgraph[u][k] != 0:
                '''
                RELAX(u,k,wgraph)
                '''
                if vd[k] > vd[u] + wgraph[u][k]:
                    vd[k] = vd[u] + wgraph[u][k]
                    vp[k] = u
                temp.append((k,vd[k]))
                temp = sorted(temp, key=lambda x:x[1]) # critical
                indice = [temp[i][0] for i in range(len(temp)) if temp[i][0] not in completed]
                Q += indice
                #visited += indice
        completed += [u]
    return vd
        
print('shortest path values from {0}: ', STP_Dijkstra(GdB, 0))

GdC = [[0,2,0,0,4,8,5,0,0],[2,0,0,1,0,0,2,0,0],[0,0,0,0,3,0,0,0,0],[0,1,0,0,0,0,0,3,4],[4,0,3,0,0,0,0,0,0],[8,0,0,0,0,0,1,0,0],[5,2,0,0,0,1,0,0,0],[0,0,0,3,0,0,0,0,2],[0,0,0,4,0,0,0,2,0]]
print('shortest path values from {3}: ', STP_Dijkstra(GdC,2))


def ifcycle(graph,i):
    visited = [i]
    layers = [[i]]
    new_layer = [j for j in range(len(graph)) if graph[i][j] != 0]
    layers.append(new_layer)
    visited += new_layer

    new_layer = []
    for k in layers[-1]:
        new_sublayer = []
        for j in range(len(graph)):
            if graph[k][j] != 0 and j != i:
                new_sublayer += [j]
        if set(new_sublayer).intersection(set(visited)) != set():
            return True
        visited += new_sublayer
        new_layer += new_sublayer
    layers.append(new_layer)

    while layers[-1] != []:
        new_layer = []
        for k in layers[-1]:
            new_sublayer = []
            for j in range(len(graph)):
                if graph[k][j] != 0 and not (j in layers[-2]):
                    new_sublayer += [j]
            if set(new_sublayer).intersection(set(visited)) != set():
                return True
            visited += new_sublayer
            new_layer += new_sublayer
        layers.append(new_layer)
    return False

tA = [[1,2],[2,3],[3,4],[2,5],[5,7],[3,6],[6,3]]
tAG = edgestograph(tA)
print('it is not cycle on 3rd vertex: ', not ifcycle(tAG,0))
