from flask import Flask, render_template, request, url_for, redirect, flash
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/commonwords/', methods=['GET','POST'])
def commonwords():
    

#use the text area content as the input text
    if request.method == 'POST':
        content = request.form['content']

#construction of a dictionary of the inserted text
        dic=dict()
        words=content.split()
        for word in words:
            dic[word]=dic.get(word,0)+1
#        print(dic)

#use of tuple to reverse the order key/value in the dictionary previously created
        lst=list()
        for k,v in dic.items():
            newtup=(v,k)
            lst.append(newtup)
#        print('flipped', lst)
        lst=sorted(lst, reverse=True)

#print out of the 10 most common words with the scheme : (times used,'word')
        for v,k in lst[:10]:
            print(k,v)

        common_words = " ".join(str(x) for x in lst[:10])
        return render_template('index.html', commonwords=common_words, content=content)

if __name__ == "__main__":
    app.run(debug=True)
