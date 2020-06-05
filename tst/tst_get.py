import json

import urllib3

get_url = "http://0.0.0.0:8383/get_task/"
data = {
    "id": "1"
}

params = "?"
for key in data:
    params = params + key + "=" + data[key] + "&"

params = params[:-1]

print("Get方法参数：" + params)

headers = {
    # heard部分直接通过chrome部分request header部分
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '14',  # get方式提交的数据长度，如果是post方式，转成get方式：【id=wdb&pwd=wdb】
    'Content-Type': 'application/x-www-form-urlencoded'

}

encoded_data = json.dumps(data).encode("utf-8")
http = urllib3.PoolManager()
r = http.request(
    "GET",
    get_url,
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
