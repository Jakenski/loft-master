from flask.ext.api import FlaskAPI, status, exceptions
from flask import request, url_for, make_response
import datetime
import timeit


app = FlaskAPI(__name__)


@app.route("/customers/", methods=['POST', 'GET'])
def add_customer():
    if request.method == 'POST':
        print (request.get_data())
        data = request.get_json()
        with open('my_customers.csv', 'a+') as f:
            timestamp = datetime.datetime.now().strftime('%Y:%m:%d %H:%M')
            name = data['name']
            f.write('%s,%s\n' % (name, timestamp)) 
        return make_response('All good')
    else:
        with open('my_customers.csv') as f:
            return f.readlines()



@app.route("/close/<int:key>/", methods=['POST'])
def calculate_total(name):
    pass
    



app.run()

#Создать среду
#Составить план 
#Понять, что именно нужно мне знать
#Написать 
