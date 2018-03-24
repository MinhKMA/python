import pymysql
import threading

def select():
    threading.Timer(1.0, select).start()
    conn = pymysql.connect(host='127.0.0.1',
                           user='root', passwd='minhkma',
                           db='information_schema')
    cur = conn.cursor()
    for i in range(100):
        cur.execute("SELECT (SELECT COUNT(*) FROM INNODB_CMPMEM) AS tot_user,"
                    "(SELECT COUNT(*) FROM INNODB_FT_CONFIG ) AS tot_cat,"
                    "(SELECT COUNT(*)FROM INNODB_SYS_TABLES) AS tot_course;")
    print('minhkma')
    conn.close()

select()
