#!/usr/bin/env python
# coding: utf-8

# # GOREV 1

# In[25]:


x = 8
type(x)


# In[26]:


y = 3.2


# In[27]:


type(y)


# In[28]:


z = 8j +18 


# In[29]:


type(z)


# In[30]:


a = "Hello World"


# In[31]:


type(a)


# In[32]:


b = True


# In[33]:


type(b)


# In[34]:


c = 23 < 22


# In[35]:


type(c)


# In[36]:


l = [1, 2, 3, 4, "String", 3.2, False]


# In[37]:


type(l)


# ***Listelerin Ozellikleri***

# #Sıralidir
# #Kapsayicidir
# #Degistirilebilir

# In[ ]:





# In[38]:


d = {"Name": "Jake",
    "Age": [27, 56],
    "Adress": "Downtown"}


# In[39]:


type(d)


# ***Sözlüklerin Ozellikleri***

# #Degistirilebilir
# #Kapsayıcı
# #Sırasız
# #Key degerleri farklı olacak

# In[40]:


t = ("Machine Learning", "Data Science")


# In[41]:


type(t)


# ***Tuple Ozellikleri***

# #Degistirilebilir
# #Sırasız + Essiz
# #Kapsayıcı

# In[42]:


s = {"python", "ml", "ds", "python"}


# In[43]:


type(s)


# ***Setlerin Ozellikleri***

# #Degistirilebilir
# #Sirasiz + Essiz
# #Kapsayici

# # GOREV 2

# Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz,kelime kelime ayırınız

# In[44]:


text = "The goal is to turn data into information, and information into insight."


# In[45]:


text.upper().replace(" , " , " ").replace(".", " ").split()


# # GOREV 3

# Verilen liste icin asagidaki adimlari uygulayiniz

# In[ ]:


# Adım 1: Verilen listenin eleman sayısına bakınız.
# Adım 2: Sıfırıncı ve dokuzuncu indeksteki elemanları çağırınız.
# Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
# Adım 4: Sekizinci indeksteki elemanı siliniz.
# Adım 5: Yeni bir eleman ekleyiniz.
# Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.


# In[47]:


lst = ["D", "A", "T", "A", "S", "C", "I", "N", "C", "E"]


# Adım 1: Verilen listenin eleman sayısına bakınız.

# In[48]:


len(lst)


#  Adım 2: Sıfırıncı ve dokuzuncu indeksteki elemanları çağırınız.

# In[49]:


lst[0]


# In[51]:


lst[9]


#  Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.

# In[52]:


data_list = lst[0:4]


# In[53]:


data_list


# Adım 4: Sekizinci indeksteki elemanı siliniz.

# In[54]:


lst.pop(8)


# Adım 5: Yeni bir eleman ekleyiniz

# In[55]:


lst.append(101)


# In[56]:


lst


# In[57]:


## append fonksiyonu ile sadece listenin sonuna eleman eklenebilir.


# Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.

# In[58]:


lst.insert(8, "N")


# In[59]:


lst


# # GOREV 4

# Verilen sözlük yapısına aşağıdaki adımları uygulayınız.

# In[62]:


dict = {'Christian' : ["America", 18] , 
       'Daisy' : ["England", 12] ,
       'Antonio' : ["Spain", 22], 
       'Dante' : ["Italy", 25]} 


# In[63]:


# Adım 1: Key değerlerine erişiniz.
# Adım 2: Value'lara erişiniz.
# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
# Adım 5: Antonio'yu dictionary'den siliniz.


# Adım 1: Key değerlerine erisiniz.

# In[64]:


dict.keys()


# Adım 2: Value'lara erişiniz

# In[65]:


dict.values()


#  Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.

# In[66]:


dict.update({"Daisy" : ["England", 13]})


# In[67]:


dict


# In[68]:


# Bu islemi indeksleme mantigiyla da yapabiliriz


# In[70]:


dict["Daisy"][1] = 14


# In[71]:


dict


#  Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.

# In[72]:


dict.update({"Ahmet" : ["Turkey", 24]})


# In[73]:


dict


#  Adım 5: Antonio'yu dictionary'den siliniz.

# In[74]:


dict.pop("Antonio")


# In[75]:


dict


# # GOREV 5

# Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri return eden fonksiyon yazınız.

# In[76]:


## Liste elemanlarına tek tek erişmeniz gerekmektedir.
## Her bir elemanın çift veya tek olma durumunu kontrol etmekiçin % yapısını kullanırız.


# In[80]:


l = [2, 13, 18, 93, 22]


# In[93]:


def  func(list): 
    cift_list = [ ]
    tek_list = [ ]
    
    for i in list :
        if i % 2 == 0 :
            cift_list.append(i)
        else:
            tek_list.append(i)
    return cift_list, tek_list

cift, tek = func(l)


# In[94]:


cift, tek


# # GOREV 6

# In[95]:


# Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı 


# sırasını temsil ederken son üç öğrenci detıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.


# In[96]:


ogrenciler = ["Ali", "Veli", "Ayse", "Talat", "Zeynep", "Ece"]


# In[97]:


## Elemanlar da gezerken aynı zamanda indekslerde de islem yapmak istediğimiz için enumerate kullanırız. Burada i=index, x=elemanlar


# In[98]:


for i, x in enumerate(ogrenciler):
    if i < 3:
        i += 1
        print("Mühendislik Fakültesi", i, ". ögrenci: ",x)
    else:
        i -= 2
        print("Tıp Fakültesi", i, ". ögrenci: ", x)


# In[100]:


## 0. indekste Ali vardı, onu 1 arttırarak yazdıgımız icin 1. orenci Ali oldu.
## 3. indekste Talat vardı, 3'e kadar saydıgımızda else e gelindiginden 2 cıkardıgımızda 1. ogrenci Talat olmus olacak.


# # GOREV 7

# Asagıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.

# In[105]:


ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]


# Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer
# almaktadır. Zip kullanarak ders bilgilerini bastırınız.

# In[ ]:


for ders_kodu, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan) :
    print(f "Kredisi {kredi} olan {ders_kodu} kodlu dersin kontenjanı {kontenjan} kisidir.")


# # GOREV 8

# In[111]:


# Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise
# 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.


# In[123]:


def kume(set1, set2):
    
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print (set2.difference(set1))
        
kume(kume1, kume2)
kume(kume2, kume1)


# In[ ]:




