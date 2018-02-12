from flask.ext.api import FlaskAPI, status, exceptions
from flask import request, response
import datetime
import LOFT*



app = FlaskAPI(__name__)

#customer = [{name: , arrived_on: LOFT.time_come, items: ['kalyan0', 'kalyan1']}, gone: LOFT.time_gone]
customers = []

def get_amount(customer_data):
    amount = LOFT.get_total(data)
    return amount 

def validate_custumer(name,time_come,customer):
    name = data.get('name')
    time_come = data.get('come')
    customer = dict.fromkeys(['name','arrived_on'],name,time_come)
    customer_dict = json.dumps(customer)
    return customer_dict

def find_customer(needed_name):
    for customer in customers.values():
        pass

@app.route('/add_customer', methods=['POST'])
def add_customer():
    data = flask.request.get_json()
    validated_customer_data = validate_customer(data)
    customers.append(validated_customer_data)
    return jsonify(status_code=200, validated_customer_data)


@app.route('/checkout_customer', methods=['POST'])
def checkout_customer():
    """The guest counts"""
    data = flask.request.get_json()
    customer_data = find_customer(data)
    amount = get_amount(customer_data)
    remove_customer(customer)
    return response({'amount': amount})




@app.route('/add_item', methods=['POST'])
def add_item():
    """Add an additional service"""
    data = flask.request.get_json()
    customer = find_customer(data)
    add_item(item, customer)
    return response({'amount': amount, 'item':item})


@app.route('/get_customer', methods=['POST'])
def get_customer():
    return costomers



    

app.run()


