mylist = ["a", "b", "c"]
print(mylist)

# mylist = mylist + "f"
# Olmayacak çünkü f değeri bir string. Köşeli parantez
# kullanarak listeye ekleme yapılabilir.

mylist = mylist + ["f"]
print(mylist)

mylist.append("g") # append metodu listeye eleman eklemek için kullanılır.
# Append metodu kullanırken geri atama yapmaya gerek yoktur.    
print(mylist)

print(mylist.pop()) # pop metodu listenin son elemanını siler. içinde sildiği elemanı tutar.
print(mylist)

mylist.pop(1) # pop metodu içine index değeri alabilir. Bu durumda o index değerindeki elemanı siler.
print(mylist)

numbers = [1, 2, 3, 4, 5, 123, 12341, 1]
numbers.sort() # sort metodu listeyi küçükten büyüğe sıralar. listenin üstüne sıralanmış halini atar.
print(numbers)

numbers.reverse() # reverse metodu listeyi ters çevirir. listenin üstüne ters çevrilmiş halini atar.
print(numbers)

print(set(numbers)) # set metodu listeyi küme yapar. Küme yaparken aynı elemanları birleştirir. Üstüne yazmaz.
