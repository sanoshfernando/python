import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# URL to monitor
URL = "https://www.jobsatamazon.co.uk/app#/jobSearch"

# Keep track of seen jobs
seen_jobs = set()

def check_jobs(driver):
    driver.get(URL)
    time.sleep(5)  # wait for jobs to load (adjust if needed)

    # ⬇️ Replace with the correct selectors from Inspect Element
    jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-selector")

    if not jobs:
        print("No job found")
        return

    found_new = False
    for job in jobs:
        try:
            title_el = job.find_element(By.CSS_SELECTOR, ".job-title-selector")
            location_el = job.find_element(By.CSS_SELECTOR, ".job-location-selector")
            link_el = job.find_element(By.TAG_NAME, "a")

            title = title_el.text.strip()
            location = location_el.text.strip()
            link = link_el.get_attribute("href")

            job_id = f"{title}|{location}|{link}"

            if job_id not in seen_jobs:
                seen_jobs.add(job_id)
                found_new = True
                print(f"New Job Found: {title} – {location}\n{link}\n")

        except Exception as e:
            print(f"Error reading job card: {e}")
            continue

    if not found_new:
        print("No new jobs found")

def main():
    options = Options()
    options.add_argument("--headless")  # run without browser window
    service = Service("C:/path/to/chromedriver.exe")  # <-- update path
    driver = webdriver.Chrome(service=service, options=options)

    try:
        while True:
            check_jobs(driver)
            time.sleep(900)  # check every 15 minutes
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
