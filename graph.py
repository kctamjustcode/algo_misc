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


