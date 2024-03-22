from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
# Inisialisasi service dengan EdgeChromiumDriverManager
service = Service(EdgeChromiumDriverManager().install())

# Inisialisasi Edge driver dengan service yang telah ditentukan
driver = webdriver.Edge(service=service)

# URL yang ingin Anda buka di browser
url = "https://github.com/lendral3n"

# Waktu delay antara setiap refresh (dalam detik)
delay = 3  # contoh: 60 detik (1 menit)

# Buka URL di browser Edge
driver.get(url)

# Fungsi untuk merefresh browser secara otomatis
def refresh_browser(driver, url, delay):
    while True:
        # Refresh tab yang sudah ada
        driver.refresh()

        # Tunggu sebelum merefresh kembali
        time.sleep(delay)

# Panggil fungsi untuk memulai merefresh browser secara otomatis
refresh_browser(driver, url, delay)
