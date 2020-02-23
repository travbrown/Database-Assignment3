from collections import namedtuple

from flask import render_template
from flask import request

from voyager.db import get_db, execute

def voyages(conn):
    return execute(conn, "select v.sid, v.bid, v.date_of_voyage from Voyages AS v")

def views(bp):
    @bp.route("/voyages")
    def _voyages():
        with get_db() as conn:
                rows = voyages(conn)
        return render_template("table.html", name="Voyages", rows=rows)
