# In Day 35, we learn about environment variables.
# Environment variables are a bunch of variables that are set in environment in which you run your code.
# These variables have values that are in string. You can use them in your application or code.
# You can even use env command in pythonanywhere console to get to know about the environment variables.
# These variables will be relative to the pythonanywhere environment.
# Now why do we need to use environment variables?
# 1) For convenience:- You need to deploy a large application. That process is quite complicated.
# Because of that, you don't want to mess around your codebase.
# But, for example your application's work is to send out emails to your clients.
# You need to change your client base email every day.
# For that, you might have certain variables, you can set them  as environment variables.
# You can modify those variables without touching the code.
# 2) For security:- Suppose, you are developing software and uploaded the code over the internet.
# You are storing important information such as API key, auth token, appid etc,
# in the same location in which the rest of the code is in.
# It's going to be dangerous for your security when you have premium account.
# That's why, you can use environment variables.
# With the help of it, you can separate out the important variables in which API key, Auth token, etc is stored, from the rest of the code.
# In order to do it, you need to use "export name_of_the_environment_variable_you_want_to_create".
# Then without spaces, use "=" after that the value you want it hold.
# Now, in order to use the environment variable in any of the code from the particular environment.
# We need to take the help of os module, wherever the variable which is set to enviroment variable now, is created in the code.
# set it to "os.environ.get(environment_variable_name).
# The get method is used to get the value of said environment variable.