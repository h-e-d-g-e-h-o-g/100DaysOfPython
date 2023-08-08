from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def intro():
    return "<h1>Guess a number between 0 and 9</h1>\
            <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"

random_number = random.randint(0, 9)
print(random_number)

# def guess(function):
#     def wrapper_function(*args):
#         guess_num = function(args[0])

#         if guess_num < random_number:
#             return "<h1>Too low, try again!<h1>\
#                     <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
#         elif guess_num > random_number:
#             return "<h1>Too high, try again!<h1>\
#                     <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
#         elif guess_num == random_number:
#             return "<h1>You found me!<h1>\
#                     <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"

#     return wrapper_function

@app.route("/<int:guess>")
def higher_or_lower(guess):
    if guess < random_number:
        return "<h1 style='color:red'>Too low, try again!<h1>\
                <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    elif guess > random_number:
        return "<h1 style='color:purple'>Too high, try again!<h1>\
                    <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    elif guess == random_number:
        return "<h1 style='color:green'>You found me!<h1>\
                <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)