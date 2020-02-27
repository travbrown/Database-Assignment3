from collections import namedtuple

from flask import g
from flask import escape
from flask import render_template
from flask import request

from voyager.db import get_db, execute
from voyager.validate import validate_field, render_errors
from voyager.validate import NAME_RE, INT_RE, DATE_RE


def sailors(conn):
    return execute(conn, "SELECT s.sid, s.name,s.age,s.experience FROM Sailors AS s")


def sailors_who_sailed(conn, bname):
    sqlCommand = f"select s.name from sailors as s, boats as b, voyages as v where v.sid=s.sid and v.bid=b.bid and b.name='{bname}' group by s.name;"
    return execute(conn, sqlCommand)


def sailors_on_date(conn, date):
    sqlCommand = f"select s.name from sailors as s, voyages as v where v.sid=s.sid and date_of_voyage='{date}' group by s.name;"
    return execute(conn, sqlCommand)


def sailors_who_sailed_certain_color_boat(conn, color):
    sqlCommand = f"select s.name from sailors as s, boats as b, voyages as v where v.sid=s.sid and v.bid=b.bid and b.color='{color}' group by s.name;"
    return execute(conn, sqlCommand)


def sailors_add(conn, name, age, exp):
    sqlCommand = f"insert into sailors(name,age,experience) values('{name}',{age},{exp});"
    return execute(conn, sqlCommand)


def views(bp):
    @bp.route("/sailors")
    def _sailors():
        with get_db() as conn:
            rows = sailors(conn)
        return render_template("table.html", name="Sailors", rows=rows)

    @bp.route("/sailors/who-sailed", methods=['POST'])
    def _sailors_who_sailed():
        with get_db() as conn:
            bname = request.form['boat-name']
            rows = sailors_who_sailed(conn, bname)
        return render_template("table.html", name=f"Sailors who sailed '{bname}'", rows=rows)

    @bp.route("/sailors/who-sailed-on-date", methods=['POST'])
    def _sailors_on_date():
        with get_db() as conn:
            date = request.form['date']
            rows = sailors_on_date(conn, date)
        return render_template("table.html", name=f"Sailors who sailed on {date}", rows=rows)

    @bp.route("/sailors/who-sailed-on-boat-of-color", methods=['POST'])
    def _sailors_who_sailed_certain_color_boat():
        with get_db() as conn:
            color =  request.form['color']
            rows = sailors_who_sailed_certain_color_boat(conn, color)
        return render_template("table.html", name=f"Sailors who sailed a {color} boat", rows=rows)

    @bp.route("/sailors/add", methods=['GET'])
    def sailors_add_page():
        return render_template("addSailor.html")

    @bp.route("/sailors/add", methods=['POST'])
    def _sailors_add():
        with get_db() as conn:
            name = request.form['name']
            age = request.form['age']
            exp = request.form['exp']
            sailors_add(conn, name, age, exp)
            rows = sailors(conn)
        return render_template("table.html", name="Sailors", rows=rows)


