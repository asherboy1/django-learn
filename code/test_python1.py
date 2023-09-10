from seleniumwire import webdriver 

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/firstapp/login/")

driver.find_element_by_name("username").send_keys("tony")
driver.find_element_by_name("password").send_keys("1234")
driver.find_element_by_name("submit").click()

for requests in driver.requests:
    if requests.__str__() == "http://127.0.0.1:8000/firstapp/login/":
        print(requests.params)
        # print(requests.querystring)