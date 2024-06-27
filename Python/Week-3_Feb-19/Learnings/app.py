#Flask is a framework or its a pythonic library by which we can create API
#In our local system we can't make our API global but in this lab we can create a global API
#Our task today: There is a simple function below we have to expose this function to the outer world
#Anyone using a url can access this function from anywhere
#In this project our lab computer will be a server with the help of flask and any browser will be client

#Conclusion: We can execute our pythonic function from a url as well

from flask import Flask

app = Flask(__name__)   #Import of flask

#We have to expose a program written inside an  application running on some port number on a server 
#When we to access something on the server computer then instead of calling using function directly we 
# will use some route  because we will expose this function as url and url is not platform dependent
# (it will follow STTP protocol)
# After giving route this function will be access from any system  

@app.route("/")    #decorate this function using route
def hello_world():
    return "Hello, World!"

if __name__=="__main__":    #Run this main function and then make this system server now
    app.run(host="0.0.0.0")


#Run code :Now this system become server it has one function
#Copy the lab url and copy it in new browser "https://gray-secretary-flxtu.pwskills.app:5000"  
# write this and we will the Hello world!
#We can access this link in our mobile device as well