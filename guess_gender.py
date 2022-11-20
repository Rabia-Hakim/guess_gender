from flask import Flask ,request
import json
import requests


app = Flask(__name__)
app.config['SECRET_KEY']='NO_SECRETS'

@app.route('/')
def Main_Page():
    person_name=request.args.get("name","")
    
    if person_name:
        result=gender(person_name)
    else:
        result=""
    return (
        """<form action="" method="get">
                Le nom est: <input type="text" name="name">
                <input type="submit" value="Verify">
            </form>"""
        + '<h2> The gender of this person is {}</h2>'.format(result))
    

def gender(name):
    
    url ="https://api.genderize.io/?name="+name
    url = requests.get(url)
    data=json.loads(url.text)
    if data['probability'] > 0.7:
        return(data['gender'])
    else:

        return "probabality is too low to guess the gender"

if __name__=='__main__':
    app.run(debug=True)

