from PIL import Image
import requests
from io import BytesIO
import getpass

def youtube_download_maxresdefault_cover(img_url:str,vedio_name:str,download_path:str):
    response = requests.get(img_url)
    image = Image.open(BytesIO(response.content))
    # 保存到指定文件夹
    image.save(f"{download_path}/{vedio_name}.png")
    # print(f"C:/Users/judai/Desktop/youtube_download/{vedio_name}")