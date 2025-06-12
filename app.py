from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

blog_posts = [
    {'id': 1, 'author': 'John Doe', 'title': 'First Post', 'content': 'This is my first post.'},
    {'id': 2, 'author': 'Jane Doe', 'title': 'Second Post', 'content': 'This is another post.'},
    # More blog posts can go here...
]


@app.route('/')
def index():
    # add code here to fetch the job posts from a file
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # Add the code that handles adding a new blog
        title = request.form.get('title','')
        author = request.form.get('author','')
        content = request.form.get('content','')
        blog_posts.append({'id': len(blog_posts)+1, 'author': author, 'title': title, 'content': content})
        return redirect(url_for('index'))

    return render_template('add.html')



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)