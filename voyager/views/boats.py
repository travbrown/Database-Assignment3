from collections import namedtuple

from flask import render_template
from flask import request
from flask import escape

from voyager.db import get_db, execute


def boats(conn):
    sqlCommand = "SELECT b.bid, b.name, b.color FROM Boats AS b"
    return execute(conn, sqlCommand)


def boats_by_popularity(conn):
    # TODO: Enter the correct SQL Command
    sqlCommand = "select * from boats"
    return execute(conn, sqlCommand)


def boats_sailed_by(conn):
    # TODO: Enter the correct SQL Command
    sqlCommand = "select * from boats"
    return execute(conn, sqlCommand)


def views(bp):
    @bp.route("/boats")
    def _boats():
        with get_db() as conn:
            rows = boats(conn)
        return render_template("table.html", name="boats", rows=rows)

    @bp.route("/boats/by-popularity")
    def _boats_by_popularity():
        with get_db() as conn:
            rows = boats_by_popularity(conn)
        return render_template("table.html", name="Boats by Popularity", rows=rows)

    @bp.route("/boats/sailed-by")
    def _boats_sailed_by():
        with get_db() as conn:
            rows = boats_sailed_by(conn)
        return render_template(
            "table.html",
            name="Boats Sailed By",
            rows=rows)