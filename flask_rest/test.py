import requests
from requests.api import request

BASE = "http://127.0.0.1:5000/"

# data = [{"likes": 10,"name":"Tim","views":100},
#         {"likes": 1000,"name":"Bill","views":500000},
#         {"likes": 25,"name":"Anne","views":7540}]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())

# input()
response = requests.patch(BASE + "video/2",{'views':99, 'likes':101})
print(response.json())
 