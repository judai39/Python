import requests

# # requests库发送请求基础用法

# # 1.发送get请求
# # 不带参数
# response_1=requests.get('https://httpbin.org/get')
# print(response_1.text)
# # 带参数
# params={'key1':'value1','key2':'value2'}
# response_2=requests.get('https://httpbin.org/get',params=params)
# print(response_2.text)

# # 2.发送post请求
# # 发送json数据
# json_data={'username':'test','password':'123456'}
# response_3=requests.post('https://httpbin.org/post',json=json_data)
# print(response_3.text)
# # 发送表单数据
# form_data={'key':'value'}
# response_4=requests.post('https://httpbin.org/post',data=form_data)
# print(response_4.text)

# # 3.处理Headers和认证
# # 自定义请求头
# headers={
#     'User-Agent':'My App 1.0',
#     'Accept':'application/json',
#     'Authorization':'Bearer Your Token Here'
# }
# response_5=requests.get('https://httpbin.org/post',headers=headers)
# print(response_5.text)
# # http基础认证
# response_6=requests.get('https://httpbin.org/basic-auth/user/pass',auth=('user','pass'))
# print(response_6.text)

# # 3.Session保持登录状态
# # 实例化一个管理reqeusts实例对象生命周期的对象,即session()
# session=requests.Session()
# # 登录
# login_data={'username':'your_user','password':'your_pass'}
# session.post('https://example.com/login',data=login_data)
# # 由于将参数交由管理requests生命周期的session实例对象,因此全局可用,这之后的登录均会携带参数
# protected_page=session.get('https://example.com/dashboard')

# # 4.文件上传下载
# # 上传
# files={'files':open(r'C:\Users\judai\Desktop\tobe.txt','rb')}
# response_7=requests.post('https://httpbin.org/post',files=files)
# # (1)普通下载
# url='https://www.hangge.com/blog/images/logo.png'
# response_8=requests.get(url)
# with open("logo.png","wb")as code:
#     code.write(response_8.content)
# # (2)流式下载(分块下载,边下载边保存,适合大文件)
# response_9=requests.get(url,stream=True)#stream参数设置为真开启
# with open("logo2.png","wb")as f:
#     for files_odds in response_9.iter_content(chunk_size=1024):
#         if files_odds:
#             f.write(files_odds)
# (3)带进度的文件下载
fileUrl='https://vdownload.hembed.com/402988-720p.mp4?secure=FyNXTpqt5554_rqS1eCE4w==,1769364001'
filePath='aaaa.mp4'
from contextlib import closing
with closing(requests.get(url=fileUrl,stream=True))as response:
    chunk_size=1024#单次请求最大值
    content_size=int(response.headers['content-length'])#内容总大小
    data_count=0
    with open(filePath,"wb")as file:
        for data in response.iter_content(chunk_size=chunk_size):
            file.write(data)
            data_count=data_count+len(data)
            now_jd=(data_count/content_size)*100
            print("\r 文件下载进度为:%d%%(%d/%d) - %s"%(now_jd,data_count,content_size,filePath),end=" ")