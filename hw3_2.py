def personal_fail( name, surname, birth_date, city, mail, telephone):
    list = (f" Имя - {name}, Фамилия - {surname}, Дата рождения - {birth_date}, Город проживания - {city}, Адресс электронной почты - {mail}, Телефон - {telephone}")
    return list
name = (input("Введите Имя:" ))
surname = (input("Введите Фамилию:" ))
birth_date = (input("Введите дату рождения:" ))
city = (input("Введите город проживания:" ))
mail = (input("Введите email:" ))
telephone = (input("Введите телефон:" ))

private_affair = personal_fail(name, surname, birth_date, city, mail, telephone)

print(private_affair)
