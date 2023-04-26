from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/experience')
def exp():
	return render_template('experience.html')

if __name__ == '__main__':
	app.run(debug=True) #para no tener que reiniciar el servidor local en cada cambio hecho
