# Store_Manager_Api
A Store Manager REST API using data structures specifically Lists and Dictionaries to store data in memory

## Application Badges
[![Coverage Status](https://coveralls.io/repos/github/ruju256/Store_Manager_Api/badge.svg?branch=develop)](https://coveralls.io/github/ruju256/Store_Manager_Api?branch=develop)
[![Build Status](https://travis-ci.org/ruju256/Store_Manager_Api.svg?branch=develop)](https://travis-ci.org/ruju256/Store_Manager_Api)
[![Maintainability](https://api.codeclimate.com/v1/badges/8a6ee1781840bded0ec9/maintainability)](https://codeclimate.com/github/ruju256/Store_Manager_Api/maintainability)
[![codecov](https://codecov.io/gh/ruju256/Store_Manager_Api/branch/develop/graph/badge.svg)](https://codecov.io/gh/ruju256/Store_Manager_Api)

## Prerequisites
In order to set up and test/use the API, this is what you will need:
* Python Envirronment : This project was built using python
* Flask Microframework: Flask is a flexible python     micro-framework that helps you build web applications.
* Pytest : Pytest is a testing framework. It helps you test all your code before you deploy it.
*Postman : A powerful HTTP client for testing web services. Basically testing the endpoints.

## Continuous Integration:
Ensuring that your code base is tested for every build. You have to have accounts for Travis CI, Codecov, Coveralls and Code climate
* A Travis CI account: Travis CI is a hosted, distributed continuous integration service used to build and test software projects hosted at GitHub.[wikipedia](https://en.wikipedia.org/wiki/Travis_CI)
* Coveralls account: Helps ypu know how much of your code or lines of code have been tested.

## Deployment
This application was deployed on [Heroku](https://www.heroku.com/). A cloud platform that can help you beta test you web apps and API endpoints.

## REST API Endpoints
These are the API endpoints that can be run on my Heroku application.
GET /products: Get All Products (https://store-manager-ruju-api-heroku.herokuapp.com/api/v1/products)

GET /products/1: Get one product with an ID of 1 (https://store-manager-ruju-api-heroku.herokuapp.com/api/v1/products/1)

GET /sales : Get all sale Records (https://store-manager-ruju-api-heroku.herokuapp.com/api/v1/sales)

GET /sales/1 :  Get one sale record with ID 1 (https://store-manager-ruju-api-heroku.herokuapp.com/api/v1/sales/1)

POST, PUT AND DELETE API REQUESTS can only be tested using POSTMAN. 