from . import app      ##在当前程序所在文件夹里__init__.py程序中导入app
from .forms import FeatureForm

from flask import render_template

from models.review import ReviewModel
review_model = ReviewModel()

@app.route('/') ## route() 装饰器来告诉 Flask 触发函数的 URL 。'/'的意思应该就是当前
def index():
    return render_template('welcome.html')


@app.route('/form/', methods=('GET', 'POST'))     ##'/form/'是在当前的下面，因为后面在welcome.html下要触发这个函数
def form():
    myform = FeatureForm()
    if myform.is_submitted():  # once submit is clicked
        line = myform.review_text.data
        sentiment, highlight_words = review_model.predict(line, highlight=True)

        # redirect to result.html and render it with the data we provided
        return render_template('result.html',
                               line=line,   ##这些后面红色的参数，应该是自己定义的变量，在result.html 中要用到的
                               highlight_words=highlight_words,
                               sentiment=sentiment)

    return render_template('form.html', form=myform)

@app.route('/result/')
def submit():
    return render_template('result.html')

@app.route('/test')
def test():
    return render_template('test.html')



@app.route('/contact')
def contact():
    return 'Contact me . x9liu@ucsd.edu'


@app.route('/author')
def author():
    return 'XIN LIU'

@app.route('/about')
def about():
    return render_template('About.html')


