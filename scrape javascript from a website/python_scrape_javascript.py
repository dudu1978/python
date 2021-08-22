from selenium import webdriver
import time

## Please update your HTTP Link
web_site = 'http://11.1.1.1'
browser = webdriver.Firefox(executable_path = 'C:/Users/geckodriver.exe')  # This is required for selenium firefox driver

driver = webdriver.Firefox()
driver.get(web_site)
time.sleep(10)
p_element = driver.execute_script("return date")
print(p_element)



######### This python will scrape the date varible that is running as a javascript in a web page######
### Index html ####
# <!-- Current Date -->
# Current Date:
# <input type="text" id="currentDate">
# <br><br>
# <script>
#   var today = new Date();
#   var year = today.getFullYear();
#   var month = today.getMonth()+1;
#   var day = today.getDate()
#   if (month < 10) {
#     month = "0" + month }
#   if (day < 10) {
#     day = "0" + day }
#   var date = year+'-'+month+'-'+day;
#   document.getElementById("currentDate").value = date;
# </script>
