import os
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.wrappers import Request, Response
from flask import Flask, render_template

app = Flask(__name__)
root_path = os.path.sep.join(app.instance_path.split(os.path.sep)[:-1])
@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/result')
def result():
    TA_name = ["Mary","Jack","Alex","Tom","Jerry"]
    TA_rate = [30,30,40,40,60]
    TA_hours = [4,5,21,12,6,10]
    
    index = 0 
    output =[]
    
    for x in TA_name:
        name = TA_name[index]
        hours = TA_hours[index]
        rate = TA_rate[index]
        
        index = index + 1
        TA_fees = name + " has received $" + str(hours * rate) +"."
         
        output.append(TA_fees)
         
    b = dict(zip(TA_name,output))
    
    return render_template('result.html', result = b)


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
        '/static': root_path+'/static',
        '/templates': root_path+'/templates'
     })
    run_simple('localhost', 5000, app)