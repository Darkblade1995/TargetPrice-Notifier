# TargetPrice-Notifier 🦅

**TargetPrice-Notifier** is a robust Python-based price monitoring tool designed specifically for Mercado Libre. It automates the process of checking product prices and alerts you the exact moment they hit your target budget.

## 🚀 Why this exists?
Traditional web scrapers often fail on major e-commerce sites because they are easily detected as bots. **MercadoScout** overcomes these hurdles by using **Selenium WebDriver** to simulate real human browsing behavior, bypassing anti-bot protections and rendering JavaScript content.

## ✨ Key Features
* **Anti-Bot Bypass**: Uses custom User-Agents and Selenium to avoid security blocks.
* **Dynamic Content Support**: Correctly renders prices loaded via JavaScript.
* **Automated Scheduling**: Checks prices daily at 09:00 AM.
* **Headless Mode**: Runs in the background without opening a visible browser window.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Automation:** Selenium WebDriver
* **Driver Management:** Webdriver Manager
* **Scheduling:** Schedule library

## 📋 Prerequisites
Install the following libraries in your terminal:
```bash
pip install selenium webdriver-manager schedule
🏗️ How it Works
Browser Emulation: Launches a headless Chrome instance.

Wait & Load: Waits 5 seconds for dynamic price elements to appear.

Data Extraction: Locates the price using stable CSS classes.

Comparison: Triggers an alert if the price is <= your target.

👤 Author
Luis Fernando Agamez

LinkedIn:https://www.linkedin.com/in/luis-fernando-agamez-44383b267/

GitHub: https://github.com/Darkblade1995