from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

profile = webdriver.FirefoxProfile()

proxy_ip = "50.232.250.157"
proxy_port = "8080"

profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.http", str(proxy_ip))
profile.set_preference("network.proxy.http_port", int(proxy_port))
profile.set_preference("network.proxy.ssl", str(proxy_ip))
profile.set_preference("network.proxy.ssl_port", int(proxy_port))
profile.set_preference("network.proxy.ftp", str(proxy_ip))
profile.set_preference("network.proxy.ftp_port", int(proxy_port))
profile.set_preference("network.proxy.socks", str(proxy_ip))
profile.set_preference("network.proxy.socks_port", int(proxy_port))

profile.update_preferences()

driver = webdriver.Firefox(firefox_profile=profile)

driver.get("https://ifconfig.me")

driver.quit()
