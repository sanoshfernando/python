import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from playsound import playsound  # pip install playsound

# Path to a sound file (mp3 or wav). You can change this to any sound you like.
ALERT_SOUND = "alert.mp3"


def check_jobs(driver):
    # Refresh the page first
    driver.refresh()
    print("🔄 Page refreshed")

    wait = WebDriverWait(driver, 30)
    try:
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".jobDetailText")))
    except:
        print("⚠️ No job cards rendered (timeout).")
        return

    job_cards = driver.find_elements(By.CSS_SELECTOR, "[data-test-id='JobCard']")

    if not job_cards:
        print("❌ No job found")
    else:
        print(f"✅ Found {len(job_cards)} job(s)")
        # Play sound alert
        playsound(ALERT_SOUND)
        for idx, job in enumerate(job_cards, 1):
            try:
                title = job.find_element(By.CSS_SELECTOR, ".jobDetailText strong").text
            except:
                title = "N/A"
            print(f"Job #{idx} - {title}")


def main():
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Open the Amazon jobs page initially
    driver.get("https://www.jobsatamazon.co.uk/app#/jobSearch")
    print("🔎 Watching Amazon Jobs page... (refreshes every 10 minutes)")

    try:
        while True:
            check_jobs(driver)
            print("⏳ Waiting 10 minutes before next check...")
            time.sleep(600)  # 10 minutes
    except KeyboardInterrupt:
        print("🛑 Stopping watcher...")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
