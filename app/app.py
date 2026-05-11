from flask import Flask, render_template

app = Flask(__name__)

products = [
    {"name": "Laptop", "price": "₹50,000"},
    {"name": "Phone", "price": "₹25,000"},
    {"name": "Headphones", "price": "₹3,000"}
]

@app.after_request
def add_security_headers(response):

    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'

    return response


@app.route('/')
def home():
    return render_template("index.html", products=products)

@app.route('/health')
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

