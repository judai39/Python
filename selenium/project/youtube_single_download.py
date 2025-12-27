from ssl import SSLError
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from youtube_locate_operation import youtube_download_cmd_m4a_f140
from youtube_cover_download import youtube_download_maxresdefault_cover
import getpass

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver_link=input("请输入您要下载的视频链接:")
vedio_download_href=driver_link.split("&")[0]

driver.get(vedio_download_href)
vedio_title=driver.find_element(By.XPATH,"//div[@id='above-the-fold' and @class='style-scope ytd-watch-metadata']/div[@id='title']/h1[@class='style-scope ytd-watch-metadata']/yt-formatted-string[1]").get_attribute("title")
download_path=f"C:/Users/{getpass.getuser()}/Desktop/youtube_download_project/youtube_download/{vedio_title}"
try:
    vedio_cover_download_href="https://img.youtube.com/vi/"+vedio_download_href.split("=")[1]+"/maxresdefault.jpg"
except SSLError:
    vedio_cover_download_href="https://i.ytimg.youtube.com/vi/"+vedio_download_href.split("=")[1]+"/maxresdefault.jpg"

youtube_download_cmd_m4a_f140(vedio_link=vedio_download_href,vedio_name=vedio_title,download_path=download_path)
youtube_download_maxresdefault_cover(img_url=vedio_cover_download_href,vedio_name=vedio_title,download_path=download_path)