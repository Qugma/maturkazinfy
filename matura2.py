# Na podstawie dostarczonego algorytmu, zapiszę funkcję w języku Python.

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


# Sprawdzimy działanie funkcji na przykładowych danych
# Przykład:
# s = 'abacaba', k1 = 2, k2 = 5 powinno zwrócić PRAWDA, ponieważ sufiks zaczynający się od s[2] (bacaba)
# jest mniejszy w porządku alfabetycznym niż sufiks zaczynający się od s[5] (aba).

s = 'aaaaaaaaaa'
k1 = 1
k2 = 5

n = len(s)

czy_mniejszy(n, s, k1, k2)

print(czy_mniejszy(n, s, k1, k2))

