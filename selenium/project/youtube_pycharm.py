from ssl import SSLError
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from youtube_locate_operation import youtube_download_cmd_m4a_f140
from youtube_cover_download import youtube_download_maxresdefault_cover
import os
import getpass

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.youtube.com/@necomakarin")
download_content_div='癒しのASMR♡ -人気順-'
# driver_link=input("请输入您要下载视频的管主主页链接")
# driver.get(driver_link)
# download_content_div=input("请输入您要下载的收藏夹的收藏夹名")
element_shouye_container1=driver.find_element(By.XPATH,f"//div[@class='style-scope ytd-two-column-browse-results-renderer']//div[@id='contents']//span[text()='{download_content_div}']/parent::a")
element_shouye_container1.click()

spicify_content_div=WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH,"//div[@id='content' and @class='style-scope ytd-app']/ytd-page-manager[@id='page-manager']/ytd-browse[@class='style-scope ytd-page-manager']/ytd-two-column-browse-results-renderer[@class='style-scope ytd-browse grid grid-disabled']//div[@id='contents' and @class=' style-scope ytd-playlist-video-list-renderer']"))
)

# driver.execute_script("var q=document.documentElement.scrollTop=10000")
# time.sleep(5)
# driver.execute_script("var q=document.documentElement.scrollTop=20000")
# time.sleep(5)
# driver.execute_script("var q=document.documentElement.scrollTop=30000")
# time.sleep(5)

# 获取到了当前用户下的所有关于癒しのASMR♡ -人気順-的视频div
vedio_div_list=spicify_content_div.find_elements(By.XPATH,"//ytd-playlist-video-renderer[@class='style-scope ytd-playlist-video-list-renderer']")
vedio_meta_element_list_len=len(vedio_div_list)
vedio_meta_element_list=[]
vedio_meta_title_list=[]
vedio_meta_href_list=[]
vedio_thumbnail_img_href_list=[]
for index in range(0,vedio_meta_element_list_len):
    vedio_meta_element_list.append(vedio_div_list[index].find_element(By.XPATH,".//a[@id='video-title']"))
    vedio_meta_title_list.append(vedio_meta_element_list[index].get_attribute("title"))
    vedio_meta_title_list[index]=vedio_meta_title_list[index].replace('/','#')
    vedio_meta_href_list.append(vedio_meta_element_list[index].get_attribute("href").split("&")[0])
    try:
        vedio_thumbnail_img_href_list.append("https://img.youtube.com/vi/"+vedio_meta_href_list[index].split("=")[1]+"/maxresdefault.jpg")
    except SSLError:
        vedio_thumbnail_img_href_list.append("https://i.ytimg.youtube.com/vi/"+vedio_meta_href_list[index].split("=")[1]+"/maxresdefault.jpg")
    
for index in range(0,2):
    # 本地创建下载路径
    download_path=f"C:/Users/{getpass.getuser()}/Desktop/youtube_download_project/youtube_download/{vedio_meta_title_list[index]}"
    try:
        os.makedirs(download_path)
    except FileExistsError:
        print(f"{vedio_meta_title_list[index]}文件夹已经存在")
    # 本地脚本操作下载视频
    youtube_download_cmd_m4a_f140(vedio_link=vedio_meta_href_list[index],vedio_name=vedio_meta_title_list[index],download_path=download_path)
    # 下载封面
    youtube_download_maxresdefault_cover(img_url=vedio_thumbnail_img_href_list[index],vedio_name=vedio_meta_title_list[index],download_path=download_path)