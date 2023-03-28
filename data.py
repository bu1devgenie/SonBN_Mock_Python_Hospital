import json
import mysql.connector
from mysql.connector import errorcode


def connect_sql(config):
    try:
        cnx = mysql.connector.connect(user=config['user'],
                                      password=config['password'],
                                      host=config['host'],
                                      database=config['database_name'])
        return cnx
    except mysql.connector.errorcode as err:
        print(err)


def create_database(cursor, db_name):
    try:
        cursor.execute("CREATE DATABASE {}".format(db_name))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))


def connect_database(cnx, db_name):
    try:
        cursor = cnx.cursor()
        cursor.execute("USE {}".format(db_name))
    except mysql.connector.Error as err:
        print("Database {} does not exist".format(db_name))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor, db_name)
            print("Create database {} successfully".format(db_name))
            cnx.database = db_name
        else:
            print(err)


def create_table(cursor, table_name, sql):
    try:
        print("Creating table {}".format(table_name))
        cursor.execute(sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Table {} is already exist".format(table_name))
        else:
            print(err)


def insert_table(cnx, table_name, attributes, values):
    try:
        sql = "INSERT INTO {} (".format(table_name)
        temp_sql = ''
        for i in range(len(attributes)):
            sql += attributes[i]
            temp_sql += "'" + str(values[i]) + "'"
            if not i == len(attributes) - 1:
                sql += ', '
                temp_sql += ', '
            else:
                sql += ') VALUES ('
                temp_sql += ')'
        sql += temp_sql
        cursor = cnx.cursor()
        cursor.execute(sql)
        cnx.commit()
        return True
    except mysql.connector.Error as err:
        print(err)
        return False


def get_all_records(cursor, table_name):
    try:
        cursor.execute("SELECT * FROM {}".format(table_name))
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(err)
        return None


def get_by_id(cursor, table_name, id):
    try:
        cursor.execute("SELECT * FROM {} WHERE id = {}".format(table_name, id))
        return cursor.fetchone()
    except mysql.connector.Error as err:
        print(err)
        return None


def update_by_id(cnx, table_name, attributes, values, id):
    try:
        sql = "UPDATE {} SET ".format(table_name)
        for i in range(len(attributes)):
            sql += "{} = '{}'".format(attributes[i], values[i])
            if not i == len(attributes) - 1:
                sql += ', '
            else:
                sql += " WHERE id = {}".format(id)

        cursor = cnx.cursor()
        cursor.execute(sql)
        cnx.commit()
        return True
    except mysql.connector.Error as err:
        print(err)
        return False


def delete_by_id(cnx, table_name, id):
    try:
        cursor = cnx.cursor()
        cursor.execute("DELETE FROM {} WHERE id = {}".format(table_name, id))
        cnx.commit()
        return True
    except mysql.connector.Error as err:
        print(err)
        return False


def search_by_name(cursor, table_name, name):
    try:
        cursor.execute("SELECT * FROM {} WHERE NAME LIKE '%{}%'".format(table_name, name))
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(err)
        return None


def get_last_n_rows(cursor, table_name, n):
    try:
        cursor.execute("SELECT * FROM {}".format(table_name))
        return cursor.fetchall()[-n::]
    except mysql.connector.Error as err:
        print(err)
        return None


def valid_foreign_key(cursor, parent_table, id):
    try:
        cursor.execute("SELECT id FROM {}".format(parent_table))
        records = cursor.fetchall()
        for r in records:
            if int(id) in r:
                return True
        return False
    except mysql.connector.Error as err:
        print(err)
        return False


def schedule_exist(cursor, name, date_from, date_to):
    try:
        cursor.execute(
            "SELECT * FROM SCHEDULE s WHERE s.name LIKE \'%{}%\' AND s.date BETWEEN \'{}\' AND \'{}\'".format(name,
                                                                                                              date_from,
                                                                                                              date_to))
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(err)
        return None


def name_exist(cursor, table_name, name):
    try:
        cursor.execute("SELECT * FROM {} WHERE NAME = \'{}\'".format(table_name, name))
        return cursor.fetchone()
    except mysql.connector.Error as err:
        print(err)
        return None


if __name__ == "_main_":
    with open('./config/config.json') as f:
        config = json.load(f)
    cnx = connect_sql(config)
    cursor = cnx.cursor()
    db_name = config['database']
    connect_database(cnx, db_name)

hospital_table = """CREATE TABLE hospital.hospital (
                id INT auto_increment NOT NULL,
                name varchar(100) NOT NULL,
                phone INT NOT NULL,
                address varchar(500) NOT NULL,
                description varchar(1000) NULL,
                CONSTRAINT hospital_pk PRIMARY KEY (id)
                )
                """
doctor_table = """CREATE TABLE hospital.doctor (
                id INT auto_increment NOT NULL,
                name varchar(100) NOT NULL,
                phone INT NOT NULL,
                email varchar(100) NOT NULL,
                address varchar(100) NOT NULL,
                hospital_id INT NOT NULL,
                CONSTRAINT doctor_pk PRIMARY KEY (id),
                CONSTRAINT doctor_FK FOREIGN KEY (hospital_id) REFERENCES hospital.hospital(id) ON UPDATE CASCADE
                )
                """

patient_table = """CREATE TABLE hospital.patient (
                id INT auto_increment NOT NULL,
                name varchar(100) NOT NULL,
                phone INT NOT NULL,
                email varchar(100) NOT NULL,
                address varchar(100) NOT NULL,
                hospital_id INT NOT NULL,
                CONSTRAINT patient_pk PRIMARY KEY (id),
                CONSTRAINT patient_FK FOREIGN KEY (hospital_id) REFERENCES hospital.hospital(id) ON UPDATE CASCADE
                )
                """

schedule_table = """CREATE TABLE hospital.schedule (
                id INT auto_increment NOT NULL,
                name varchar(100) NOT NULL,
                `date` DATE NOT NULL,
                doctor_id INT NOT NULL,
                patient_id INT NOT NULL,
                `result` varchar(100) NOT NULL,
                CONSTRAINT schedule_pk PRIMARY KEY (id),
                CONSTRAINT schedule_FK FOREIGN KEY (doctor_id) REFERENCES hospital.doctor(id) ON UPDATE CASCADE,
                CONSTRAINT schedule_FK_1 FOREIGN KEY (patient_id) REFERENCES hospital.patient(id) ON UPDATE CASCADE
                )
                """


