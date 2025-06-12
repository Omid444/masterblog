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
    """Add new book if request is post and return index.html, otherwise it goes to add.html """
    if request.method == 'POST':
        # Add the code that handles adding a new blog
        title = request.form.get('title','')
        author = request.form.get('author','')
        content = request.form.get('content','')
        blog_posts.append({'id': len(blog_posts)+1, 'author': author, 'title': title, 'content': content})
        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    """Delete post by post id and return index.html"""
    for post in blog_posts:
        if post['id'] == post_id:
            blog_posts.pop(blog_posts.index(post))
            return redirect(url_for('index'))


def fetch_post_by_id(post_id):
    """Get post by its id"""
    for post in blog_posts:
        if post['id'] == post_id:
            return post


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """Update post if request is post and return index.html otherwise it goes tp update.html page"""
    # Fetch the blog posts from the JSON file
    post = fetch_post_by_id(post_id)
    if post is None:
        # Post not found
        return "Post not found", 404

    if request.method == 'POST':
        title = request.form.get('title','')
        author = request.form.get('author','')
        content = request.form.get('content','')
        post['title'] = title
        post['author'] = author
        post['content'] = content
        return redirect(url_for('index'))
    return render_template('update.html', post=post)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)