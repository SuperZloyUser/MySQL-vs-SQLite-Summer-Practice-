import pymysql
import datetime


# Класс, взаимодействующий с СУБД MySQL
class MySQL_CRUD:
    cursor = None
    connect = None

    timings = {'count': 0, 'CREATE': 0, 'READ': 0, 'UPDATE': 0, 'DELETE': 0}

    # Подключение к БД
    @classmethod
    def __init__(cls):
        try:
            cls.connect = pymysql.connect(host='127.0.0.1', port=3306,
                                          user='root', password='12345', db='mysql')
            cls.cursor = cls.connect.cursor()
            print('Successfully connected to MySQL DB!')
        except Exception as ex:
            print(ex)

        cls.cursor.execute("DROP TABLE IF EXISTS temp;")
        cls.cursor.execute(
            "CREATE TABLE temp (ID int NOT NULL AUTO_INCREMENT, value int, description char(50), PRIMARY KEY (ID));")

    # Вычисление среднего значения времени выполнения
    @classmethod
    def get_avg_time(cls):
        count = cls.timings['count'] / 4
        report = 'MySQL avg time:\nCREATE: ' + str(round(cls.timings['CREATE'] / count, 6)) + \
                 '; READ: ' + str(round(cls.timings['READ'] / count, 6)) + \
                 '; UPDATE: ' + str(round(cls.timings['UPDATE'] / count, 6)) + \
                 '; DELETE: ' + str(round(cls.timings['DELETE'] / count, 6)) + '\n'
        return report

    # Тестирование запроса CREATE
    @classmethod
    def Crud(cls, count):
        timer = datetime.datetime.now()
        for i in range(0, count):
            cls.cursor.execute("INSERT INTO temp (value, description) VALUES ("
                               + str(i * i) + ", 'test');")
        time = datetime.datetime.now() - timer
        cls.timings['CREATE'] += time.total_seconds()
        cls.timings['count'] += 1
        return time

    # Тестирование запроса READ
    @classmethod
    def cRud(cls, count):
        timer = datetime.datetime.now()
        cls.cursor.execute("SELECT * FROM temp;")
        cls.cursor.fetchall()
        time = datetime.datetime.now() - timer
        cls.timings['READ'] += time.total_seconds()
        cls.timings['count'] += 1
        return time

    # Тестирование запроса UPDATE
    @classmethod
    def crUd(cls, count):
        timer = datetime.datetime.now()
        for i in range(0, count):
            cls.cursor.execute("UPDATE temp SET description = 'new description';")
        time = datetime.datetime.now() - timer
        cls.timings['UPDATE'] += time.total_seconds()
        cls.timings['count'] += 1
        return time

    # Тестирование запроса DELETE
    @classmethod
    def cruD(cls, count):
        timer = datetime.datetime.now()
        for i in range(0, count):
            cls.cursor.execute("DELETE FROM temp WHERE ID = " + str(i + 1) + ";")
        time = datetime.datetime.now() - timer
        cls.timings['DELETE'] += time.total_seconds()
        cls.timings['count'] += 1
        return time
