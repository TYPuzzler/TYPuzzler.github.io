import win32api
from flask import Flask, render_template

app = Flask(__name__)


#Using the below, the popup message appears on the page load of index.html
#0x00001000 - This makes the popup appear over the browser window
@app.route('/')
def index():
    win32api.MessageBox(0, 'You get a new piece!', 'New Piece', 0x00001000)
    return render_template('index.html')

#Using the below, the popup message appears when the button is clicked on the webpage.
#0x00001000 - This makes the popup appear over the browser window
@app.route('/test')
def test():
    win32api.MessageBox(0, 'You have just run a python script on the button press!', 'Running a Python Script via Javascript', 0x00001000)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)