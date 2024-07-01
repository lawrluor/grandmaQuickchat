from flask import Flask, render_template, jsonify, url_for
import json

app = Flask(__name__)

def load_quickchat_data():
	with open('static/data.json', 'r') as file:
		return json.load(file)
@app.route('/')
def home():
	data = load_quickchat_data()
	return render_template('index.html', topics=data["topics"])

@app.route('/display/<text>')
def display(text):
	return render_template('display.html', text=text)

if __name__ == '__main__':
    app.run(debug=True)
