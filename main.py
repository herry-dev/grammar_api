from flask import Flask
from players.player import charbp
from accounts.signup import createnew

app = Flask(__name__)
app.register_blueprint(createnew)
app.register_blueprint(charbp)
if __name__ == '__main__':
    app.run(debug=False)
