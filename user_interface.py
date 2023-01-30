import person as pax
import employees as empl
import room_base as room
import booking_list as book
import exeption as ex
from logg import logging

def menu():
    while True:

        num_type=input("Выберите раздел базы данных отеля 'Нежный рассвет'\n"
                      "1 - Работа с персоналом\n"
                      "2 - Работа с клиентом\n"
                      "3 - Работа с номерным фондом\n"
                      "4 - Бронирование номеров / Работа с бронированием\n"
                      "5 - Выход из программы\n")

        match num_type:
            case "1":
                logging.info('enter the menu "Personal"')
                menu_person()
            case "2":
                logging.info('enter the menu "Employees')
                menu_employee()
            case "3":
                logging.info('enter the menu "Room base')
                menu_room()
            case "4":
                logging.info('enter the menu "Booking List')
                menu_booking()
            case "5":
                logging.info('program exit')
                break
            case _:
                logging.info('Restarting the program')
                print("Вы выбрали неверное значение: уточните выбор или нажмите 5 для прекращения работы программы")


def menu_employee():
    while True:

        num_type=input("Вы находитесь в журнале учета персонала отеля 'Нежный рассвет'. Возможные действия:\n"
                    "1 - Добавить сотрудника\n"
                    "2 - Удалить сотрудника\n"
                    "3 - Скорректировать информацию по статусу работника\n"
                    "4 - Скорректировать персональную информацию по сотруднику\n"
                    "5 - Вернуться в главное меню\n")

        match num_type:
            case "1":
                logging.info('enter New Employee')
                pass
            case "2":
                logging.info('Delete Employee')
                pass
            case "3":
                logging.info('Change Employee')
                pass
            case "4":
                logging.info('Chenge Person')
                pass
            case "5":
                logging.info('exit to main menu')
                break
            case _:
                logging.info('Restarting the program')
                print("Вы выбрали неверное значение: уточните выбор или нажмите 5 для возврата в Главное меню")


def menu_person():
    while True:

        num_type=input("Вы находитесь в журнале учета персональной информации о клиентах и сотрудниках отеля 'Нежный рассвет'. Возможные действия:\n"
                    "1 - Добавить клиента или персональную информацию о сотруднике\n"
                    "2 - Удалить клиента или персональную информацию о сотруднике\n"
                    "3 - Скорректировать персональную информацию о клиенте или сотруднике\n"
                    "4 - Вернуться в главное меню\n")

        match num_type:
            case "1":
                logging.info('Enter New Person')
                pax.new_person_input()
            case "2":
                pax.delete_person()
                logging.info('Delete Person')
                pass
            case "3":
                logging.info('Change Person')
                pax.person_change_info()
            case "4":
                logging.info('exit to main menu')
                break
            case _:
                logging.info('Restarting the program')
                print("Вы выбрали неверное значение: уточните выбор или нажмите 4 для возврата в Главное меню")

def menu_room():
    while True:

        num_type=input("Вы находитесь в журнале учета номерного фонда отеля 'Нежный рассвет'. Возможные действия:\n"
                    "1 - Добавить номер в базу\n"
                    "2 - Удалить номер из базы\n"
                    "3 - Скорректировать номер в базе\n"
                    "4 - Проверить статус номера в базе\n"
                    "5 - Вывести список занятых свободных номеров по статусу\n"
                    "6 - Вернуться в главное меню\n")

        match num_type:
            case "1":
                logging.info('Enter New Room')
                pass
            case "2":
                logging.info('Delete Room')
                pass
            case "3":
                logging.info('Change Room')
                pass
            case "4":
                logging.info('Check status Room')
                pass
            case "5":
                logging.info('Choice rooms by status')
                pass
            case "6":
                logging.info('exit to main menu')
                break
            case _:
                logging.info('Restarting the program')
                print("Вы выбрали неверное значение: уточните выбор или нажмите 6 для возврата в Главное меню")

def menu_booking():
    while True:

        num_type=input("Вы находитесь в журнале бронирований отеля 'Нежный рассвет'. Возможные действия:\n"
                    "1 - Новое бронирование\n"
                    "2 - Отмена бронирования\n"
                    "3 - Изменение бронирования\n"
                    "4 - Вернуться в главное меню\n")

        match num_type:
            case "1":
                logging.info('New Booking')
                pass
            case "2":
                logging.info('cancellation of booking')
                pass
            case "3":
                logging.info('Change Booking')
                pass
            case "4":
                logging.info('exit to main menu')
                break
            case _:
                logging.info('Restarting the program')
                print("Вы выбрали неверное значение: уточните выбор или нажмите 4 для возврата в Главное меню")
