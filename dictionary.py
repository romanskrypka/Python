# Ключ : Значение
# dictionary = {
#    "Cat": "Кошка",
#    "Bat": "Летучая мышь"
# }
# контрл + / позволяет закоментировать сразу несколько строк
#print(dictionary)

#cat = dictionary["Cat"]
#print(cat)

countries = {
   "Африка": ["Египет", "Конго", "ЮАР"],
   "Азия": ["Китай", "Таиланд", "Индонезия"]
}

africa = countries["Африка"]
#print(africa)

africa_key = "Африка"
#print(countries[africa_key])

countries["Европа"] = ["Австрия", "Испания", "Италия"]
#print(countries)
#print(countries["Европа"])

# countries[0] = "Hello"
# print(countries)

# africa.append("Эфиопия")
# print(africa)
# print(countries)
# print(len(countries["Африка"]))

name = input("Введите имя: ")
#print(name)

print("Привет", name)

