import os
import sys
from flask import Flask, jsonify, request
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
from models.users import Users

app = Flask(__name__)
app.secret_key = "#StoreManagerAPIKey"

app.config['JWT_SECRET_KEY'] = '@andela256'
jwt = JWTManager(app)

#creating a list of dictionaries for all product details
products = [
{}
]

#creating a list of dictionaries for all sales records

sales = [
    {}
]
@app.route("/auth/signup", methods=['POST'])
def signup():
    post_data = request.get_json
    email = post_data.get('email')
    name = post_data.get('name')
    password = post_data.get('password')
    role = post_data.get('role')
    new_user = Users(name, email, password, role)
    name =new_user.signup()

    return jsonify({
        'msg':'You have successfully added {}'.format(name)
    }), 201

@app.route("/auth/login", methods = ['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    if not email:
        return jsonify({"msg":"Email can not be empty"}), 400
    if not password:
        return jsonify({"msg":"Password can not be empty"}), 400

    if email != 'ezramahlon@gmail.com' or password !='admin123':
        return jsonify({"msg":"Invalid Email or Password"}), 400

    access_token = create_access_token(identity = email)
    return jsonify(access_token=access_token),200

@app.route("/api/v1/logout")
@jwt_required
def logout():
    pass

@app.route("/api/v1/products", methods = ['GET'])
@jwt_required
def get_products():
    return jsonify({'products' : products})


@app.route("/api/v1/products/<int:id>", methods = ['GET'])
@jwt_required
def get_single_product_details(id):
    product_details = [product for product in products if product['id'] == id]
    return jsonify({'product':product_details[0]})
    

@app.route("/api/v1/sales", methods = ['GET'])
@jwt_required
def get_sales_records():
    return jsonify({'sales' : sales})


@app.route("/api/v1/sales/<int:id>", methods = ['GET'])
@jwt_required
def get_single_sales_record(id):
    sale_record = [sale for sale in sales if sale['id'] == id]
    return jsonify({'sale':sale_record[0]})


@app.route("/api/v1/products", methods=['POST'])
@jwt_required
def add_new_product():
    if len(products)==0:
       product = {
        "id" : 1,
        "product_name" : request.json[0]['product_name'],
        "manufacture_date" : request.json[0]['manufacture_date'],
        "expiry_date" : request.json[0]['expiry_date']
        }
    elif len(products)!=0:
        product = {
        "id" : len(products) +1,
        "product_name" : request.json[0]['product_name'],
        "manufacture_date" : request.json[0]['manufacture_date'],
        "expiry_date" : request.json[0]['expiry_date']
        }
    
    products.append(product)
    return jsonify({"products": products})


@app.route("/api/v1/sales", methods=['POST'])
@jwt_required
def create_a_sale():
    sale = {
        "id" : len(sales)+1,
        "product_sold" : request.json[0]['product_sold'],
        'quantity' : request.json[0]['quantity'],
        'unit_cost' : request.json[0]['unit_cost'],
        'total_cost' :request.json[0]['total_cost'],
        'attendant' :request.json[0]['attendant']
        }
    sales.append(sale)
    return jsonify({"sales": sale})


@app.route("/api/v1/products/<int:id>", methods = ['PUT'])
@jwt_required
def update_product(id):
    my_product = [product for product in products if product['id'] == id]
    
    my_product[0]['product_name'] = request.json[0]['product_name']
    my_product[0]['manufacture_date'] = request.json[0]['manufacture_date']
    my_product[0]['expiry_date'] = request.json[0]['expiry_date']

    return jsonify({"product" : my_product[0]})


@app.route("/api/v1/products/<int:id>", methods = ['DELETE'])
@jwt_required
def delete_product(id):
    my_product = [product for product in products if product['id'] == id]
    products.remove(my_product[0])
    return jsonify({"product" : products})


if __name__ == "__main__":
    app.run(debug=True)