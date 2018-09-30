from flask import Flask,render_template,request
app= Flask(__name__)

@app.route('/',methods=['GET','POST'])
def main():
     return render_template('myassignment1.html')

if __name__=="__main__":
    app.run()

@app.route('/fact', methods=['GET','POST'])
def fact():
    factorial = 1
    try:
        num=int(request.form.get('inputfactorial'))
        if num<0:
            return "Sorry, factorial does not exist for negative numbers. PLease try again"
        elif num==0:
            return "The factorial of 0 is 1"
        else:
            for i in range(1,num+1):
                factorial=factorial*i
        return str(factorial)
    except:
        return "Please enter only integer values"
                 
