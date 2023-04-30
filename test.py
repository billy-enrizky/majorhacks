from flask import Flask, render_template, request, redirect

import gpt
from answer_key import dictionary, env
import subprocess
import web_use_page
import final_page
import web_use_2
from gpt import fc

app = Flask(__name__, static_url_path='/static')
app.template_folder = 'templates'


personal_info = []
retriever_1 = []
retriever_2 = []
result = []
description = []


@app.route('/')
def home():
    return render_template('website.html')


@app.route('/next', methods=['POST'])
def next():
    personal_info.extend([request.form.get('name'), request.form.get('email'),
                          request.form.get('age')])
    question = ['q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11']
    for q in question:
        retriever_1.append(request.form.get(q))
    major = final_page.fc(retriever_1)
    result.append(major)
    return redirect('/unitypes')


@app.route('/unitypes', methods=['GET', 'POST'])
def unitypes():
    return render_template('second.html')


@app.route('/submit', methods=['POST'])
def submit():
    retriever_2.append(request.form.get('q1'))
    retriever_2.append(request.form.get('q2'))
    retriever_2.append(request.form.get('q3'))
    retriever_2.append(result[0])
    uni = web_use_2.fc(retriever_2, retriever_1)
    result.extend(uni)
    description.extend(gpt.fc(result[0], result[1], result[2], result[3]))
    return redirect('/thanks')


@app.route('/thanks')
def thanks():
    return render_template('results.html', x=result[1], y=result[2], z=result[3]
                           , a=result[0], m=description[1], n=description[2],
                           o=description[3], p=description[0])


if __name__ == "__main__":
    print("starting")
    a = app.run(debug=True)
