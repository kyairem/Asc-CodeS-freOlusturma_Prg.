import random #random fonksiyonu için
sayi=int(input("Sifre kac karakterden olusacaktir?:")) #kullanıcıya kaç karekter girmesi istendiği sorulur
dizi1=[] #kullanıcının girdiği karekterleri için dizi elemanı
dizi2=[] #kullanıcının girdiği karekterleri ascıı koda çevirmek için dizi elemanı
for i in range(0,sayi): #kullanıcının girdiği sayı kadar çalışır
    karekter=input("Karekter {}:".format(i+1)) #kaç karekter girilirse kullanıcının o kadar karekter girmesi istenir
    dizi1.append(karekter) #girilen karakterler dizi1' e eklenir
print("Olusturulucak Rastgele Sifre:") #ekrana yazdırılır
for i in dizi1: #dizi1 içerisindeki tüm elemanlara işlem yapmak, dizi1 elemanı sayısı kadar çalışır
    dizi2.append(ord(i)) #dizi1 elemanlarını ascıı kodları değerlerini dizi2' ye ekler
    print(random.choice(dizi2), end="") #dizi2 elemanları içerisinde rastgele seçim yapmak için


