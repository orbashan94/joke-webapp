import random
from flask import Flask

app = Flask(__name__)

joke_1 = "What's the best thing about Switzerland ?? I don't know but the flag is a big plus."
joke_2 = "How do trees get online? They just log on!"
joke_3 = "What is an astronaut's favorite part on a computer? The space bar."
joke_list = [joke_1,joke_2,joke_3]

@app.route('/')
def main():
    return 'Welcome to my jokes jenerator'

@app.route("/joke")
def get_joke():
    return random.choice(joke_list)

if __name__ == "__main__":
    app.run()
