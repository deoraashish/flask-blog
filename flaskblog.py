from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'title': 'Article 1',
        'author': 'Ashish Deora',
        'date_posted': '23rd April 2020',
        'content': 'Hello world'
    },
    {
        'title': 'Article 2',
        'author': 'Vinay Makwana',
        'date_posted': '24th April 2020',
        'content': 'Hello world again'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
