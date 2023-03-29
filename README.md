# poc-g
# POC generation

### 介绍

> 快速生成一个漏洞验证、或者批量漏洞验证的POC

### 参数

```
options:
  -h, --help            show this help message and exit
  -m METHOD, --method METHOD
                        HTTP method (get, post, put)
  -p PATH, --path PATH  HTTP url path
  -d DATA, --data DATA  HTTP request post data
  -c CTYPE, --ctype CTYPE
                        HTTP request post Content-Type
  -f FILE, --file FILE  HTTP request post upload filename
  -s STATUS, --status STATUS
                        HTTP status code
  -r RESPONSE, --response RESPONSE
                        HTTP response body
  -o OUTPUT, --output OUTPUT
                        Output Python file
```

### 使用

> 生成一个test.py文件，GET请求，URL路径为/index.html，当状态码为200的时候显示漏洞存在

![image-20230328135029845](F:\image\image-20230328135029845.png)

> 生成一个test.py文件，POST请求，请求体为username=admin&password=123456&submit=login，当状态码为200并且响应包包含"login success"的时候显示漏洞存在

![image-20230329111419602](F:\image\image-20230329111419602.png)

> 生成一个test.py文件，POST请求，上传文件1.png，当响应包包含"上传成功"的时候显示漏洞存在

![image-20230329112353125](F:\image\image-20230329112353125.png)

>生成一个test.py文件，PUT请求，请求体为id=1，当状态码为200的时候显示漏洞存在

![image-20230329112941992](F:\image\image-20230329112941992.png)

