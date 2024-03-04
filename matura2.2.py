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
                return 'TAK'
            else:
                return 'NIE'
    if j <= n:
        return "TAK"
    else:
        return "NIE"
    

slowa1 = open('Z:\Python\matura\DANE\DANE_M\slowa3.txt', 'r')

read = slowa1.readlines()
pierwszy = int(read[0].strip())
drugi = read[1].strip()
sufiks1 = int(read[2].split()[0])
sufiks2 = int(read[2].split()[1])


funkcja = czy_mniejszy(pierwszy,drugi,sufiks1,sufiks2)

nazwa = "slowa3.txt "
wynik = open('Z:\Python\matura\wynik2_2.txt','a')

wynik.write(nazwa+funkcja+'\n')
