from app import app
from flask import render_template
from models.order_list import orders

@app.route('/orders')
def index():
    return render_template('index.html', title = 'Home', orders = orders)

@app.route('/orders/<order_number>')
def display_order(order_number):
    name = ""
    date = ""
    author = ""
    book_title = ""
    for order in orders:
        if order.order_number == int(order_number):
            name = order.customer_name
            date = order.date
            book_title = order.book_title
            author = order.author
    return render_template('order.html', order_number = order_number, \
                            name = name, date = date, \
                            book_title = book_title, author = author)
