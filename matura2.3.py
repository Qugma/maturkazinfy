def czy_mniejszy(n, s, k1, k2):
    i = k1
    j = k2
    iteracje = 0
    while i <= n and j <= n:
        
        if s[i - 1] == s[j - 1]:
           i +=1
           j +=1 
           
        else:
            if s[i-1] < s[j-1]:
                return True
            else:
                return False
    if j <= n:
        return True
    else:
        return False
    
s = 'mascarpone'
dlugos = len(s)
tab = [0]*dlugos
miejsce = 0

for i in range(dlugos+1):
    for j in range(dlugos):
        if i == j:
            continue
        elif czy_mniejszy(dlugos,s,i,j) == 0:
            miejsce += 1
    tab[miejsce] = i
    miejsce = 0

print(tab)


