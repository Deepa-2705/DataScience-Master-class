from flask import Flask

app = Flask(__name__)   #Import of flask

@app.route("/welcome")    #decorate this function using route
def welcome():
    return "welcome to ABC Corporation!"

@app.route("/")    #decorate this function using route
def details():
    Comapany_Name="ABC Corporation"
    Location="India"
    Contact_details="999-999-9999"
    return ("Company name : {} \n Location : {} \n Contact Details : {}".format(Comapany_Name,Location,Contact_details))

if __name__=="__main__":    #Run this main function and then make this system server now
    app.run(host="0.0.0.0")