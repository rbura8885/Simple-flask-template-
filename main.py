from flask import Flask
app = Flask('app')

@app.route('/')
def hello_world():
  return 'hello, World'
@app.route('/about')
def about():
  return 'this is about page '
  

app.run(host='0.0.0.0', port=8080)