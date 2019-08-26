from flask import Flask, request
from flask_cors import CORS
from jsonreadtest import loadfile

app = Flask(__name__)
CORS(app)

@app.route('/form-example', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        name = request.form.get('name')
        website = request.form['website']
        place = request.form['place']

        loadfile(name,website,place)

        return '''<h5>Name : {}</h5>
                    <h5>Web : {}</h5>
                    <h5>Place : {}</h5>'''.format(name, website, place)

    return '''<form method="POST">
                  #Name: <input type="text" name="name"><br>
                  #Website: <input type="text" name="website"><br>
                  #Place: <input type="text" name="place"><br>
                  #<input type="submit" value="Submit"><br>
                </form>'''

@app.route('/json-example', methods=['POST'])
def json_example():
    req_data = request.get_json()

    name = req_data['name']
    website = req_data['website']
    place = req_data['place']

    loadfile(name,website,place)

    return '''<h5>Name : {}</h5>
                    <h5>Web : {}</h5>
                    <h5>Place : {}</h5>'''.format(name, website, place)

if __name__ == '__main__':
   app.run()