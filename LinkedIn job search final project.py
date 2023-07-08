import requests
from bs4 import BeautifulSoup

# Send an HTTP GET request to the webpage
url = "https://www.linkedin.com/jobs/search/?currentJobId=3648738004&geoId=105646813&location=Spain&refresh=true"
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find and extract the desired data from HTML elements
job_titles = soup.find_all('h3', class_='base-search-card__title')
for title in job_titles:
    print(title.text.strip())

# Save the data (example: write to a CSV file)
with open('job_titles.csv', 'w') as file:
    for title in job_titles:
        file.write(title.text.strip() + '\n')
