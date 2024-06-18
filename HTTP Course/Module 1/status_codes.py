import requests

def make_request(method, url, headers=None, payload=None):
    response = requests.request(method, url, headers=headers, data=payload)
    print(f"Status Code: {response.status_code}")
    print(response.text)

# 101
make_request("POST", "http://httpbin.org/status/101")

# 201
make_request("POST", "https://reqres.in/api/users")

# 204
make_request("DELETE", "https://reqres.in/api/users/2")

# 302
make_request("GET", "http://httpbin.org/redirect/1")

# 400
make_request("POST", "https://reqres.in/api/register")

# 401
make_request("GET", "http://httpbin.org/basic-auth/user1/pswd")

# 404
make_request("GET", "https://reqres.in/users/23")

# 500
make_request("DELETE", "http://httpbin.org/redirect-to")



