dict1 = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

dict2 = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "born": "USA"
}

dict3 = {
    "name": "John",
    "age": 30,
    "location": {
        "city": "New York",
        "born": "USA"
    }
}

print(dict2["age"])
print(dict3["location"]["born"])

# Üst ve alttakiler aynı anlaa geliyor ama alttaki daha güvenli

print(dict2.get("age"))
print(dict3.get("location").get("city"))

print(dict3.keys()) # Anahtarlar
print(dict3.values()) # Anahtar Değerleri
print(dict3.items()) # Anahtarlar ve Değerler