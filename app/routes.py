from app import app
from flask import render_template, request
from app.models import model, formopener


@app.route('/')
@app.route('/younger_index')
def index():
    return render_template('younger_index.html')


@app.route('/younger_results', methods = ['GET', 'POST'])
def results ():
    if request.method == 'GET':
        return "Please use the form <br> <a href='/younger_index'>Click here to go home!</a>"
        
    else:
        userdata = request.form
        nickname = userdata ['nickname']
        print(userdata)
        final_results, img_url = model.final_results(userdata) 
        return render_template('younger_results.html',nickname=nickname, final_results=final_results, img_src=img_url)