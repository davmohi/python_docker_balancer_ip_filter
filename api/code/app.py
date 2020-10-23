from flask import Flask,render_template, flash, request
from wtforms import Form,TextAreaField,TextField, validators, StringField, SubmitField
import requests,json

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    query = TextAreaField('query:', validators=[validators.required()])
    def validate_query(form, field):
        try:
            json.loads(field.data)
        except: 
            raise validators.ValidationError("Invalid input syntax")
    
@app.route("/", methods=['GET', 'POST'])
def page():
    form = ReusableForm(request.form)

    print (form.errors)
    if request.method == 'POST':
        query=request.form['query']
        print (query)

    if form.validate():
        # Save the comment here.
        response = requests.get('http://worker:8080/filter/',data=json.dumps(query),headers = {'Content-type': 'application/json', 'Accept': 'text/plain'})
        data = response.json()
        flash(data.replace("\\", '').replace("\"\"", ''))
    return render_template('page.html', form=form)

@app.route('/ips/')
def getIps():
    response = requests.get('http://worker:8080/ips')
    data = response.json()
    return json.dumps(data)

@app.route('/geoip/')
def getGeoip():
    response = requests.get('http://worker:8080/geoip')
    data = response.json()
    return json.dumps(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9090)

