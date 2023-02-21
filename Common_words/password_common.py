from flask import Flask, render_template, request
import random

app = Flask(__name__)

#to make appear something on browser
#@app.route("/")
#def home():
#    return "Hello World!"



@app.route('/')
def index():
    return render_template("index.html")


@app.route('/pass/', methods=['GET'])
def show_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    random_letters = random.sample(letters, 7)
    random.shuffle(random_letters)
    password = ''
    password = password.join(random_letters)
    show_password = password
    return render_template('index.html', show_password = show_password)

###

@app.route('/bla/', methods=['GET'])
def testing():
    fh=open('words.txt')
    for line in fh:
        line=line.rstrip()
        print(line)
    return ('index.html', line)

###################################

@app.route('/commonwords/', methods=['GET'])
def commonwords():
    fh=open('words.txt','r')
    dic=dict()
    for line in fh:
        line=line.rstrip()
        words=line.split()
        for word in words:
            dic[word]=dic.get(word,0)+1
#print(dic)

    lst=list()
    for k,v in dic.items():
        newtup=(v,k)
        lst.append(newtup)
#print("flipped", lst)

    lst=sorted(lst, reverse=True)
#print("sorted", lst[:10])

    for v,k in lst[:10]:
        print(k,v)

    return render_template('index.html', k, v)


if __name__ == "__main__":
    app.run(debug=True)
