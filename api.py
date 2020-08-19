from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('gif-v-1-sam.html')

@app.route('/sam-v')
def sam_v_submit():
    best = request.args.get('v-1-sam-b')
    worst = request.args.get('v-1-sam-w')
    if best==worst:
        return render_template('gif-v-1-sam.html', mesg="PLEASE SELECT TWO DIFFERENT GIFS!")
    elif best==None or worst==None:
        return render_template('gif-v-1-sam.html', mesg="PLEASE ANSWER BOTH QUESTIONS!")
    else:
        return render_template('gif-a-1-sam.html', mesg="")

'''
@app.route('/def')
def def_submit():
    best = request.args.get('v-1-def-b')
    worst = request.args.get('v-1-def-w')
    if best==worst:
        return render_template('gif-v-1-def.html', mesg="PLEASE SELECT TWO DIFFERENT GIFS!")
    elif best==None or worst==None:
        return render_template('gif-v-1-def.html', mesg="PLEASE ANSWER BOTH QUESTIONS!")
    else:
        return render_template('gif-v-1-word.html', mesg="")

@app.route('/word')
def word_submit():
    best = request.args.get('v-1-word-b')
    worst = request.args.get('v-1-word-w')
    if best==worst:
        return render_template('gif-v-1-word.html', mesg="PLEASE SELECT TWO DIFFERENT GIFS!")
    elif best==None or worst==None:
        return render_template('gif-v-1-word.html', mesg="PLEASE ANSWER BOTH QUESTIONS!")
    else:
        return render_template('gif-a-1-sam.html', mesg="")
'''

@app.route('/sam-a')
def sam_a_submit():
    best = request.args.get('a-1-sam-b')
    worst = request.args.get('a-1-sam-w')
    if best==worst:
        return render_template('gif-a-1-sam.html', mesg="PLEASE SELECT TWO DIFFERENT GIFS!")
    elif best==None or worst==None:
        return render_template('gif-a-1-sam.html', mesg="PLEASE ANSWER BOTH QUESTIONS!")
    else:
        return render_template('gif-d-1-sam.html', mesg="")

@app.route('/sam-d')
def sam_d_submit():
    best = request.args.get('d-1-sam-b')
    worst = request.args.get('d-1-sam-w')
    if best==worst:
        return render_template('gif-d-1-sam.html', mesg="PLEASE SELECT TWO DIFFERENT GIFS!")
    elif best==None or worst==None:
        return render_template('gif-d-1-sam.html', mesg="PLEASE ANSWER BOTH QUESTIONS!")
    else:
        return render_template('thank.html', mesg="")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050, debug=True)