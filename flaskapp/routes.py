from flaskapp import app
from pprint import pprint
import gateway as api
from flask import request
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/search',methods=['GET','OPTIONS'])
def search():
    name = str(request.args.get('name'))
    return api.findMappingByName(name)

@app.route('/create',methods=['POST','OPTIONS'])
def create():
    ipv4 = str(request.args.get('ipv4'))
    ipv6 = str(request.args.get('ipv6'))
    name = str(request.args.get('name'))
    return api.addMapping(ipv4, ipv6, name)

