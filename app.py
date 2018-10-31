from flask import Flask, jsonify, request, make_response
from models.users import Users
from models.products import Products
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import jwt
from functools import wraps



app = Flask(__name__)
app.config['SECRET_KEY'] = "#StoreManagerAPIKey"

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return jsonify({"msg":"Token is missing"}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = Users.find_specific_item('users', 'email', data['email'])
        except:
            return jsonify({'message':'Token is invalid'}), 401
        return f(current_user, *args, **kwargs)

    return decorated

@app.route("/home", methods=['POST'])
def home():
    return jsonify({"msg": "Welcome to home pa"})

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
                "name": name,
                "email":email,
                "password":password,
                "role":role
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

    if check_password_hash(user[3], password):
        access_token = jwt.encode({'email':user[2], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({"access_token":access_token.decode('UTF-8')})

    return make_response('could not verify. Invalid Password', 401, {'WWW-Authenticate': 'Basic realm=Login required'})

@app.route("/api/v1/logout")
def logout(current_user):
    pass

@app.route("/api/v1/products", methods = ['GET'])
def get_products(current_user):
    pass


@app.route("/api/v1/products/<int:id>", methods = ['GET'])
def get_single_product_details(current_user, id):
    # product_details = [product for product in products if product['id'] == id]
    # return jsonify({'product':product_details[0]})
    pass
    

@app.route("/api/v1/sales", methods = ['GET'])
def get_sales_records(current_user):
    # return jsonify({'sales' : sales})
    pass


@app.route("/api/v1/sales/<int:id>", methods = ['GET'])
def get_single_sales_record(id):
    # sale_record = [sale for sale in sales if sale['id'] == id]
    # return jsonify({'sale':sale_record[0]})
    pass


@app.route("/api/v1/products", methods=['POST'])
def add_new_product():
    post_data = request.get_json()
    
    product_name = post_data['product_name']
    manufacture_date = post_data['manufacture_date']
    expiry_date = post_data['expiry_date']
    quantity = post_data['quantity']
    description = post_data['description']

    new_product = Products(product_name, manufacture_date, expiry_date, quantity, description)
    prod_name =new_product.save_product()
    return jsonify({
        'msg':'{} successfully added'.format(prod_name),
        'product': {
                "product_name": product_name,
                "manufacture_date":manufacture_date,
                "expiry_date":expiry_date,
                "quantity":quantity,
                "description":description
             },
    }), 201 

@app.route("/api/v1/products/<int:id>", methods = ['PUT'])
def update_product(id):
    post_data = request.get_json()

    product_name = post_data['product_name']
    manufacture_date = post_data['manufacture_date']
    expiry_date = post_data['expiry_date']
    quantity = post_data['quantity']
    description = post_data['description']

    new_product_details = Products(product_name, manufacture_date, expiry_date, quantity, description)
    updated_product = new_product_details.update_a_product(id)

    if not updated_product:
        return jsonify({"msg":"Product can not be found in the database"}), 400

    return jsonify({
            'msg':'{} Details successfully Updated'.format(product_name),
            'product id': id
        })
    
    


@app.route("/api/v1/sales", methods=['POST'])
def save_a_sale(current_user):
    # sale = {
    #     "id" : len(sales)+1,
    #     "product_sold" : request.json[0]['product_sold'],
    #     'quantity' : request.json[0]['quantity'],
    #     'unit_cost' : request.json[0]['unit_cost'],
    #     'total_cost' :request.json[0]['total_cost'],
    #     'attendant' :request.json[0]['attendant']
    #     }
    # sales.append(sale)
    # return jsonify({"sales": sale})
    pass


@app.route("/api/v1/products/<int:id>", methods = ['DELETE'])
def delete_product(id):
    # my_product = [product for product in products if product['id'] == id]
    # products.remove(my_product[0])
    # return jsonify({"product" : products})
    pass


if __name__ == "__main__":
    app.run(debug=True)