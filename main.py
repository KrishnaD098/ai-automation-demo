from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://duckduckgo.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("EY careers automation")
search_box.submit()

time.sleep(5)

results = driver.find_elements(By.CSS_SELECTOR, "a[data-testid='result-title-a']")

print("\nSearch result titles:\n")

if len(results) == 0:
    print("No title found")
else:
    for index, result in enumerate(results, start=1):
        title = result.text

        if title:
            print(f"{index}. {title}")

driver.quit()