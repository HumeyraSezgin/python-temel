#SORU 1
# listenin elemanlarını düzleştiren kod
def flatten(l):
    flatt = []
    for item in l:
        if type(item) is list: #eğer listeyse
            for item2 in item:
                flatt.append(item2) #elemanları tek tek ekle
        else:
            flatt.append(item) #değilse direkt ekle
    for i in flatt:
        if type(i) is list: #eğer hala elemanlarından biri listeyse tekrarla
            return flatten(flatt)
    return flatt

#print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))

#SORU2

# listeyi ters çeviren fonksiyon eğer içindeki eleman da liste ise onu da ters çevirir.
def reverse(l):
    for i in range(len(l)):
        if type(l[i]) is list: #içerideki eleman listeyse
            l[i]=l[i][::-1]
    return l[::-1]

#print(reverse([[1, 2], [3, 4], [5, 6, 7]]))

