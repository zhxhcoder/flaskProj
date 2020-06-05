import json
import urllib3

post_url = "http://0.0.0.0:8383/add_task/"

data = {
    "id": "2",
    "info": "第二",
}
encoded_data = json.dumps(data).encode("utf-8")
http = urllib3.PoolManager()
r = http.request(
    "POST",
    post_url,
    body=encoded_data,
    headers={
        'content-type': 'application/json;charset=UTF-8'
    }
)
if r.status == 200:
    response = r.data
    if len(response) > 0:
        j = json.loads(response)
        print(j)
