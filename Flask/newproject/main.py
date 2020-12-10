from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World'
app.add_url_rule('/', 'hello', hello_world)

@app.route('/admin/')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as guest' % guest

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

@app.route('/blog/<int:postID>')
def show_blod(postID):
    return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f' % revNo

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))

if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug=True)
# https://www.tutorialspoint.com/flask/flask_http_methods.htm
