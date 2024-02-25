from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Set up the Chrome driver
service = Service('/path/to/chromedriver')  # Set the path to your chromedriver executable
driver = webdriver.Chrome(service=service)

# Navigate to the website
driver.get('https://unstop.com/legal/privacy-policy')  # Replace 'https://example.com' with the URL of the website you want to scrape

# Wait for the content to load (you may need to adjust the waiting time)
driver.implicitly_wait(10)  # Wait for 10 seconds for the content to load

# Find the element containing the desired content
content_element = driver.find_element(By.XPATH, '//*[@id="content"]')  # Adjust the XPath to match the element containing the content

# Extract the text from the element
content = content_element.text

# Print or process the content as needed
print(content)

# Close the browser
driver.quit()
