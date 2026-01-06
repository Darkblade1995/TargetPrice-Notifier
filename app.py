import time
import schedule
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class PriceMonitor:
    def __init__(self, url, target_price):
        self.url = url
        self.target_price = target_price

    def get_price(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless") 
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        try:
            driver.get(self.url)
            time.sleep(5)  

            price_element = driver.find_element(By.CLASS_NAME, "andes-money-amount__fraction")
            
            if not price_element:
                print("Price not found on screen")
                return None
            
            price_text = price_element.text.strip()
            
            price = float(price_text.replace('.', '').replace(',', ''))
            
            driver.quit() 
            return price
        
        except Exception as e:
            print(f"Error fetching price: {e}")
            driver.quit()
            return None

    def check_price(self):
        current_price = self.get_price()
        if current_price:
            if current_price <= self.target_price:
                print("!!! PRICE ALERT !!!")   
                print(f"Current price: ${current_price}") 
                print(f"Target price: ${self.target_price}")
                print("! IT IS TIME TO BUY !")
                return True
            else:
                print(f"Current price: ${current_price} - Still hasn't dropped")
        return False

    def monitor(self):
        print(f"Monitoring: {self.url}")
        print("Performing first check...")
        self.check_price()

        schedule.every().day.at("09:00").do(self.check_price)
        # schedule.every(1).minutes.do(self.check_price)

        while True:
            schedule.run_pending()
            time.sleep(60)

if __name__ == "__main__":
    monitor = PriceMonitor(
        url="https://www.mercadolibre.com.co/apple-macbook-air-13-pulgadas-2020-chip-m1-256-gb-de-ssd-gris-espacial/p/MCO17828518",
        target_price=5000000
    )
    monitor.monitor()



