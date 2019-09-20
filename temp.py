print("PROGRAMA ALGORITMO DE PRIM")
print

padres = range(9)
marcados = range(9)
minimos = range(9)
sumatoria = range(9)
m = [0]*9

for i in range(9):
    m[i]=[0]*9
    padres[i] = 0
    marcados[i] = 0
    minimos[i] = 99
    sumatoria[i] = 0

m[0][2] = 1; m[0][8] = 4; m[1][8] = 1; m[2][0] = 1; m[2][3] = 3; m[2][4] = 1; m[2][8] = 5; m[3][2] = 3; m[3][4] = 4
m[4][2] = 1; m[4][3] = 4; m[4][5] = 6; m[4][6] = 7; m[5][4] = 6; m[5][6] = 4; m[6][4] = 7; m[6][5] = 4; m[6][7] = 3
m[6][8] = 2; m[7][6] = 3; m[7][8] = 7; m[8][0] = 4; m[8][1] = 1; m[8][2] = 5; m[8][6] = 2; m[8][7] = 7

x=0; marcados[0]=1; minimos[0]=0

print(padres)
print
print(marcados)
print
print(minimos)
print
print(sumatoria)
print

for i in m:
    print(i)

op = True
while op != False:
    temp=99
    for i in range(9):
        if m[x][i] != 0 and marcados[i] == 0:
            if padres[i] != 0:
                if sumatoria[i] > (sumatoria[x] + m[x][i]):
                    minimos[i] = m[x][i]
                    padres[i] = x+1
                    sumatoria[i] = sumatoria[x] + m[x][i]
            else:
                if minimos[i] > m[x][i]:
                    minimos[i] = m[x][i]
                    padres[i] = x+1
                    sumatoria[i] = minimos[i] + sumatoria[x]
            if m[x][i] < temp:
                temp = m[x][i]
                temp2 = i
    x = temp2
    marcados[temp2] = 1
    
    op = False
    for i in range(9):
        if marcados[i] == 0:
            op = True
            
'''
while op !=0:
    temp = 99
    
    for i in range(9):
        if m[x][i] != 0 and marcados[i] == 0:
            if minimos[i] > m[x][i]:
                minimos[i] = m[x][i]
                padres[i] = x+1
            if m[x][i] < temp:
                temp = m[x][i]
                temp2 = i
    x = temp2
    marcados[temp2] = 1
    
    op = 0
    for i in range(9):
        if marcados[i] == 0:
            op = 1
'''
            
for i in m:
    print(i)