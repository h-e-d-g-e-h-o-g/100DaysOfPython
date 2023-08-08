# Today, we learn about different types of requests.
# As, we already know how to make http requests across the internet with the help of requests module.
# 1)First, we already read about the get request in which we retrieve the data from the external service through making get request.
# 2)Second is post request, in which we send our data to the external service. For example:- saving data in spreadsheet.
# We can do this by making the post request to the googele sheets API.
# 3) Third is put request, in this kind of request, we update the stored data in external service.
# Like, updating the values in google sheets by making put request.
# 4) Fourth is, delete request, in which we delete the data in the external service.
# Now, to create Habit tracker, we are going to use pixela API.
# First, we need to create our account to use it.
# To make our user account, we need to make POST request.
import requests
from datetime import datetime
USER_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "sdlkfjsdklfjasdf532"
USERNAME = "h-e-d-g-e-h-o-g"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url="https://pixe.la/v1/users", json=user_params)
# Here, i have used json keyword argument to pass required parameters.
# print(response.text)
# Here, i have used text property to print the response in text format.
# Now, i have commented out the post request code because, as the account already made.
# Now, if it runs, it gives me an error. As, the username is registered.

# Now, the next step is to create a graph.
# To create a graph, we need to make a post request to different endpoint.
GRAPH_ENDPOINT = f"{USER_ENDPOINT}/{USERNAME}/graphs"

header = {
    "X-USER-TOKEN": TOKEN
}

graph_params = {
    "id": "graph1",
    "name": "Studying",
    "unit": "hours",
    "type": "float",
    "color": "sora"
}
# Here, i am providing the required parameters that are necessary to make post request to the endpoint.
# id is used to identify the graph in the url.
# name is used to set the name of the graph.
# unit is used to specify the unit to measure the data that graph deals with.
# type is used to specify the datatype of the unit of measure.(only int and float are allowed)
# color is used to set the color of the graph.

# Now, if you try to make the request. Then, it will raise an error.
# Because, there is no way to authenticate you. Means, No way to verify that you are the one that trying to create graph that associates with your account.
# To authenticate yourself, the api providers want you to do the authentication through header.
# In previous works, we don't need to do the authentication in the header part.
# As, there are many ways to authenticate yourself.
# It is one of the ways, but it is the most secure.
# As, in other ways, when we make a request to the endpoint. The url will contain our api key.
# But, it is still safe. As, the request is done through HTTPS. The 'S' stand for secure.
# Our request will be in encrypted form. But, still it can be leaked to someone.
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=header)
# print(response.text)

# Adding pixel to the graph
PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{graph_params['id']}"
today = datetime.now()
DATE = today.strftime("%Y%m%d")
# Formatting the date, whatever requirement we have using strftime().
pixel_params = {
    "date": DATE,
    "quantity": input("How many hours did you study today?")
}
response = requests.post(url=PIXEL_ENDPOINT, json=pixel_params, headers=header)
print(response.text)

UPDATE_PIXEL_ENDPOINT = f"{PIXEL_ENDPOINT}/{DATE}"
update_params = {
    "quantity": "2.51",
}
# response = requests.put(url=UPDATE_PIXEL_ENDPOINT, json=update_params, headers=header)
# print(response.text)
delete_endpoint = UPDATE_PIXEL_ENDPOINT
# response = requests.delete(url=delete_endpoint, headers=header)
# print(response.text)