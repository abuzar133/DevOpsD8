from pprint import pprint
import requests
#getting the response from the api, pass the url of the api,get the response code and print the json response
def get_api_response(url):
    response = requests.get(url)
    print(response.status_code)
    json_response = response.json()
    pprint(json_response)
    data = json_response["data"]
    # print(data)
    for user in data:
        print(user["first_name"])
get_api_response("https://reqres.in/api/users?page=2")

#post data to the api, pass the url and the data to be posted
def post_api_data(url,data):
    response = requests.post(url,data)
    print(response.status_code)
    print(response.text)
post_api_data("https://reqres.in/api/users",{
    "name": "morpheus",
    "job": "leader",
    "id": "410",
    "createdAt": "2024-09-24T13:33:52.341Z"
})

#########################PUT METHOD##########################
def put_api_response(url,data):
    response = requests.put(url)
    print(response.status_code)
    json_response = response.json()
    pprint(json_response)
put_api_response("https://reqres.in/api/users/2", {
    "name": "morpheus",
    "job": "zion_resident",
    "updatedAt": "2024-09-24T14:01:54.188Z"
})







