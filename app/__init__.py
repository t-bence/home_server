from flask import Flask

app = Flask(__name__)
# import views
from app import views

if __name__ == "__main__":
    app.run()