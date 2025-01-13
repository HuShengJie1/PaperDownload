import os
import shutil
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--disable-blink-features=AutomationControlled")

# 这行代码添加了一个启动参数，用于禁用Chrome中的Blink引擎特性--AutomationControlled

profile = {"download.default_directory": "./download", "download.prompt_for_download": False,
           "profile.default_content_setting_values.automatic_downloads": 1}
options.add_experimental_option("prefs", profile)

#options.add_argument("--headless")
options.add_argument("--disable-gpu")

#user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/"
#             "537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
#options.add_argument(f'user-agent={user_agent}')
# 禁用下载保护，允许下载所有类型的内容,禁用pdf查看器
options.add_experimental_option("prefs", {"download_restrictions": 0})
options.add_experimental_option("prefs", {"safebrowsing.enabled": False})
options.add_experimental_option("prefs",{"plugins.always_open_pdf_externally": True})
options.add_argument("--unsafely-treat-insecure-origin-as-secure=http://journal.yykxjz.cn")

baseUrl = "http://journal.yykxjz.cn/yykxjz/ch/reader/issue_browser.aspx"
driver = webdriver.Chrome(options=options)
driver.get(baseUrl)

PaperURL = driver.find_elements(By.XPATH,"//table//a")
for i,url in enumerate(PaperURL):
    PaperURL[i] = url.get_attribute("href")

for url in PaperURL:
    driver.get(url)
    downloadList = driver.find_elements(By.XPATH, "//a[contains(@href, 'create_pdf.aspx')]")
    for download in downloadList:
        download.click()
        time.sleep(1)
    time.sleep(5)