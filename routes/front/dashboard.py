from flask import render_template

from app import app


@app.route("/dashboard")
def dashboard():
    # Static dashboard page; authentication has been removed.
    return render_template("page/dashboardpage.html"), 200