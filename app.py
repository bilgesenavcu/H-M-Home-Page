
from flask import Flask, redirect, render_template,send_from_directory, request

app = Flask(__name__)
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/images/<path:filename>')
def get_image(filename):
    return send_from_directory('images',filename)


if __name__ == '__main__':
   
   app.run(debug=True)