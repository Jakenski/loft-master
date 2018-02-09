from flask.ext.api import FlaskAPI, status, exceptions
from flask import request, response
import datetime
#import LOFT



app = FlaskAPI(__name__)

#customer = [{name: ..., arrived_on: LOFT.time_come, items: ['kalyan0', 'kalyan1']}, gone: LOFT.time_gone]





@app.route('/add_customer', methods=['POST'])
def add_customer():
    data = request.get_json()
  
    validated_customer_data = validate_customer(data)
    customers.append(validated_customer_data)
    return response(status_code=200, data={'foo': 1, 'bar': 2))


@app.route('/checkout_customer', methods=['POST'])
def checkout_customer():
    data = request.get_json()
    customer_data = find_customer(data)
    amount = get_amount(customer_data)
    remove_customer(customer)

    return response({'amount': amount})


@app.route('/add_item', methods=['POST'])
def add_item():
    data = request.get_json()
    user = find_customer(data)
    add_item(item, customer)
    return({'amount': amount, 'item':item})


@app.route('/get_customer', methods=['GET'])
def get_customer():
    return costomers



    

app.run()

