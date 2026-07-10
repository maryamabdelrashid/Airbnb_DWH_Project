import pandas as pd
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("Starting the detailed scraper...")

chrome_options = Options()
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

cities = ['Amsterdam', 'Athens', 'Barcelona', 'Berlin', 'Budapest', 'Lisbon', 'London', 'Paris', 'Rome', 'Vienna']
all_data = []

for city in cities:
    print(f"\n[City: {city}] Collecting links...")
    
    url = f"https://www.airbnb.com/s/{city}/homes?room_types[]=Entire%20home%2Fapt&min_bedrooms=2"
    driver.get(url)
    time.sleep(random.uniform(5, 8))

    try:
        driver.find_element(By.XPATH, "//button[contains(., 'Got it')]").click()
        time.sleep(1)
    except: 
        pass

    try:
        driver.find_element(By.CSS_SELECTOR, "button[aria-label='Close']").click()
        time.sleep(1)
    except: 
        pass

    property_links = []
    
    while len(property_links) < 50:
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[itemprop='itemListElement']")))
            listings = driver.find_elements(By.CSS_SELECTOR, "div[itemprop='itemListElement']")
            
            for listing in listings:
                try:
                    href = listing.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                    if href and "/rooms/" in href and href not in property_links:
                        property_links.append(href)
                    if len(property_links) >= 50:
                        break
                except:
                    continue
            
            if len(property_links) < 50:
                next_btn = driver.find_element(By.CSS_SELECTOR, "a[aria-label='Next']")
                driver.execute_script("arguments[0].click();", next_btn)
                time.sleep(random.uniform(4, 7))
        except Exception:
            print("No more pages or Next button not found.")
            break
            
    print(f"Collected {len(property_links)} links. Extracting details...")

    for idx, link in enumerate(property_links):
        print(f"Visiting property {idx+1}/{len(property_links)}...")
        driver.get(link)
        time.sleep(random.uniform(3, 5)) 
        
        try:
            try:
                driver.find_element(By.CSS_SELECTOR, "button[aria-label='Close']").click()
                time.sleep(0.5)
            except: 
                pass

            try:
                name = driver.find_element(By.TAG_NAME, "h1").text
            except:
                name = "N/A"
                
            try:
                price_elements = driver.find_elements(By.XPATH, "//span[contains(text(), 'ج.م') or contains(text(), '$') or contains(text(), '€')]")
                price = price_elements[0].text if price_elements else "N/A"
            except:
                price = "N/A"
                
            rating = "N/A"
            reviews_count = "0"
            try:
                review_elements = driver.find_elements(By.XPATH, "//div[contains(text(), 'reviews') or contains(text(), 'review')]")
                if review_elements:
                    reviews_text = review_elements[0].text 
                    if '·' in reviews_text:
                        rating = reviews_text.split('·')[0].strip()
                        reviews_count = reviews_text.split('·')[1].strip()
                    else:
                        rating = reviews_text
            except:
                pass
                
            try:
                superhost_elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'Superhost')]")
                superhost = "Yes" if len(superhost_elements) > 0 else "No"
            except:
                superhost = "No"
                
            try:
                guest_fav_elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'Guest favorite')]")
                guest_favorite = "Yes" if len(guest_fav_elements) > 0 else "No"
            except:
                guest_favorite = "No"

            all_data.append({
    "City": city,
    "Name": name,
    "Price": price,
    "Rating": rating,
    "Reviews_Count": reviews_count,
    "Superhost": superhost,
    "Guest_Favorite": guest_favorite,
    "Link": link
})
        
            
        except Exception:
            print("Failed to extract data for this property. Skipping.")
            continue

print("\nScraping complete. Saving to CSV...")
df = pd.DataFrame(all_data)
df.to_csv("airbnb_detailed_500_apartments.csv", index=False, encoding='utf-8-sig')
driver.quit()

print("Task finished. Data saved in airbnb_detailed_500_apartments.csv")
