from app import app
from flask import render_template
from products import product_list


@app.route('/')
def homepage():
    return render_template('page/homepage.html', products=product_list)
