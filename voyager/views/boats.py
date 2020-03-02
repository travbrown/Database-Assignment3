from collections import namedtuple

from flask import render_template
from flask import request
from flask import escape

from voyager.db import get_db, execute

def boats(conn):
    sqlCommand = "SELECT * FROM boats as b;"
    return execute(conn, sqlCommand)

def boats_add(conn, name, color):
    sqlCommand = f"insert into boats(name, color) values('{name}', '{color}');"
    return execute(conn, sqlCommand)

def boats_by_popularity(conn):
    sqlCommand = "select b.name from voyages as v, boats as b where b.bid = v.bid group by b.name order by count(*) desc;"
    return execute(conn, sqlCommand)

def boats_sailed_by(conn,sname):
    sqlCommand = f"select b.name from boats as b, sailors as s, voyages as v where v.sid=s.sid and b.bid=v.bid and s.name='{sname}' group by b.name;"
    return execute(conn, sqlCommand)


def views(bp):
    @bp.route("/boats")
    def _boats():
        with get_db() as conn:
            rows = boats(conn)
        return render_template("table.html", name="Boats", rows=rows)

    @bp.route("/boats/by-popularity")
    def _boats_by_popularity():
        with get_db() as conn:
            rows = boats_by_popularity(conn)
        return render_template("table.html", name="Boats by Popularity", rows=rows)

    @bp.route("/boats/sailed-by", methods = ['POST'])
    def _boats_sailed_by():
        with get_db() as conn:
            sname = request.form['sailor-name']
            rows = boats_sailed_by(conn, sname)
        return render_template("table.html",name=f"Boats Sailed By {sname}",rows=rows)
    
    @bp.route("/boats/add", methods = ['GET'])
    def boats_add_page():
        return render_template("addBoat.html")

    @bp.route("/boats/add", methods = ['POST'])
    def _boats_add():
        with get_db() as conn:
            name = request.form['name']
            color = request.form['color']
            boats_add(conn, name, color)
            rows = boats(conn)
        return render_template("table.html", name="Boats", rows=rows)
