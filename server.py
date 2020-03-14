from flask import Flask, render_template, request, redirect, url_for

import data_handler

app = Flask(__name__)

headers = [' '.join(header.split("_")) for header in data_handler.DATA_HEADER]
data = {}


@app.route('/')
def home():
    data = data_handler.get_elements_csv()
    return render_template('home.html', headers=headers, data=data[1:])


@app.route('/story', methods=['GET', 'POST'])
def story():
    if request.method == 'POST':
        title = request.form['title']
        user_story = request.form['story']
        acceptance_criteria = request.form['acceptance_criteria']
        business_value = request.form['business_value'] + " point"
        estimation = request.form['estimation'] + "h"
        status = request.form['status']
        _id = data_handler.get_id()
        row = [_id, title, user_story, acceptance_criteria, business_value, estimation, status]

        data_handler.add_element_csv(row)

        return redirect('/')

    return render_template('story.html')


@app.route('/list')
def route_list():
    user_stories = data_handler.get_all_user_story()

    return render_template('list.html', user_stories=user_stories, status='')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
