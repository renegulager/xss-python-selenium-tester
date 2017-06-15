from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from string import Template
import unittest, json

CHROMEDRIVER = './bin/gekodriver'
TESTID = '1'
urls = 'http://192.168.99.100/vulnerabilities/xss_r/?name=${INPUT}'
payloads = [ """<script>console.error(${TID})</script>""",
"""console.error(${TID})//<svg/onload=console.error(${TID})>'-console.error(${TID})-'""" ]



class XSSTest(unittest.TestCase):
  ##  Setup browser etc.
   def setUp(self):
       fp = webdriver.FirefoxProfile()
       fp.set_preference("general.useragent.override","XSS fuzzer")
       fp.update_preferences()
       self.driver=webdriver.Firefox(firefox_profile=fp)

   def tearDown(self):
##self.driver.result()
       self.driver.quit()

   def logIn(self):
        self.driver.get(urls)
        username = driver.find_element_by_name("username")
        password = driver.find_element_by_name("password")
        username.send_keys("admin")
        password.send_keys("password")
        self.driver.find_element_by_name("Login").click()


   def test_run(self):
       id = int(TESTID)*10;
     ##  logIn()
       
       self.driver.get(urls)
       username = self.driver.find_element_by_name("username")
       password = self.driver.find_element_by_name("password")
       username.send_keys("admin")
       password.send_keys("password")
       self.driver.find_element_by_name("Login").click()

       for xss in payloads:
           xss1 = Template(xss).substitute(TID=str(id))
           url1 = Template(urls).substitute(INPUT=xss1)
           print url1
           id = id + 1
           self.driver.get(url1)

   def result(self):
     n = 0
     for cmsg in self.driver.get_log('browser'):
         if -1 != str(cmsg).find(" " + TESTID):
           print(json.dumps(cmsg))
           n += 1
    
     self.assertEqual(0, n)

# entry point
if __name__ == "__main__":
 unittest.main()
