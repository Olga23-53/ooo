#Спросим у пользователя год рождения А.С. Пушкина
year = int(input("Введите год рождения А.С.Пушкина:"))
# Если пользователь ввел верный год спросить у него день рождения

if year == 1799:#если год верен, то спросим день рождения
     day = int(input("Введите день рождения А.С.Пушкина(число):"))
     #проверим верно ли указано число рождения
     if day == 6:
         print("Верно")
     else:
         print("Неверный день рождения")
else:
    #если год неверный, сразу выводим сообщение
    print("Неверный год")

