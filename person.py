from logg import logging
# import user_interface as UI
import exeption as ex
import csv
import os
# os.rename(src,dest)

# person_db = {}

def person_id_counter():
    file = open('person_id.txt', 'r+', encoding='utf-8')
    person_id_count = file.readlines()
    next_id = int(person_id_count[-1])+1
    file.writelines(str(next_id)+'\n')
    file.close()
    return next_id

def new_person_input():
    id_person = person_id_counter()
    print(f'Новый ID: {id_person}')
    employee_true = ex.employee_true(input ("Является сотрудником 1 - да, 0 - нет: "))
    name = input ("ИМЯ: ").title()
    second_name = input ("ОТЧЕСТВО: ").title()
    last_name = input ("ФАМИЛИЯ: ").title()
    interior_phone_number = input ("Введите внутренний номер телефона: ")
    mobile_phone_number =  input ("Введите мобильный номер телефона: ")
    adress_zip_code = input ("Введите почтовый индекс: ")
    adress_city = input ("ГОРОД: ").title()
    adress_street = input ("УЛИЦА: ").title()
    adress_bld = input ("НОМЕР ДОМА: ")
    adress_apt = input ("НОМЕР КВАРТИРЫ, если есть: ")
    
    new_person = [id_person, employee_true, name, second_name, last_name, interior_phone_number, mobile_phone_number, adress_zip_code, adress_city, adress_street, adress_bld, adress_apt]
    with open('person_base.csv', 'a', newline='') as f:
        writer = csv.writer(f, delimiter = ';')
        writer.writerow(new_person)
        logging.info(f"Adding a new person to 'person_base.csv': ID {id_person}")
    print(f'Внесена запись: ID {id_person}: {new_person}\n')


def find_person():
    find_id = int(input('Введите ID для поиска: '))
    find_index = 0
    with open('person_base.csv', 'r+', newline='') as f:
        person_db = f.readlines()
        for i in range(1,len(person_db)):
            new_list = person_db[i].split(';')
            if (int(new_list[0]) == find_id):
                find_index = i
                break

    return find_index

# def int_index_find():
#     try:
#         int_index = int(find_person())
#     except:
#         print('ID не найден')
#         int_index_find()
#     return int_index

def delete_person():
    index_person_change = int(find_person())

    with open('person_base.csv', 'r', newline='') as fread:
        person_db = fread.readlines()
    
    with open('person_base.csv', 'w', newline='') as fwrite:
        for i in range(len(person_db)):
            if (i !=index_person_change):
                fwrite.writelines(person_db[i])
    print('Запись удалена из базы\n')


def person_change_info():
    index_person_change = int(find_person())

    with open('person_base.csv', 'r', newline='') as f:
        person_db = f.readlines()
    
    with open('person_base.csv', 'w', newline='') as f:
        for i in range(len(person_db)):
            if (i !=index_person_change):
                f.writelines(person_db[i])
            else:
                new_list = person_db[index_person_change].replace('\r\n','').split(';')
                id_person = new_list[0]
                employee_true = new_list[1]
                name = new_list[2]
                second_name = new_list[3]
                last_name = new_list[4]
                interior_phone_number = new_list[5]
                mobile_phone_number = new_list[6]
                adress_zip_code = new_list[7]
                adress_city = new_list[8]
                adress_street = new_list[9]
                adress_bld = new_list[10]
                adress_apt = new_list[11]

                while True:
                    num_type=input("Какие данные будем менять:\n"
                            "1 - Является сотрудником\n"
                            "2 - ФИО\n"
                            "3 - Внутренний номер телефона\n"
                            "4 - Мобильный номер телефона\n"
                            "5 - Адрес\n"
                            "6 - ЗАВЕРШИТЬ РЕДАКТИРОВАНИЕ (Возврат в главное меню)\n")
                    match num_type:
                        case "1":
                            employee_true = ex.employee_true(input ("Является сотрудником 1 - да, 0 - нет: "))
                        case "2":
                            last_name = input ("ФАМИЛИЯ: ").title()
                            name = input ("ИМЯ: ").title()
                            second_name = input ("ОТЧЕСТВО: ").title()
                        case "3":
                            interior_phone_number = input ("Введите внутренний номер телефона: ")
                        case "4":
                            mobile_phone_number =  input ("Введите мобильный номер телефона: ")
                        case "5":
                            adress_zip_code = input ("Введите почтовый индекс: ")
                            adress_city = input ("ГОРОД: ").title()
                            adress_street = input ("УЛИЦА: ").title()
                            adress_bld = input ("НОМЕР ДОМА: ")
                            adress_apt = input ("НОМЕР КВАРТИРЫ, если есть: ")
                        case "6":
                            break
                        case _:
                            print("Вы выбрали неверное значение: уточните выбор или нажмите 6 для возврата в Главное меню")

                change_person = [id_person, employee_true, name, second_name, last_name, interior_phone_number, mobile_phone_number, adress_zip_code, adress_city, adress_street, adress_bld, adress_apt]
                writer = csv.writer(f, delimiter = ';')
                writer.writerow(change_person)
                logging.info(f"Changing a person in 'person_base.csv': ID {id_person}")
    print(f'Внесены изменения в запись: ID {id_person}: {change_person}\n')
