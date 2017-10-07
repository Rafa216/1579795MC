class Fila:
	  def __init__(self):
	    self.fila=[]
	  def obtener(self):
	    return self.fila.pop()
	  def meter(self,e):
	    self.fila.insert(0,e)
	    return len(self.fila)
	  @property
	  def longitud(self):
	    return len(self.fila)


class Grafo:
	  def __init__(self):
	    self.V = set()
	    self.E = dict()
	    self.vecinos = dict()
	  def agrega(self, v):
	    self.V.add(v)
	    if not v in self.vecinos:
	      self.vecinos(v) = set()
	  def conecta(self, v, u, peso=1):
	    self.agrega(v)
	    self.agrega(u)
	    self.E[(v, u)] = self.E[(u,v)] = peso
	    self.vecinos[v].add(u)
	    self.vecinos[u].add(v)


def B_F_S(g,ni):
		visit=[]
		f=Fila()
		f.met(ni)
		while(f.lon>0):
			na=f.obt()
			visit.append(na)
			ra=g.vecinos[na]
			for nodo in ra:
				if nodo not in visit:
					f.met(nodo)
		return visit
