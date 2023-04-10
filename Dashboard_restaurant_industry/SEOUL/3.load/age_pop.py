# PostgreSQL에 정제된 데이터 적재

import pandas as pd
import psycopg2
from psycopg2 import extras
import config
from age_pop import age_rename



def get_age_pop():
    """
    정제된 데이터를 불러오는 함수
    """
    
    return age_rename()


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
    cur.execute("""CREATE TABLE IF NOT EXISTS age_pop(
                    area_name VARCHAR(50), 
                    population VARCHAR(50), 
                    age VARCHAR(50), 
                    under10 VARCHAR(50), 
                    age10 VARCHAR(50), 
                    age20 VARCHAR(50), 
                    age30 VARCHAR(50), 
                    age40 VARCHAR(50), 
                    age50 VARCHAR(50), 
                    age60 VARCHAR(50), 
                    age70 VARCHAR(50), 
                    age80 VARCHAR(50), 
                    age90 VARCHAR(50), 
                    upper100 VARCHAR(50), 
                    population_man VARCHAR(50), 
                    age_man VARCHAR(50), 
                    under10_man VARCHAR(50), 
                    age10_man VARCHAR(50), 
                    age20_man VARCHAR(50), 
                    age30_man VARCHAR(50), 
                    age40_man VARCHAR(50), 
                    age50_man VARCHAR(50), 
                    age60_man VARCHAR(50), 
                    age70_man VARCHAR(50), 
                    age80_man VARCHAR(50), 
                    age90_man VARCHAR(50), 
                    upper100_man VARCHAR(50), 
                    population_woman VARCHAR(50), 
                    age_woman VARCHAR(50), 
                    under10_woman VARCHAR(50), 
                    age10_woman VARCHAR(50), 
                    age20_woman VARCHAR(50), 
                    age30_woman VARCHAR(50), 
                    age40_woman VARCHAR(50), 
                    age50_woman VARCHAR(50), 
                    age60_woman VARCHAR(50), 
                    age70_woman VARCHAR(50), 
                    age80_woman VARCHAR(50), 
                    age90_woman VARCHAR(50), 
                    upper100_woman VARCHAR(50)
                    );""")

    # insert query
    query = f'INSERT INTO age_pop({columns}) \
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

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
