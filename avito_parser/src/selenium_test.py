import undetected_chromedriver as uc
driver = uc.Chrome(browser_executable_path="/usr/lib/brave-browser/brave-browser")
driver.get('https://nowsecure.nl')
driver.save_screenshot('nowsecure.png')
