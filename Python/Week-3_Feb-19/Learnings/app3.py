#Now write a function that takes an input an then return result after some operation

from flask import Flask
from flask import request   #Import so that it can request something from the url

app = Flask(__name__)

@app.route("/hello2")    
def hello_world2():
    return "Hello, World2!"

@app.route('/input_url')   #binding with url
def request_input():
    data=request.args.get('x')     #Request an url from argument and get it 
    return ("This is the input which i'm getting {}".format(data)) 

if __name__=="__main__":    
    app.run(host="0.0.0.0")

#"https://gray-secretary-flxtu.pwskills.app:5000/input_url?x=data%20science" this link will expose input_url
