from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Craig'}

    posts = [
        {
            'author': {'username': 'Joe'},
            'body': 'Everything Now by Arcade Fire was my album of 2017!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'I really enjoyed listening to the new Noel Gallagher album'
        },
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)
    #return render_template('index.html', user=user)
