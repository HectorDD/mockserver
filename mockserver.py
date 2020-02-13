from flask import Flask, request, jsonify, session
from mockresponder import *

app = Flask(__name__)

t=SuccessTemplate('existeUsuario',{'identificacion':'122333'},{'result':'success','status':'true'})
te=DefaultTemplate('existeUsuario',{'result':'success','status':'false'})
mockResponder=MockResponder([t],[te])

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    print(path)
    print(request.json)
    return mockResponder.executeQuery(path,request.json)

if __name__ == '__main__':
    app.run(host= '0.0.0.0',port=8034)