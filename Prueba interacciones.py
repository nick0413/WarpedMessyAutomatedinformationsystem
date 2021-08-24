class pos():
  def __init__(self,tipo,pos):
    self.tipo=tipo
    self.pos=pos
    self.posxn=pos[0]
    self.posyn=pos[1]




cargapos1 = pos('positivo', [2,1])
cargapos2 = pos('positivo', [2,2])

cargapos3 = pos('positivo', [4,2])

carganeg1 = pos('negativo', [3,6])
carganeg2 = pos('negativo', [8,3])

carganet1=pos('neutro', [3,5])
carganet2 = pos('neutro', [1,5])


L=[cargapos1,cargapos2,cargapos3,carganeg1,carganeg2,carganet1,carganet2]



def cercania(L):
  q=[]



  for i in L:
    q.append(i)


  for i in q:

    k=i.posxn
    j=i.posyn


    for o in q:

      g= o.posxn
      h = o.posyn

      if abs(k-g)==1:   #uno esta encima del otro
        if abs(j-h)==0:
        #print('aaaaaaaaaaaaa',i.tipo, i.pos, o.tipo, o.pos)
        #no son neutros
            if i.tipo!='neutro' and o.tipo!='neutro':
              if i.tipo==o.tipo:

                if i.pos>o.pos:
                  print('alejo')
                  i.posxn=i.posxn+1
                  o.posxn=o.posxn-1

                if i.posxn<o.posxn:
                  print('alejo2')
                  i.posxn=i.posxn-1
                  o.posxn=o.posxn+1

                print('repeler===> vertical',i.tipo, i.posxn,i.posyn, o.tipo, o.posxn,o.posyn)


                q.remove(i)
                q.remove(o)
      if abs(j-h)==1:   #uno esta al lado
        if abs(k-g)==0:
        #print('aaaaaaaaaaaaa',i.tipo, i.pos, o.tipo, o.pos)
        #no son neutros
            if i.tipo!='neutro' and o.tipo!='neutro':
              if i.tipo==o.tipo:

                if i.pos>o.pos:
                  print('alejo')
                  i.posyn=i.posyn+1
                  o.posyn=o.posyn-1

                if i.posyn<o.posyn:
                  print('alejo2')
                  i.posyn=i.posyn-1
                  o.posyn=o.posyn+1

                print('repeler===>horizontal',i.tipo, i.posxn,i.posyn, o.tipo, o.posxn,o.posyn)


                q.remove(i)
                q.remove(o)
  return q
 

def equilibrio(l):
    equi=False
    while not equi:
        q=cercania(l)
        if q==l:
            equi=True




print('==========================',L[2].posxn,L[3].posxn)
equilibrio(L)

print('==========================',L[2].posxn,L[3].posxn)

