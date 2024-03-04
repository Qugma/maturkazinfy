def czy_mniejszy(n, s, k1, k2):
    i = k1
    j = k2
    iteracje = 0
    while i <= n and j <= n:
        
        iteracje +=1
        if s[i - 1] == s[j - 1]:
           i +=1
           j +=1 
           
        else:
            iteracje +=1
            if s[i-1] < s[j-1]:
                return True
            else:
                return False
    if j <= n:
        return True
    else:
        return False
    
s = "piweczkozimnelomza"
n = len(s)
k1= 4
k2 = 8


