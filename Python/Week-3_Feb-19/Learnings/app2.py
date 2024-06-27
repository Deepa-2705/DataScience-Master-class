#Without API we can't build and deploy any application
#Google pay never keep money it just an application which communicates with bank for any transaction
#Banks have a different platform and the gpay have a different platform
#Let the gpay have wriitten its function in java and the bank has written their code in python
#then we have create communication from python to java and vice versa
#Here comes the concept of api(Application Programming interface). 
#Whenever we are trying to do some heterogeneous application access or transaction through http or web
#then is called web API
#Whenever we search something on google it takes the request from the clients and then send it to the 
#server using API and then some algorithm fetches the response and sends it back
#We create API to communicate between 2 homogeneous and 2 heterogenous system

#Difference between API and Web API
   #We create API using tcp,smtp,http protocols 
   #We create Web API using http protocol only 

#Rest and Soap Architecture:
   #REST:Representational State transfer
   #Soap: Simple object acesss protocol

#Both are used in creating API
#Rest by default uses http protocol(function like put,get,post,delete )
   #Features of rest: simplicity, scalability, flexibility
    #It is less secure
#Soap uses Smtp and tcp /ip protocol
   #Soap transfer all messages using xml and inside that wsdl(web service description language)
    #more secure
    
    
# RESTful services,also known as RESTful APIs,are web services that follow REST architectural style.
#REST stands for Representational State Transfer, which is a set of principles for building web 
#services that use HTTP (Hypertext Transfer Protocol) as the communication protocol.

# RESTful services are based on the following principles:

#Client-server architecture:The client and server are separated,allowing them to evolve independently.

#Stateless:Each request sent to the server contain all the information needed to complete the request.
#The server does not maintain any client context between requests.

# Cacheable: Responses from the server can be cached to improve performance.
#(Suppose 1000 people visiting a site at the same time.there are various thumbnails and images on the 
#web pages which will load again and again this loads the server so we are gonna catch or store these
#thing at a particular location so we dont have to request from the server for these things
#so that they dont use lot of resouces time again and again etc )

# Uniform interface: RESTful services use a uniform interface consisting of resources, HTTP verbs
#(GET, POST, PUT, DELETE), and hypermedia links.

# Layered system: RESTful services can be composed of multiple layers, allowing for scalability,
#flexibility, and security.

#The all above is the intro lecture to API

from flask import Flask

app = Flask(__name__) 

#if we have 3  function and we have to expose all 3 function at the same time then the 
# procedure will be similar to previous one

# if we to expose all function separately then provide another url inside their decorator 
@app.route("/")    
def hello_world():
    return "Hello, World!"

@app.route("/hello1")    
def hello_world1():
    return "Hello, World1!"

@app.route("/hello2")    
def hello_world2():
    return "Hello, World2!"

#Create one own function
@app.route('/test_func')
def test():
    a=5+6
    return("This is my first function in flask {}".format(a))

if __name__=="__main__":    
    app.run(host="0.0.0.0")


# "https://gray-secretary-flxtu.pwskills.app:5000/hello1" This link will print Hello world1
# "https://gray-secretary-flxtu.pwskills.app:5000/hello2" This link will print Hello world2
# "https://gray-secretary-flxtu.pwskills.app:5000/test_func" This link is for test function

# 200 in terminal means successful
# 404 in terminal means page not found
# 503 in terminal means bad great way