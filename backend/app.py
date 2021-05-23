from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def hello_world():
    return render_template('index.html', show_hero_section=True)

@app.route('/blog.html')
def blog():
    return render_template('blog.html')

@app.route('/about-us.html')
def about_us():
    return render_template('about-us.html')

@app.route('/blog-single.html')
def blog_single():
    return render_template('blog-single.html')

@app.route('/portfolio-details.html')
def portfolio_details():
    return render_template('portfolio-details.html')       

if __name__ == '__main__':
    app.run(debug=True)
