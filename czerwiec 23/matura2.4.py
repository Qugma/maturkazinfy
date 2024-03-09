def czy_mniejszy(n, s, k1, k2):
    i = k1
    j = k2
    
    while i < n and j < n:

        if s[i] == s[j]:
           i +=1
           j +=1 
           
        else:

            if s[i] < s[j]:
                return True
            else:
                return False
    if j <= n:
        return True
    else:
        return False

def znajdz_najmniejszy_sufiks(s):
    n = len(s)
    najmniejszy_sufiks = 0
    for i in range(1, n):
        if czy_mniejszy(n, s, najmniejszy_sufiks, i):
            najmniejszy_sufiks = i
    return s[najmniejszy_sufiks:]

# Przygotowanie do odczytu danych wejściowych
with open('matura/DANE/DANE_M/sufiks_4.txt', 'r') as plik:
    linie = plik.readlines()

# Przetworzenie każdego słowa i znalezienie najmniejszego sufiksu
wyniki = [znajdz_najmniejszy_sufiks(linia.split()[1]) for linia in linie if linia.strip() != '']

# Zapisanie wyników do pliku wyjściowego
with open('Z:\Python\matura\wynik2_4.txt', 'w') as plik_wynikowy:
    for wynik in wyniki:
        plik_wynikowy.write(wynik + '\n')
