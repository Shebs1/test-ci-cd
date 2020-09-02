from flask import Flask
from flask import request
import math
import time
import datetime

app = Flask(__name__)

#@app.route('/')
#def index():
#    return str(datetime.datetime.now())
# curl -X POST -H "Content-Type: application/json; charset=UTF-8" --data '{"a":"5","b":"2","oper":"/"}' "http://0.0.0.0:5000/api/v0.1/add"
@app.route('/api/v0.1/add', methods = ["POST"])
def add():
    if request.is_json:
        a = request.json.get('a')
        b = request.json.get('b')
        oper = request.json.get('oper')
        return calc(a,b,oper)
    else:
         return "no json"
def calc(a, b, oper):
    if oper == '+':
        return str(float(a)+float(b))
    if oper == '-':
        return str(float(a)-float(b))
    if oper == '*':
        return str(float(a)*float(b))
    if oper == '/':
        if b==0:
            return "Infinity"
        return str(float(a)/float(b))
print(calc(5,7,"+"))


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)