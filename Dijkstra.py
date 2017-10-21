from heapq import heappop, heappush
from copy import deepcopy
def flatten(R):
    while len(R) > 0:
        yield R[0]
        R = R[1]
        
class grafo:
    def __init__(self):
        self.V = set() # un conjunto
        self.E = dict() # un mapeo de pesos de aristas
        self.vecinos = dict() # un mapeo
   def agrega(self, v):
        self.V.add(v)
        if not v in self.vecinos:
            self.vecinos[v] = set()
   def conecta(self, v, u, peso=1):
        self.agrega(v)
        self.agrega(u)
        self.E[(v, u)] = self.E[(u, v)] = peso # en ambos sentidos
        self.vecinos[v].add(u)
        self.vecinos[u].add(v)
   def complemento(self):
        comp= Grafo()
        for v in self.V:
            for w in self.V:
                if v != w and (v, w) not in self.E:
                    comp.conecta(v, w, 1)
        return comp
  def shortest(self, v): # Dijkstra's algorithm
        q = [(0, v, ())] 
        visited = set()
        while len(q) > 0:
            (l, u, p) = heappop(q)
            if u not in visited:
                visited.add(u)
                dist[u] = (l,u,list(flatten(p))[::-1] + [u])
            p = (u, p)
            for n in self.vecinos[u]:
                if n not in visited:
                    el = self.E[(u,n)]
                    heappush(q, (l + el, n, p))
  def kruskal(self):
        e = deepcopy(self.E)
        arbol = Grafo()
        peso = 0
        comp = dict()
        t = sorted(e.keys(), key = lambda k: e[k], reverse=True)              nuevo = set()
        while len(t) > 0 and len(nuevo) < len(self.V):
            #print(len(t)) 
            arista = t.pop()
            w = e[arista]    
            del e[arista]
            (u,v) = arista
            c = comp.get(v, {v})
            if u not in c:
                #print('u ',u, 'v ',v ,'c ', c)
                arbol.conecta(u,v,w)
                peso += w
                nuevo = c.union(comp.get(u,{u}))
                for i in nuevo:
                    comp[i]= nuevo
        print('MST con peso', peso, ':', nuevo, '\n', arbol.E)
        return arbol

g= grafo()
g.conecta('a','b', 2)
g.conecta('b','c', 1)
g.conecta('c','d', 1)
g.conecta('d','e', 2)
g.conecta('e','f', 1)
g.conecta('a','i', 1)
g.conecta('i','c', 4)
g.conecta('d','g', 1)
g.conecta('g','e', 2)
g.conecta('g','h', 1)
g.conecta('h','f', 2)
g.conecta('i','j', 1)
g.conecta('j','k', 1)
g.conecta('k','u', 2)
g.conecta('k','l', 1)
g.conecta('u','t', 1)
g.conecta('l','m', 1)
g.conecta('m','d', 3)
g.conecta('m','n', 1)
g.conecta('n','g', 3)
g.conecta('n','o', 1)
g.conecta('o','h', 3)
g.conecta('l','p', 1)
g.conecta('p','t', 1)
g.conecta('p','q', 1)
g.conecta('q','n', 2)
g.conecta('q','s', 1)
g.conecta('t','s', 1)
g.conecta('s','r', 1)
g.conecta('r','o', 3)

print(g.shortest('f'))
