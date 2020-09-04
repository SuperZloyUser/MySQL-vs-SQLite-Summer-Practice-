from MySQL_CRUD import MySQL_CRUD
from SQLite_CRUD import SQLite_CRUD


# Функция для сбора информации и вывода в файл
def collect_report(count, dbms_name, *args):
    report = str('--- ' + dbms_name + ' ---\n' + str(count) + ') CREATE: ' + str(args[0]) +
                 '; READ: ' + str(args[1]) +
                 '; UPDATE: ' + str(args[2]) +
                 '; DELETE: ' + str(args[3])) + '\n'
    # print(report)
    file = open('out.txt', 'a')
    file.write(report)
    file.close()


# Основная функция
def main():

    # Размер итерации (количество запросов)
    count = 5000

    # Очистка старого отчёта
    file = open('out.txt', 'w')
    file.write('### REPORT ###\n\n')
    file.close()

    # Инициализация классов + подключение к локальным базам данных
    MySQL_CRUD()
    SQLite_CRUD()

    # Тестирование баз данных; 10 итераций, 5000 экземпляров каждого запроса
    for i in range(0, 10):
        print('Итерация ' + str(i + 1) + ' / 10;')

        # Тестирование MySQL
        collect_report(i + 1, "MySQL", MySQL_CRUD.Crud(count), MySQL_CRUD.cRud(count),
                       MySQL_CRUD.crUd(count), MySQL_CRUD.cruD(count))

        # Тестирование SQLite
        collect_report(i + 1, "SQLite", SQLite_CRUD.Crud(count), SQLite_CRUD.cRud(count),
                       SQLite_CRUD.crUd(count), SQLite_CRUD.cruD(count))

        # print('\n')

    my_sql_report = MySQL_CRUD.get_avg_time()
    sq_lite_report = SQLite_CRUD.get_avg_time()

    print(my_sql_report)
    print(sq_lite_report)

    file = open('out.txt', 'a')
    file.write('\n')
    file.write(my_sql_report)
    file.write(sq_lite_report)
    file.close()


if __name__ == '__main__':
    main()
