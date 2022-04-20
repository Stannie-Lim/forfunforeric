from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def root():
  return 'hi this is working'

app.run(debug = True)
