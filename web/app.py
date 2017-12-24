# app.py


from flask import Flask
from flask import request, render_template
from flask.ext.sqlalchemy import SQLAlchemy
#from config import BaseConfig


app = Flask(__name__)
#app.config.from_object(BaseConfig)
#db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def index():
	return "Hello, World!"

if __name__ == '__main__':
    app.run()
