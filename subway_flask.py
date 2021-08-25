import threading
from flask import Flask, render_template
import pymysql

app = Flask(__name__)

conn = pymysql.connect(host = "subway.ctoxzprbsanl.ap-northeast-2.rds.amazonaws.com", user = "chan", passwd = "gurcks621", db = "subway", charset='utf8')
# try:


# finally:
#     conn.close()

@app.route('/')
def index():
    # return render_template('index.html')
    curs = conn.cursor()
    curs2 = conn.cursor()

    sql = "select * from subway.seats order by TIME desc limit 1"
    sql2 = "select * from subway.person order by TIME desc limit 1"
    conn.ping(reconnect=True)
    curs.execute(sql)
    curs2.execute(sql2)

    seat = curs.fetchall()
    person = curs2.fetchall()

    conn.commit()
    return render_template('index.html', seat=seat, person=person)

@app.route('/car_2')
def index_2():
    # return render_template('index.html')
    curs = conn.cursor()
    curs2 = conn.cursor()

    sql = "select * from subway.seats order by TIME desc limit 1"
    sql2 = "select * from subway.person order by TIME desc limit 1"
    conn.ping(reconnect=True)
    curs.execute(sql)
    curs2.execute(sql2)

    seat = curs.fetchall()
    person = curs2.fetchall()

    conn.commit()
    return render_template('index_2.html', seat=seat, person=person)

if __name__ == '__main__':
    app.run(debug=True)
    threading.Timer(3, index).start()
    threading.Timer(3, index_2).start()
