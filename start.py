import json
import inquirer

# Переменные
city_tmp = []
city = []
pizzeria_adrress = []

# Откр pizza.json и salary.json
f1 = open('pizza.json', encoding="utf8")
pizza_data = json.load(f1)

for x in range(0,28):
    city_tmp.append(pizza_data[x]["city"])
    for i in city_tmp:
        if i not in city:
            city.append(i)
city.sort()

#print(city)

print("\n\n\n\n\nДобро пожаловать!")
questions = [inquirer.List('ans', message="Выберите город", choices=city)]
answers = inquirer.prompt(questions) # И ждем ввод

# заполняем адрес пиццерий в массив
for x in range(0, 28):
    if pizza_data[x]["city"] == answers["ans"]:
        pizzeria_adrress.append(pizza_data[x]["addr"])

questions = [inquirer.List('ans', message="Выберите пиццерию", choices=pizzeria_adrress)]
answers = inquirer.prompt(questions)


for x in range(0, 28):
    if pizza_data[x]["addr"] == answers["ans"]:
        print("Выбранный адрес: " + pizza_data[x]["addr"])
        print("Заказы в прямом эфире: https://orderstatusboard.dodois.io/boards?PizzeriaId=" + pizza_data[x]["uuid"])
        print("Камера на кухне: " + pizza_data[x]["camera"])