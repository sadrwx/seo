import time, random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait(min_sec, max_sec):
    time.sleep(random.uniform(min_sec, max_sec))

def run_search():
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:114.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36; Mobile Safari/537.36"
    )

    service = Service("/home/om/chromedriver/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get("https://www.google.com")
        wait(1.5, 3)

        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("تعمیرات تجهیزات ازمایشگاهی راستین ازما")
        wait(0.8, 1.5)
        search_box.send_keys(Keys.RETURN)
        wait(1.5, 3)

        target_url = "https://rastinazma-co.ir"

        links = driver.find_elements(By.CSS_SELECTOR, "a[href]")
        for link in links:
            try:
                href = link.get_attribute("href")
                if target_url in href:
                    link.click()
                    print(f"🚀 کلیک شد روی: {href}")
                    wait(3, 4.5)

                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.TAG_NAME, "body"))
                    )

                    for _ in range(random.randint(3, 4)):
                        driver.execute_script(f"window.scrollBy(0, {random.randint(800, 1200)})")
                        wait(0.8, 1.5)

                    if random.random() > 0.5:
                        x = random.randint(200, 1200)
                        y = random.randint(300, 1500)
                        driver.execute_script(f"window.scrollTo({x}, {y});")
                        print("🖱️ حرکت موس به موقعیت تصادفی")
                        wait(0.4, 0.8)

                    print("🚪 بستن مرورگر پس از اتمام کار")
                    break  # لینک پیدا شد، از حلقه خارج شو
            except Exception as e:
                print(f"❌ خطا در کلیک روی لینک: {e}")
    finally:
        driver.quit()  # مرورگر همیشه بسته شود حتی اگر خطا رخ دهد

# اجرای تابع
run_search()

