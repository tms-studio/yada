from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  context = {}
  
  if request.method == 'POST' and request.form.get('username', None):
    context['username'] = request.form['username']
    
  return render_template('index.html', **context)
