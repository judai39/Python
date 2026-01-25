import requests
from requests.exceptions import RequestsWarning,Timeout,ConnectionError
# 网络请求天生不稳定,需要异常处理

# 1.异常处理
try:
    response=requests.get("https://httpbin.org/delay/5",timeout=3)
    response.raise_for_status()#检查当前状态码是否异常(正常的话就是200,不正常就是4xx,5xx)
    print(response.json)
except Timeout:
    print("请求超时了")
except ConnectionError:
    print("连接失败了")
except RequestsWarning:
    print("请求异常")

# 2.连接池复用(Requests默认会复用连接,但也可以手动控制)
# 什么叫连接池复用?
    # session = requests.Session()
    # response1 = session.get('https://www.example.com')
    # response2 = session.get('https://www.example.com')
    # response3 = session.get('https://www.example.com')
    # 由于session管理requests的生命周期,在默认情况下,这几个response均会访问通过一个请求实例
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session=requests.Session()
# pool_connection 允许维护的连接池数量（host 数量）上限。
# pool_maxsize 每个维护的连接池的可复用的tcp连接数量上限为20
# max_retries决定了连接请求异常的最大重连次数(total最大重连数,backoff_factor决定指数退避的等待时间-默认1)
adapter=HTTPAdapter(pool_connections=20,pool_maxsize=20,max_retries=Retry(total=3,backoff_factor=1))
# HttpAdapter挂载（mount）到 requests.Session()
session.mount('http://',adapter)
session.mount('https://',adapter)