# PostgreSQL에 정제된 데이터 적재

import pandas as pd
import psycopg2
from psycopg2 import extras
import config
from area_pop import area_rename



def get_area_pop():
    """
    정제된 데이터를 불러오는 함수
    """
    
    return area_rename()


def get_connection():
    """
    PostgreSQL의 connection을 get.
    """
    connection = psycopg2.connect(
        host=config.host,
        user=config.user,
        password=config.password,
        database=config.db
    )
    return connection


def load_on(df):
    """
    정제된 데이터를 PostgreSQL에 적재한다.
    """
    connection = get_connection()
    cur = connection.cursor()

    columns = ','.join(df.columns)

    # table creation
    cur.execute("""CREATE TABLE IF NOT EXISTS area_pop(
                    area_name VARCHAR(50), 
                    population VARCHAR(50), 
                    generation VARCHAR(50), 
                    generation_population VARCHAR(150), 
                    population_man VARCHAR(50), 
                    population_woman VARCHAR(50), 
                    rate VARCHAR(50)
                    );""")

    # insert query
    query = f'INSERT INTO area_pop({columns}) VALUES(%s,%s,%s,%s,%s,%s,%s)'

    # INSERT DATA
    try:
        # df를 insert
        print(f'Trying to load rows...')
        extras.execute_batch(cur=cur, sql=query, argslist=tuple(df.values))

        cur.close()
        connection.commit()
        print('Completed')

    except (Exception, psycopg2.Error) as e:
        raise

    finally:
        connection.close()
        print("Done!!")



if __name__ == '__main__':


    load_on(df)
