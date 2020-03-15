from flask import Flask, render_template, request, redirect, url_for

import data_handler

app = Flask(__name__)
app.jinja_env.lstrip_blocks = True
app.jinja_env.trim_blocks = True

headers = [' '.join(header.split("_")) for header in data_handler.DATA_HEADER]
data = {}


@app.route('/')
def home():
    data = data_handler.read_elements_csv()
    return render_template('home.html', headers=headers, data=data[1:])


@app.route('/story', methods=['GET', 'POST'])
def story():
    if request.method == 'POST':
        title = request.form['title']
        user_story = request.form['story']
        acceptance_criteria = request.form['acceptance_criteria']
        business_value = request.form['business_value']
        estimation = request.form['estimation']
        user_id = data_handler.get_id()

        row = [user_id, title, user_story, acceptance_criteria, business_value, estimation]
        data_handler.add_element_csv(row)

        return redirect('/')

    return render_template('story.html')


@app.route('/story/<int:user_id>', methods=['GET', 'POST'])
def story_id(user_id):
    requested_dict = data_handler.get_element_by_id(user_id)
    if request.method == 'POST':
        title = request.form['title']
        user_story = request.form['story']
        acceptance_criteria = request.form['acceptance_criteria']
        business_value = request.form['business_value']
        estimation = request.form['estimation']
        status = request.form['status']

        row = [user_id, title, user_story, acceptance_criteria, business_value, estimation, status]
        data_handler.add_element_csv(row, user_id)

        return redirect('/')

    return render_template('story.html', data=requested_dict)


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
