import requests
from bs4 import BeautifulSoup

# Function to extract text from a webpage
def extract_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    print(text)
    return text

# Function to save text to a file
def save_to_file(text, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

# Main function
def websScrape(url):
    # URL of the webpage


    # Make a request to the webpage
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find links for Privacy Policy and Terms and Conditions

    privacy_policy_link = soup.find('a', href=True, string='Privacy Policy')['href']
    print(privacy_policy_link)
    # terms_conditions_link = soup.find('a', href=True, string='terms of use')['href']
    # print(url + terms_conditions_link)
    
    # Extract text from Privacy Policy and Terms and Conditions pages
    privacy_policy_text = extract_text(privacy_policy_link)
    # terms_conditions_text = extract_text(terms_conditions_link)

    # # Save the text to files
    save_to_file(privacy_policy_text, 'privacy_policy.txt')
    # save_to_file(terms_conditions_text, 'terms_conditions.txt')
    return privacy_policy_text


