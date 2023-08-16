import requests
from bs4 import BeautifulSoup

def get_jobs(search_query):
    base_url = "https://example.com/jobs"  # Replace with the actual job search website URL
    params = {"q": search_query}

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        job_listings = soup.find_all("div", class_="job-listing")  # Adjust the class name based on the website's structure

        jobs = []
        for job in job_listings:
            title = job.find("h2").text.strip()
            company = job.find("span", class_="company").text.strip()
            location = job.find("span", class_="location").text.strip()
            link = job.find("a")["href"]
            jobs.append({"title": title, "company": company, "location": location, "link": link})

        return jobs
    else:
        print("Failed to retrieve job listings.")

if __name__ == "__main__":
    search_query = input("Enter job search query: ")
    jobs = get_jobs(search_query)
    
    if jobs:
        for job in jobs:
            print(f"Title: {job['title']}")
            print(f"Company: {job['company']}")
            print(f"Location: {job['location']}")
            print(f"Link: {job['link']}")
            print("-" * 30)
    else:
        print("No jobs found.")
