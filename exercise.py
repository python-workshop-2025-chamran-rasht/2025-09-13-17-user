from flask import Flask, render_template

app = Flask(__name__)

app.config.from_object('default_config')
app.config.from_prefixed_env()

@app.route('/')
def index_ep():
    return render_template('index.html')
