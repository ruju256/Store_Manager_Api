import os
import sys
from flask import Flask, jsonify, request


#creating a list of dictionaries for all product details
app = Flask(__name__)
app.secret_key = "#StoreManagerAPIKey"

products = [
    {
        'id' : 1,
        'product_name' : 'Bread',
        'manufacture_date' : '2018-11-02',
        'expiry_date' : '2019-01-10'
    },
    {
        'id' : 2,
        'product_name' : 'Sugar',
        'manufacture_date' : '2018-05-12',
        'expiry_date' : '2019-01-06'
    },
    {
        'id' : 3,
        'product_name' : 'Rice',
        'manufacture_date' : '2018-06-02',
        'expiry_date' : '2018-10-13'
    },
    {
        'id' : 4,
        'product_name' : 'soda',
        'manufacture_date' : '2018-03-20',
        'expiry_date' : '2019-01-01'
    }
]

#creating a list of dictionaries for all sales records

sales = [
    {
        'id' : 1,
        'product_sold' : 'Rice',
        'quantity' : '3 kgs',
        'unit_cost' : '3500',
        'total_cost' : '10500',
        'attendant' : 'john'
    },
    {
        'id' : 2,
        'product_sold' : 'Bread',
        'quantity' : '1 loaf',
        'unit_cost' : '4500',
        'total_cost' : '4500',
        'attendant' : 'john'
    },
    {
        'id' : 3,
        'product_sold' : 'soda',
        'quantity' : '2 crates',
        'unit_cost' : '23000',
        'total_cost' : '46000',
        'attendant' : 'mary'
    },
]

@app.route("/api/v1/products", methods = ['GET'])
def get_products():
    return jsonify({'products' : products})


@app.route("/api/v1/products/<int:id>", methods = ['GET'])
def get_single_product_details(id):
    product_details = [product for product in products if product['id'] == id]
    return jsonify({'product':product_details[0]})
    

@app.route("/api/v1/sales", methods = ['GET'])
def get_sales_records():
    return jsonify({'sales' : sales})


@app.route("/api/v1/sales/<int:id>", methods = ['GET'])
def get_single_sales_record(id):
    sale_record = [sale for sale in sales if sale['id'] == id]
    return jsonify({'sale':sale_record[0]})


@app.route("/api/v1/products", methods=['POST'])
def add_new_product():
    product = {
        "id" : '1',
        "product_name" : request.json[0]['product_name'],
        "manufacture_date" : request.json[0]['manufacture_date'],
        "expiry_date" : request.json[0]['expiry_date']
        }
    products.append(product)
    return jsonify({"products": products})


@app.route("/api/v1/sales", methods=['POST'])
def create_a_sale():
    sale = {
        "id" : 5,
        "product_sold" : request.json[0]['product_sold'],
        'quantity' : request.json[0]['quantity'],
        'unit_cost' : request.json[0]['unit_cost'],
        'total_cost' :request.json[0]['total_cost'],
        'attendant' :request.json[0]['attendant']
        }
    sales.append(sale)
    return jsonify({"sales": sale})


@app.route("/api/v1/products/<int:id>", methods = ['PUT'])
def update_product(id):
    my_product = [product for product in products if product['id'] == id]
    
    my_product[0]['product_name'] = request.json[0]['product_name']
    my_product[0]['manufacture_date'] = request.json[0]['manufacture_date']
    my_product[0]['expiry_date'] = request.json[0]['expiry_date']

    return jsonify({"product" : my_product[0]})


@app.route("/api/v1/products/<int:id>", methods = ['DELETE'])
def delete_product(id):
    my_product = [product for product in products if product['id'] == id]
    products.remove(my_product[0])
    return jsonify({"product" : products})


if __name__ == "__main__":
    app.run(debug=True)