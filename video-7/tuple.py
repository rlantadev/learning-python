mylist = ["a", "b", "c"]
tup = ("a", "a", "b", "c")

print(mylist)
print(tup)

mylist[0] = "d"
print(mylist)

# tup[0] = "d" # Demetler(Tuple) değiştirilemez. Bu yüzden hata alırız.
# print(tup)

tup.count("a") # Demet içindeki a elemanının kaç tane olduğunu sayar.
print(tup.count("a"))

tup.count("d") # Demet içindeki d elemanının kaç tane olduğunu sayar.
print(tup.count("d"))

tup.index("b") # Demet içindeki b elemanının index değerini verir.
print(tup.index("b"))

tup.index("a") # Demet içindeki ilk a lmanının index değerini verir.
print(tup.index("a"))

tup.index(True) # Demet içindeki True elemanının index değerini verir. True demet içinde yoktur. Bu yüzden hata alırız.
# Countta ise yokluğun bir karşılığı vardır ve 0 döner.

