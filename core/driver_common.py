from seleniumwire import webdriver

_driver = None

def get_driver():
	global _driver
	if _driver is None:
		chrome_options = webdriver.ChromeOptions()
		chrome_options.set_capability("goog:loggingPrefs", { "performance": "ALL", "browser": "ALL" })

		_driver = webdriver.Chrome( options = chrome_options )
		
	return _driver