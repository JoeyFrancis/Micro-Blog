from app import app

#decorators-> modifies the function that follows it
@app.route('/')
@app.route('/index')

def index():
    return "Hello, World!"