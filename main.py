from flask import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/result", methods=['GET'])
def result():
    product = request.args.get('product')
    return render_template('result.html', text=product)

app.run(debug=True)