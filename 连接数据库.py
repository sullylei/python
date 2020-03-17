import cx_Oracle

db_conn=cx_Oracle.connect('root/password@localhost/newmbdb')
db_cursor=db_conn.cursor()

sql_cmd='SELECT trs_date FROM log'

db_cursor.execute(sql_cmd)


for row in  db_cursor:
    print(row)

db_cursor.close()
db_conn.close()
