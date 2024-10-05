import psycopg2                                                         # import psycopg2


connection=psycopg2.connect(user='postgres',                            # connect to the database
                            password='Soumen@1234',
                            host='localhost',
                            database='postgres')

Cursor=connection.cursor()                                              # create a cursor
Cursor.execute('select * from dept')                                    # execute sql
result=Cursor.fetchall()                                                # fetch the data
print(result)

print('\n\n\n')
sql='''
        SELECT * FROM dept
        WHERE {}={};
'''.format('dept_id',1)
Cursor.execute(sql)
result=Cursor.fetchall()
print(result)

Cursor.close()