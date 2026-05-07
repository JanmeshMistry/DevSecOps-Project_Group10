from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Phone", "price": 25000},
    {"id": 3, "name": "Headphones", "price": 3000}
]

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to AegisFlow E-Commerce Platform"
    })

@app.route('/products')
def get_products():
    return jsonify(products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)