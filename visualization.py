import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
Terraria = pd.read_csv("Terraria.csv")
plt.figure(figsize = (10, 5))
plt.plot(Terraria['NAME'].tail(6), Terraria['DPS (SINGLE TARGET)'].tail(6), color = 'blue', marker = 'o', markersize = 7, label = 'DPS (SINGLE TARGET)'),
plt.title('Статистика урона оружий')
plt.xlabel('Названия оружий')
plt.ylabel('Урон в секунду')
plt.grid()
plt.legend()
plt.show()

# На представленной ранее линейной диаграмме, созданной с применением библиотеки Matplotlib, можно утверждать, что по оси x отображены наименования оружия, а по оси y - уровень урона в секунду. Из анализа графика следует, что самым мощным оружием является Imp Staff.

plt.figure(figsize = (15, 5))
plt.plot(Terraria['NAME'].tail(10), Terraria['DPS (MULTI TARGET)'].tail(10), color = 'green', marker = 'o', markersize = 7, label = 'DPS (MULTI TARGET)'),
plt.title('Статистика урона оружий')
plt.xlabel('Названия оружий')
plt.ylabel('Урон в секунду')
plt.grid()
plt.legend()
plt.show()

# Из представленного выше линейного графика, построенного с использованием библиотеки Matplotlib, можно заключить, что по оси x отражены названия оружия, а по оси y - уровень урона в секунду. Важно отметить, что у оружия Hornet Staff и Paper Plane отсутствует показатель DPS (MULTI TARGET), в то время как самым мощным считается оружие Flinx Staff.

plt.figure(figsize = (15, 5))
plt.plot(Terraria['NAME'].tail(10), Terraria['CLASS'].tail(10), color = 'red', marker = 'o', markersize = 7, label = 'CLASS'),
plt.title('Статистика урона оружий')
plt.xlabel('Названия оружий')
plt.ylabel('Класс персонажа')
plt.grid()
plt.legend()
plt.show()

# По данным представленного выше линейного графика, созданного с использованием библиотеки Matplotlib, можно утверждать, что по оси x представлены названия оружия, а по оси y - класс персонажа. Из вывода можно сделать вывод, что класс Summoner является наиболее активным в использовании оружия.

plt.bar(Terraria['NAME'].head(5), Terraria['DPS (SINGLE TARGET)'].head(5), color = 'pink', label = "Урон по одной цели")
plt.title('Статистика урона оружий')
plt.xlabel('Названия оружий')
plt.ylabel('Урон в секунду')
plt.legend()
plt.show()

# На представленной ранее столбчатой диаграмме, созданной с применением библиотеки Matplotlib, можно утверждать, что по оси x отображены наименования оружия, а по оси y - уровень урона в секунду. Из анализа графика следует, что самым мощным оружием является Zenith.

plt.bar(Terraria['NAME'].head(5), Terraria['DPS (MULTI TARGET)'].head(5), color = 'orange', label = "Урон по множеству целей")
plt.title('Статистика урона оружий')
plt.xlabel('Названия оружий')
plt.ylabel('Урон в секунду')
plt.legend()
plt.show()

# Из представленного выше столбчатой диаграммы, построенного с использованием библиотеки Matplotlib, можно заключить, что по оси x отражены названия оружия, а по оси y - уровень урона в секунду. Важно отметить, что самым слабым оружием является Last Prism, в то время как самым мощным считается оружие Zenith.

plt.bar(Terraria['NAME'].head(5), Terraria['DPS (SINGLE TARGET + PROYECTILE ONLY)'].head(5), color = 'purple', label = "Урон только по одиночной цели + снаряд")
plt.title('Статистика урона оружий')
plt.xlabel('Названия оружий')
plt.ylabel('Урон в секунду')
plt.legend()
plt.show()

# По данным представленного выше столбчатой диаграммы, созданного с использованием библиотеки Matplotlib, можно утверждать, что по оси x представлены названия оружия, а по оси y - урон только по одиночной уели + снаряд. Из вывода можно сделать вывод, что самым слабым по урону является Terrarian, а самым сильным Star Wrath.

plt.figure(figsize = (25, 10))
quantity = Terraria['CLASS'].value_counts()
plt.pie(quantity, labels = quantity.index, autopct = '%1.1f%%', colors = ['pink', 'green', 'red', 'purple'])
plt.title('Соотношение классов')
plt.legend()
plt.show()

# По данным представленного выше круговой диаграмме, созданного с использованием библиотеки Matplotlib, можно утверждать, что показано соотношение классов персонажей. Из вывода можно сделать вывод, что класс Summoner является менее активным в использовании, а класс Melee наоборот самым использованным.

plt.figure(figsize = (25, 10))
quantity = Terraria['GAME PROGRESSION'].value_counts()
plt.pie(quantity, labels = quantity.index, autopct = '%1.1f%%', colors = ['green', 'blue', 'yellow', 'red', 'gray', 'orange', 'violet', 'pink', 'purple', 'brown', 'beige', 'silver', 'azure', 'maroon', 'coral', 'tan'])
plt.title('Соотношение игрового прогесса')
plt.legend()
plt.show()

# По данным представленного выше круговой диаграмме, созданного с использованием библиотеки Matplotlib, можно утверждать, что показано соотношение игрового прогресса. Из вывода можно сделать вывод, что прогресс Pre-Boss является наиболее активным в получении оружия, а Post-QueenSlime менее активным в получении оружия.

plt.figure(figsize = (10, 6))
plt.scatter(Terraria['NAME'].head(7), Terraria['DPS (SINGLE TARGET)'].head(7), color = 'purple')
plt.title('Связь между название оружия и уроном в секунду')
plt.xlabel('Название оружия')
plt.ylabel('Урон в секунду')
plt.show()

# По данным представленного выше диаграммы рассеяния, созданного с использованием библиотеки Matplotlib, можно утверждать, что показано связь между оружием и их уроном в секунду. Из вывода можно сделать вывод, что самым сильным оружием является Zenith, а самым слабым является Celebration Mk.2.

plt.figure(figsize = (10, 6))
plt.scatter(Terraria['GAME PROGRESSION'].head(40), Terraria['NAME'].head(40), color = 'green')
plt.title('Связь между название оружия и игровым прогрессом')
plt.xlabel('Игровой прогресс')
plt.ylabel('Название оружия')
plt.show()

# По данным представленного выше диаграммы рассеяния, созданного с использованием библиотеки Matplotlib, можно утверждать, что показано связь между оружием и их получения в зависимоти от игрового прогресса. Из вывода можно сделать вывод, что самые получаемые оружия является Post-Plantera, а самым менее получаемым является Post-WoF.

plt.figure(figsize = (10, 6))
plt.hist(Terraria['DPS (SINGLE TARGET + PROYECTILE ONLY)'], bins = 30, color = ["pink"], edgecolor = 'orange', alpha = 0.7, label = 'Распределение урона  секунду')
plt.legend()
plt.show()

# По данным представленного выше гистограммы, созданного с использованием библиотеки Matplotlib, можно утверждать, что показано распределение урона в секунду только одиночной цели + снаряд. Из вывода можно сделать вывод, что самым большим показателм урона является от 0 до 200, а самым меньшим является от 1200 до 1400.

plt.figure(figsize = (10, 6))
plt.hist(Terraria['CLASS'], bins = 30, color = ["orange"], edgecolor = 'black', alpha = 0.7, label = 'Распределение класса персонажа')
plt.legend()
plt.show()

# По данным представленного выше гистограммы, созданного с использованием библиотеки Matplotlib, можно утверждать, что показано распределение класса персонажа. Из вывода можно сделать вывод, что самым часто использованным классом является Melee, а самым редко используемым является Summoner.