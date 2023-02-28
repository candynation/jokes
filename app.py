import json
from flask import Flask, render_template, redirect, url_for
from werkzeug.exceptions import abort

app = Flask(__name__)

    
def readFile():
    file=open("jokes.json")
    jokes=json.load(file)
    file.close()
    #print(jokes)
    return jokes

def get_joke(joke_id):
    jokes=readFile()
    joke=jokes[joke_id-1]
    print(joke);
    if joke is None:
        abort(404)
    return joke



@app.route('/')
def index():
    joke=get_joke(1)
    return render_template('index.html', joke=joke)

@app.route('/<int:joke_id>')
def joke(joke_id):
    jokes=readFile();
    if joke_id==0:
        joke_id = len(jokes);
        return redirect(url_for('joke',joke_id=joke_id));
    elif joke_id > len(jokes):
        joke_id = 1;
        return redirect(url_for('joke',joke_id=joke_id));
    joke=get_joke(joke_id)
    return render_template('index.html', joke=joke)
