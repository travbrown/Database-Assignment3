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


def sailors_who_sailed(conn):
    # TODO: Enter the correct SQL Command
    sqlCommand = "select * from sailors"
    return execute(conn, sqlCommand)


def sailors_on_date(conn):
    # TODO: Enter the correct SQL Command
    sqlCommand = "select * from sailors"
    return execute(conn, sqlCommand)


def sailors_who_sailed_certain_color_boat(conn):
    # TODO: Enter the correct SQL Command
    sqlCommand = "select * from sailors"
    return execute(conn, sqlCommand)


def sailors_add(conn, name, age, exp):
    # TODO: Enter the correct SQL Command
    # TODO: Implement operations & views
    sqlCommand = "select * from sailors"
    return execute(conn, sqlCommand)


def views(bp):
    @bp.route("/sailors")
    def _sailors():
        with get_db() as conn:
            rows = sailors(conn)
        return render_template("table.html", name="Sailors", rows=rows)

    @bp.route("/sailors/who-sailed")
    def _sailors_who_sailed():
        with get_db() as conn:
            rows = sailors_who_sailed(conn)
        return render_template("table.html", name="Sailors who sailed", rows=rows)

    @bp.route("/sailors/who-sailed-on-date")
    def _sailors_on_date():
        with get_db() as conn:
            rows = sailors_on_date(conn)
        return render_template("table.html", name="Sailors who sailed on date", rows=rows)

    @bp.route("/sailors/who-sailed-on-boat-of-color")
    def _sailors_who_sailed_certain_color_boat():
        with get_db() as conn:
            rows = sailors_who_sailed_certain_color_boat(conn)
        return render_template("table.html", name="Sailors who sailed on boat of a certain color", rows=rows)

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
        return "Success"


