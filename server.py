from flask import Flask, render_template, request, redirect, url_for

import data_handler

app = Flask(__name__)

data = []


@app.route('/')
def home():
    data = data_handler.get_elements_csv('data.csv')
    return render_template('home.html', titles=data_handler.DATA_HEADER, elements=data)


@app.route('/story', methods=['GET', 'POST'])
def story():
    return render_template('story.html')


@app.route('/list')
def route_list():
    user_stories = data_handler.get_all_user_story()

    return render_template('list.html', user_stories=user_stories)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
