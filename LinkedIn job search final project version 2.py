import csv
import requests
from bs4 import BeautifulSoup

# Send an HTTP GET request to the webpage
url = "https://www.linkedin.com/jobs/search/?currentJobId=3648738004&geoId=105646813&location=Spain&refresh=true"
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find and extract the desired information
job_results = soup.find_all('li', class_='result-card')

# Create a CSV file and write headers
csv_file = open('job search results.csv', 'w', newline='')
writer = csv.writer(csv_file)
writer.writerow(['Title', 'Salary', 'Location', 'Experience'])

# Iterate over job results and write data to the CSV file
for job_result in job_results:
    # Extract job title
    title = job_result.find('h3', class_='base-search-card__title').text.strip()

    # Extract salary information
    salary_elem = job_result.find('span', class_='salary-text')
    salary = salary_elem.text.strip() if salary_elem else "Not specified"

    # Extract location
    location_elem = job_result.find('span', class_='job-result-card__location')
    location = location_elem.text.strip() if location_elem else "Not specified"

    # Extract experience level
    experience_elem = job_result.find('li', class_='job-result-card__listitem--experience')
    experience = experience_elem.text.strip() if experience_elem else "Not specified"

    # Write data to the CSV file
    writer.writerow([title, salary, location, experience])

# Close the CSV file
csv_file.close()