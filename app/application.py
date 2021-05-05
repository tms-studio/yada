from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  context = {}
  
  if method == 'POST' and request.form.get('username', None):
    context['username'] = request.form['username']
    
  return render_template('index.html', **context)
