
from flask import Flask, jsonify, request, make_response
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
from models.users import Users
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import jwt



app = Flask(__name__)
app.secret_key = "#StoreManagerAPIKey"

app.config['JWT_SECRET_KEY'] = '@andela256'
products=[]
sales=[]

@app.route("/auth/signup", methods=['POST'])
def save_user():
    post_data = request.get_json()
    
    name = post_data['name']
    email = post_data['email']
    password = post_data['password']
    hashed_password = generate_password_hash(password, method='sha256')
    role = post_data['role']
    new_user = Users(name, email, hashed_password, role)
    name =new_user.save_user()

    return jsonify({
        'msg':'You have successfully added {}'.format(name),
        'user': {
                "id": 1,
                "name": "name",
                "email":"email",
                "password":"password",
                "role":"role"
             },
    }), 201

@app.route("/auth/login", methods = ['POST'])
def login():

    post_data = request.get_json()
    email = post_data['email']
    password = post_data['password']
    auth = request.authorization

    if not auth or not email or not password:
        return make_response('could not verify either authentication or email password or fields are empty', 401, {'WWW-Authenticate': 'Basic realm=Login required'})
    user = Users.find_specific_item('users', 'email', email)

    if not user:
        return make_response('could not verify. User is not in the database', 401, {'WWW-Authenticate': 'Basic realm=Login required'})

    if check_password_hash(user.password, password):
        access_token = jwt.encode({'email':user.email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['JWT_SECRET_KEY'])
        return jsonify({"access_token":access_token.decode('UTF-8')})

    return make_response('could not verify. Invalid Password', 401, {'WWW-Authenticate': 'Basic realm=Login required'})

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