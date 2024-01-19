from selenium import webdriver
# from selenium.webdriver.firefox.service import Service as FFService

class RunFFTests():
    def test(self):
        try:
            # No need to specify executable_path
            driver = webdriver.Firefox()
            # ffservice = FFService()
            # driver = webdriver.Firefox(service=ffservice)

            # Open the URL
            driver.get("https://www.selenium.dev/")
        except Exception as e:
            # If an exception occurs, print an error message
            print(f"Error: {e}")
            print("GeckoDriver setup is not correct. Please check your setup.")


run_tests = RunFFTests()
run_tests.test()
