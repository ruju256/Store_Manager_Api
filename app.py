import os
import sys
from flask import Flask, jsonify, request


app = Flask(__name__)
app.secret_key = "#StoreManagerAPIKey"



if __name__ == "__main__":
    app.run(debug=True)