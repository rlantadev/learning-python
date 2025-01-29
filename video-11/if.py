# <text> Bu bir placeholderdır. Burası daha sonra doldurulacak anlamına gelir.
# if döngüsü bazı koşulları kontrol etmek için kullanılır. Sorgulamaya göre işlem yapar.
# else döngüsü if döngüsüne bağlı olarak çalışır. if döngüsü çalışmazsa else döngüsü çalışır.
# elif döngüsü if döngüsüne bağlı olarak çalışır. if döngüsü çalışmazsa ve elif döngüsü çalışırsa else döngüsü çalışmaz.

weather = "sunny"

if weather == "sunny":
    print("Wear your sunglasses!")
elif weather == "rainy":
    print("Take your umbrella!")
elif weather == "cloudy":
    print("Wear your jacket!")
else:
    print("Weather is not rainy or sunny!")

age = 35
if age < 18:
    print("You are a minor!")
elif age >= 18:
    print("You are an adult!")
elif age >= 65:
    print("You are a senior!")
else:
    print("You are a minor, adult or senior!")

mylist = ["a", "b", "c"]
myword = "f"


if myword in mylist:
    print("It is aldready in the list!")
else:
    mylist.append(myword)
    print("It is not in the list but now it is added to the list!")
    print("New list is: {}".format(mylist))

if (myword in mylist) and (myword == mylist[0]):
    print("It is aldready in the list and it is the first element!")
elif (myword in mylist):
    print("It is already in the list but it is not the first element!")
else:
    mylist.append(myword)
    print("It is not in the list but now it is added to the list!")
    print("New list is: {}".format(mylist))

# if sorgularında isteğe bağlı parantez de kullanılabilir.
# satır düzenlerine dikkat edilmelidir, sorgulardan sonra iki nokta koyulmalıdır.
