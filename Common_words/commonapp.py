from flask import Flask, render_template, request, url_for, redirect, flash
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

###################################
'''
#to show the test of the .txt file
@app.route('/apri/', methods=['GET'])
def request():
    fname = input("Enter file name: ")
    fh=open(fname,'r')
    return render_template("index.html", apri=fh)
'''


@app.route('/commonwords/', methods=['GET', 'POST'])
def commonwords():
    '''

    fname = input("Enter file name: ")
    try:
        fh=open(fname,'r')
    except:
        print('Wrong file name. Insert a valid file name:')
        quit()
'''

    if request.method == 'POST':
#        title = request.form['title']
        content = request.form['content']
        fh=content
        fh=list()
        fh.append({'content': content})
#        fh.append({'title': title, 'content': content})
#        return redirect(url_for('index'))

        dic=dict()
#        fh=str()
        for line in fh:
            print(line)

    return render_template('index.html' , commonwords = line)


if __name__ == "__main__":
    app.run(debug=True)
