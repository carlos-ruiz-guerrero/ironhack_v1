import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.infojobs.net/jobsearch/search-results/list.xhtml?keyword=Data%20engineer&normalizedJobTitleIds=2511_258e46f9-0075-4a2e-adae-1ff0477e0f30&provinceIds=&cityIds=&teleworkingIds=&categoryIds=&workdayIds=&educationIds=&segmentId=&contractTypeIds=&page=1&sortBy=RELEVANCE&onlyForeignCountry=false&countryIds=&sinceDate=ANY&salaryMin=6000&salaryPeriod=YEAR&salaryType=GROSS&subcategoryIds="

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the job listings on the page
job_listings = soup.find_all('li', class_='sui-AtomCard-layoutItem')

# Initialize an empty list to store the data
data = []

# Extract information from each job listing
for listing in job_listings:
    title = listing.find('a', class_='sui-LinkBasic sui-LinkBasic--blue job-item__title')['title']
    company = listing.find('span', class_='job-item__company').text.strip()
    location = listing.find('span', class_='job-item__location').text.strip()
    salary = listing.find('span', class_='job-item__salary').text.strip()

    data.append({
        'Title': title,
        'Company': company,
        'Location': location,
        'Salary': salary
    })

# Create a DataFrame from the collected data
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('infojobs_dataset.csv', index=False)