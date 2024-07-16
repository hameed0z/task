from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import url_changes
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

def get_request(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless") # Ensure GUI is off
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--enable-javascript")
    chrome_options.add_argument("--enable-cookies")

    webdriver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
    
    driver.get(url)
    # Wait for the URL to change
    WebDriverWait(driver, 10).until(url_changes(url))
    # Wait for the loader to disappear, mean data is loaded
    loader_class_name = "loader-wrpr"
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, loader_class_name)))

    page_source = driver.page_source
    driver.quit()
    
    return page_source

url = 'https://proscheduler.prometric.com/?prg=SCHS&path=seatavail'
output = get_request(url)

# We can use BeautifulSoup to fetch the data from the output html and make it more organized, but requirements doesn't say so
# So, I will just write the output to a file
with open('output.html', 'w') as f:
    f.write(output)
