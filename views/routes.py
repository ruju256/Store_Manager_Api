from flask import Flask, jsonify, request, make_response
from models.users import Users, ValidateUserEmail
from models.products import Products
from models.categories import Categories
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

        if 'access-token' in request.headers:
            token = request.headers['access-token']
        
        if not token:
            return jsonify({"msg":"Token is missing"}), 401
        try:
            token_data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = Users.find_specific_item('users', 'email', token_data['email'])
        except:
            return jsonify({'message':'Token is invalid'}), 401
        return f(current_user, *args, **kwargs)

    return decorated

@app.route("/auth/signup", methods=['POST'])
def save_user():
    post_data = request.get_json()    
    name = post_data['name']
    email = post_data['email']
    hashed_password = generate_password_hash(post_data['password'], method='sha256')
    role = post_data['role']
    email_object = ValidateUserEmail(name, email, hashed_password, role)
    verify_email = email_object.does_email_exist(email)
    
    if not verify_email[2]:
       return jsonify({"msg_fail":"{} is already registered. Try other or Login".format(email)})
    
    new_user = Users(name, email, hashed_password, role)
    name =new_user.save_user()
    return jsonify({
        'msg':'You have successfully added {}'.format(name),
        'user': {
                "id": 1,
                "name": name,
                "email":email,
                "password":post_data['password'],
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
        access_token = jwt.encode({'email':user[2], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=90)}, app.config['SECRET_KEY'])
        return jsonify({"access_token":access_token.decode('UTF-8')})

    return make_response('could not verify. Invalid Password', 401, {'WWW-Authenticate': 'Basic realm=Login required'})


@app.route("/api/v1/products", methods = ['GET'])
@token_required
def get_products(current_user):
    if not Products.view_all_products('products'):
        return jsonify({"msg":"You have no products in store"})

    return jsonify({"prouducts":Products.product_list}), 200


@app.route("/api/v1/category", methods=['POST'])
@token_required
def add_category(current_user):
    post_data = request.get_json()

    category_name = post_data['category']
    new_category = Categories(category_name)
    category = new_category.save_category()

    return jsonify({
     'msg':'{} category successfully added'.format(category),
        'product': {"category": category_name},
    }), 201 

@app.route("/api/v1/products", methods=['POST'])
@token_required
def add_new_product(current_user):
    post_data = request.get_json()
    
    product_name = post_data['product_name']
    unit_price = post_data['unit_price']
    quantity = post_data['quantity']
    description = post_data['description']
    category = post_data['category']

    new_product = Products(product_name, unit_price, quantity, description, category)
    prod_name =new_product.save_product()
    return jsonify({
        'msg':'{} successfully added'.format(prod_name),
        'product': {
                "product_name": product_name,
                "unit_price":unit_price,
                "quantity":quantity,
                "description":description,
                "category":category
             },
    }), 201 

@app.route("/api/v1/products/<int:id>", methods = ['PUT'])
@token_required
def update_product(current_user, id):
    post_data = request.get_json()

    product_name = post_data['product_name']
    unit_price = post_data['unit_price']
    quantity = post_data['quantity']
    description = post_data['description']
    category = post_data['category']

    if not product_name or not unit_price or not quantity or not description or not category:
        return make_response('Ensure that all fields are not empty', 400)
    new_product_details = Products(product_name, unit_price, quantity, description, category)
    updated_product = new_product_details.update_a_product(id)

    if not updated_product:
        return jsonify({"msg":"Product can not be found in the database"}), 400

    return jsonify({
            'msg':'{} Details successfully Updated'.format(product_name),
            "update_product":{
                'product id': id,
                "product_name":product_name,
                "unit_price":unit_price,
                "quantity":quantity,
                "description":description,
                "category":category
            }
        })

@app.route("/api/v1/products/<int:id>", methods = ['GET'])
@token_required
def get_single_product_details(current_user, id):
    single_product = Users.find_specific_item('products','id', id)
    if not single_product:
        return jsonify({"msg":"Product does not exist"})
    return jsonify({
        'product':{
            "product_name" : single_product[1],
            "unit_price" : single_product[2],
            "quantity" : single_product[3],
            "description" : single_product[4],
            "category": single_product[5]
        }
    })
    

@app.route("/api/v1/products/<int:id>", methods = ['DELETE'])
@token_required
def delete_product(current_user, id):
   
    product = Users.find_specific_item('products','id', id)
    if not product:
        return jsonify({"msg":"Product does not exist"})
    Products.delete_product(id)

    return jsonify({
        "msg":" Product has been deleted"
        })

@app.route("/api/v1/sales", methods = ['GET'])
def get_sales_records(current_user):
    
    pass


@app.route("/api/v1/sales/<int:id>", methods = ['GET'])
def get_single_sales_record(id):
   
    pass

@app.route("/api/v1/sales", methods=['POST'])
@token_required
def save_a_sale(current_user):
    pass

    
if __name__ == "__main__":
    app.run(debug=True)