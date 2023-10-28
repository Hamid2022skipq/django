import requests
import json
URL='http://127.0.0.1:8000/stuCreate/'
data={
    'name':'M. Iqran Khan',
    'roll':4,
    'city':'Narowal'
}
json_data=json.dumps(data)
re=requests.post(URL,json_data)
if re.status_code // 100 == 2:
    try:
        result = re.json()
        print(result)
    except json.JSONDecodeError:
        print("Invalid JSON response from the server.")
else:
    print(f"Request failed with status code: {re.status_code}")

# update Data
URL1='http://127.0.0.1:8000/stuUpdate/'
data={
    'name':'M. Iqran Khan',
    'city':'Lahore'
}
json_data=json.dumps(data)
re=requests.put(URL1,json_data)
if re.status_code // 100 == 2:
    try:
        result = re.json()
        print(result)
    except json.JSONDecodeError:
        print("Invalid JSON response from the server.")
else:
    print(f"Request failed with status code: {re.status_code}")


