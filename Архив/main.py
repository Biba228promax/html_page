from flask import *

app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html')


@app.route("/result")
def result():
    product = request.args.execute("SELECT * FROM products").fetchall()
    cards = cursor
    for product in products:
        cards.append(make_product_card(product))
    return render_template('result.html', products=cards)

app.run(debug=True)