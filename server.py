from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/<int:x>')
@app.route('/<int:x>/<int:y>')
@app.route('/<int:x>/<int:y>/<clr1>')
@app.route('/<int:x>/<int:y>/<clr1>/<clr2>')
def index(x=8,y=8,clr1="red",clr2="black"):
    return render_template('index.html',x=x,y=y,clr1=clr1,clr2=clr2)

if __name__ == '__main__':
  app.run(debug=True)
