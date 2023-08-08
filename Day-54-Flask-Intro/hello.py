from flask import Flask

app = Flask(__name__)
# By providing the name to the flask, flask will check that the app code is from the current module not from any imported module.

print(__name__)
# As you can see, Here, we are initialising our flask applicatin with the help of Flask() class and passing a required input
# such as __name__. What is that?
# __name__ is a special attribute in python.
# You could tap into any class, function, methods, descriptors to get their respective name.
# When we get "__main__" as __name__ then, it tells us that we are executing code of the particular module.
# It runs code from script or interacting prompt but not from any imported module.

@app.route("/")
# When user hits up the following path means, he adds forward slash after the url given after running the code.
# He will get to see the homepage, there, he will see "Hello World!".
# Syntatically, It is a python decorator.
# Like for example, you might have lot of functions in your class or module.
# Each of those functions, you might want to add more functionality.
# You can do this by the help of decorators function.
# Decorator function is a kind of function, through it, we can add more functionality to existing functions.
# Functions are first class objects, that can be passed as an argument to other functions.
# You can create nested functions, means function defined inside of another function.
# The inner function is only accessible inside of the outer fuctions, means can't be called outside of it.
# To avoid it, you can return the inner function.
# To do this, you need to call the outer function, when it will be executed, it will return inner function.
# Set the result of this fuction to a variable. Through variable, you can call the inner function anytime regardless of scope issue.
 
def hello_world():
    return "<p>Hello, World!</p>"
# Here, @app.route('/') means that when the user go to homepage route or  the URL of the webstite's homepage.
# hello_world() is going to be run.

if __name__ == "__main__":
    # As you can see when we printed __name__, it gives us __main__.
    # Means we are running code from the current file.
    app.run()
    # Here, this line of code is doing the same thing when we go to the terminal and enter flask run.]
