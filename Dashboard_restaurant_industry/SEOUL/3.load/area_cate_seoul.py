# PostgreSQL에 정제된 데이터 적재

import pandas as pd
import psycopg2
from psycopg2 import extras
import config
from area_cate_seoul import cate_rename_seoul



def get_area_cate_seoul():
    """
    정제된 데이터를 불러오는 함수
    """
    
    return cate_rename_seoul()


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
    cur.execute("""CREATE TABLE IF NOT EXISTS area_cate_seoul(
                    name VARCHAR(50), 
                    cate_1 VARCHAR(50), 
                    cate_2 VARCHAR(50), 
                    cate_3 VARCHAR(50), 
                    dong VARCHAR(50), 
                    lon VARCHAR(50), 
                    lat VARCHAR(50), 
                    cate_mix VARCHAR(50)
                    );""")

    # insert query
    query = f'INSERT INTO area_cate_seoul({columns}) \
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'

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
