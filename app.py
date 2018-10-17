from flask import Flask

app = Flask(__name__)

@app.route("/api/v1/products")
def get_products():
    return "get_products"


if __name__ == "__main__":
    app.run(debug=True)