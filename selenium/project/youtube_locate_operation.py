import pyautogui
import time
import pyperclip
import getpass

# 下载视频
def youtube_download_cmd_mp4_f96(vedio_link:str,vedio_name:str,download_path:str):
    pyautogui.keyDown('win')
    pyautogui.press('r')
    pyautogui.keyUp('win')
    pyautogui.write('cmd')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.write(f'yt-dlp -f96 "{vedio_link}"')
    pyperclip.copy(f' -o "{download_path}/{vedio_name}.m4a"')
    time.sleep(2)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')

# 下载音频
def youtube_download_cmd_m4a_f140(vedio_link:str,vedio_name:str,download_path:str):
    pyautogui.keyDown('win')
    pyautogui.press('r')
    pyautogui.keyUp('win')
    pyautogui.write('cmd')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.write(f'yt-dlp -f140 "{vedio_link}"')
    pyperclip.copy(f' -o "{download_path}/{vedio_name}.m4a"')
    time.sleep(2)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    