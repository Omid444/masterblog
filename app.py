from flask import Flask, render_template, request, redirect, url_for
import json
import os
app = Flask(__name__)


def load_post():
    """Upload json file, if no such file exist in path or if it is empty it will return empty list"""
    if os.path.exists('data/blog_posts.json'):
        with open('data/blog_posts.json', 'r') as file:
            content = file.read().strip()
            if content:
                return json.loads(content)
    return []


def save_post(posts):
    """Write changes to jason file"""
    json_post = json.dumps(posts, indent=4)
    with open('data/blog_posts.json', 'w') as file:
        file.write(json_post)


blog_posts = load_post()


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
        if all([title, author, content]):
            blog_posts.append({'id': (max(post['id'] for post in blog_posts) + 1), 'author': author, 'title': title, 'content': content})
            save_post(blog_posts)
            return redirect(url_for('index'))
        else:
            return "all field must be filled"

    return render_template('add.html')


@app.route('/delete/<int:post_id>', methods=['GET'])
def delete(post_id):
    """Delete post by post id and return index.html"""
    post = fetch_post_by_id(post_id)
    if post is None:
        # Post not found
        return "Post not found", 404

    for post in blog_posts:
        if post['id'] == post_id:
            blog_posts.pop(blog_posts.index(post))
            save_post(blog_posts)
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
        print(title, content, author)
        print(all([title, author, content]))
        if all([title, author, content]):
            post['title'] = title
            post['author'] = author
            post['content'] = content
            save_post(blog_posts)
            return redirect(url_for('index'))
        else:
            return "all field must be filled"

    return render_template('update.html', post=post)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)