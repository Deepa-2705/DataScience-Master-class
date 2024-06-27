#Get method is sends through url which is exposed to the entire world
#Real time example of get method is google search
#post method :this method will be access from the id written inside a body and nobody can see that inside url
#Real time example of post method is gmail application

from flask import Flask ,request ,render_template, jsonify

app = Flask(__name__)

@app.route("/")   #this method will be visible very first
def Home_page():   #Whatever written in this html page render it 
    return render_template('index.html')

@app.route('/math',methods=['POST'])
def math_ops():  #If sender is sending data  using form  not by url (use post)
    if (request.method=='POST'):
        #Get the data first usinng the id 
        #Yesterday we were using get method to take the data 
        # (get is not secure  and it is by default but post is secure method :it takes data using body)
        ops= request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])

        if ops=='add':
            r=num1+num2
            result= "The sum of",str(num1),"and",str(num2),"is",str(r)


        if ops=='subtract':
            r=num1-num2
            result= "The substraction of",str(num1),"and",str(num2),"is",str(r)


        if ops=='multiply':
            r=num1*num2
            result= "The multiplication of",str(num1),"and",str(num2),"is",str(r)


        if ops=='divide':
            r=num1/num2
            result= "The division of",str(num1),"and",str(num2),"is",str(r)


        if ops=='modulo':
            r=num1%num2
            result= "The modulous of",str(num1),"and",str(num2),"is",str(r)

        return render_template('result.html',result=result)


@app.route('/postman_action',methods=['POST'])
def math_ops1():  #If sender is sending data  using form  not by url (use post)
    if (request.method=='POST'):
        #Get the data first usinng the id 
        #Yesterday we were using get method to take the data 
        # (get is not secure  and it is by default but post is secure method :it takes data using body)
        ops= request.json['operation']    
        num1=int(request.json['num1'])   #take input in form of dictionery 
        num2=int(request.json['num2'])

        if ops=='add':
            r=num1+num2
            result= "The sum of",str(num1),"and",str(num2),"is",str(r)


        if ops=='subtract':
            r=num1-num2
            result= "The substraction of",str(num1),"and",str(num2),"is",str(r)


        if ops=='multiply':
            r=num1*num2
            result= "The multiplication of",str(num1),"and",str(num2),"is",str(r)


        if ops=='divide':
            r=num1/num2
            result= "The division of",str(num1),"and",str(num2),"is",str(r)


        if ops=='modulo':
            r=num1%num2
            result= "The modulous of",str(num1),"and",str(num2),"is",str(r)

        return jsonify(result)    #Convert final result in string format

if __name__=="__main__":
    app.run(host="0.0.0.0")


#now we have to test this function from some outside application
#Famous application for api testing :POSTMAN (we will test this function on postman)
#In post man click on new workspace then http then select post method write url
#" https://yellow-lifeguard-cllvu.pwskills.app:5000/postman_action" then select body then raw then json
#then write like:  write in double quote only 
# {
#     "operation":"add",
#     "num1": 34,
#     "num2": 45
# }
# Now run this lap flask program then click on send on postman
#Giving result in dictionery format

#The beauty of api is we are communicating from this lab to postman application