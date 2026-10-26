import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
              a=np.array(a)
              b=np.array(b)
              c=[]
              if a.shape[1]==b.shape[0]:
                for i in range(0,len(a)):
                    row=[]
                    for j in range(0,len(b[0])):
                        tot=0
                        for k in range(0,len(a[0])):
                            tot+=a[i][k]*b[k][j]
                        row.append(tot)
                    c.append(row)
                return c
              return -1
