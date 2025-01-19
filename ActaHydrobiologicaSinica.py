import os
import shutil
import time

from selenium.webdriver.common.by import By
from selenium import webdriver


import os
import time

def monitor_folder(folder_path, initial_files, interval=0.5):
    # 获取初始文件列表
    print("开始监控文件夹...")

    while True:
        time.sleep(interval)  # 间隔检查
        current_files = set(os.listdir(folder_path))
        new_files = current_files - initial_files

        # 判断是否有新增的 PDF 文件
        pdf_files = [file for file in new_files if file.lower().endswith(".pdf")]
        if pdf_files:
            print("检测到新增 PDF 文件:", pdf_files)
            break

        initial_files = current_files  # 更新文件列表

# 使用示例
folder_to_monitor = r"C:\Users\asus\Downloads"  # 替换为目标文件夹路径



from selenium.webdriver.edge.options import Options
# 配置 Edge 浏览器选项
options = Options()
options.add_experimental_option("detach", True)  # 启用调试模式
options.add_argument("--start-maximized")  # 启动时最大化窗口

baseUrl = "http://www.aquaticjournal.com/ssswxb/article/2019/1"
driver = webdriver.Edge()
driver.get(baseUrl)
flag = True
while flag:
    downloadList = driver.find_elements(By.XPATH, "//a[text()='PDF下载']")
    for download in downloadList:
        try:
            initial_files = set(os.listdir(folder_to_monitor))
            download.click()
            time.sleep(1)
            monitor_folder(folder_to_monitor, initial_files)
        except:
            continue
    next = driver.find_element(By.XPATH, "//a[text()='下一期']")
    if next:
        next.click()
    else:
        flag = False

input("按 Enter 键退出...")