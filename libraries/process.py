from libraries.common import log_message, capture_page_screenshot, browser
from config import OUTPUT_FOLDER, tabs_dict
from libraries.dominos.dominos import Dominos

class Process():
    
    def __init__(self, credentials: dict):
        log_message("Initialization")

        prefs = {
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_setting_popups": 0,
            "directory_upgrade": True,
            "download.default_directory": OUTPUT_FOLDER,
            "plugins.always_open_pdf_externally": True,
            "download.prompt_for_download": False
        }

        browser.open_available_browser(preferences = prefs)
        browser.set_window_size(1920, 1080)
        browser.maximize_browser_window()

        dominos = Dominos(browser, {"url": "https://www.dominos.com.pe/es/"})
        tabs_dict["Dominos"] = len(tabs_dict)
        dominos.access_dominos()
        self.dominos = dominos

    def start(self):
        """
        main
        """

        self.dominos.go_to_order_online()
        self.dominos.create_the_pepperoni_pizza()
        self.dominos.customize_the_pizza()
        self.dominos.finish_the_order()
        self.dominos.get_order_information()
        self.dominos.create_excel()
        self.dominos.set_billing_information()
    
    def finish(self):
        log_message("DW Process Finished")
        browser.close_browser()