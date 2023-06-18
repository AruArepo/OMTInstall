from selenium import webdriver
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Baseclass:
    data=''

    def get_list(self,ssh_client,path):
        _stdin, _stdout,_stderr=ssh_client.exec_command('cd '+path+';ls')
        for item in iter(_stdout.readline,""):
            return item

    def execution(self,ssh_client,cmd):
        _stdin, _stdout,_stderr=ssh_client.exec_command(cmd)
        for item in iter(_stdout.readline,""):
            print(item)
    
    def lpv_version(self,ssh_obj,cmd):
        _stdin, _stdout,_stderr=ssh_obj.exec_command('cd '+cmd)
        for item in iter(_stdout.readline,""):
            if item.__contains__('local-storage-provisioner'):
                return item

    def get_browser(self):
        firefox_options= webdriver.FirefoxOptions()
        firefox_options.add_argument('--ignore-certificate-errors')
        firefox_options.add_argument('--allow-insecure-localhost')
        driver=webdriver.Firefox(options=firefox_options)
        return driver
    
    def load_json(self,path):
        with open(path,'r') as f:
           data= json.load(f)
           return data          
    
    def open_url(self,driver,data):
        driver.get(data)

    def send_keys(self,driver,path,data):
        driver.find_element(By.XPATH,path).clear()
        driver.find_element(By.XPATH,path).send_keys(data)

    def click(self,driver,ele):
        driver.find_element(By.XPATH,ele).click()
    
    def waitforele(self,driver,ele,sec):
        WebDriverWait(driver,sec).until(EC.presence_of_element_located((By.XPATH,ele)))
        return driver.find_element(By.XPATH,ele)
    
    def close(self,driver):
        driver.close()

    def javascript(self,driver,path):
        driver.execute_script(path)
        
    def scrolltoview(self,driver,ele):
        driver.execute_script("arguments[0].scrollIntoView();", ele)

    def js_browserview(self,driver,cmd,):
        driver.execute_script(cmd)