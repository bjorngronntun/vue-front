from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello world'
    
@app.route('/graph1')
def home1():
    return render_template('front1.html')

@app.route('/graph2')
def home2():
    return render_template('front2.html')

if __name__ == '__main__':
    app.run(port=5050, debug=True)
