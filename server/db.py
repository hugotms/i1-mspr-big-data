from sqlalchemy import create_engine

import os
import pymysql
import pandas as pd

class MySQL:

    def __init__(self):
        user = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
        url = os.getenv('DB_URL')
        port = os.getenv('DB_PORT')
        database = os.getenv('DB_NAME')

        connection_string = "mysql+pymysql://" + user + ':' + password + '@' + url + ':' + port + '/' + database

        self.db_connection = create_engine(connection_string, pool_recycle=3600).connect()

    def get_cities(self):
        sql_query = "select * from Ville;"

        frame = pd.read_sql(sql_query, self.db_connection)

        return frame['nom'].values

    def get_data_of_city(self, city):
        sql_query = "select * from Parking p join Ville v on p.idVille=v.id where v.nom='" + city + "';"

        frame = pd.read_sql(sql_query, self.db_connection)

        return frame
    
    def modify_number_of_place(self, available_places, parking_name):
        sql_query = "update Parking set nb_places_libres=" + str(available_places) + " where idVille=" + city_id + ";"

        print("Il reste " + str(available_places) + " places sur le parking " + parking_name)

    def close(self):
        self.db_connection.close()
