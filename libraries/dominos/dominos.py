from libraries.common import log_message, files, capture_page_screenshot
from config import OUTPUT_FOLDER, tabs_dict
import os, time
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
import SeleniumLibrary.errors

class Dominos():

    def __init__(self, rpa_selenium_instance, credentials:dict):
        self.browser = rpa_selenium_instance
        self.dominos_url = credentials["url"]
        self.order_information = []

    def access_dominos(self):
        """
        Access the Dominos page from the browser
        """
        log_message("Start - Access Dominos.pe")
        self.browser.go_to(self.dominos_url)
        log_message("End - Access Dominos.pe")

    def go_to_order_online(self):
        """
        Open the section for ordering online
        """
        log_message("Start - Go to Order Online")
        try:
            self.browser.wait_until_element_is_visible('//a[text()="Ordena en línea"]', timeout=timedelta(seconds=1))
            self.browser.click_element('//a[text()="Ordena en línea"]')

            self.browser.wait_until_element_is_visible('//span[contains(text(),"Entrega a Domicilio")]', timeout=timedelta(seconds=2))
            self.browser.click_element('//span[contains(text(),"Entrega a Domicilio")]')

            self.browser.wait_until_element_is_visible('//label[contains(text(),"Tipo de Dirección")]', timeout=timedelta(seconds=2))
            self.browser.click_element('//select/option[@value="House"]')
            self.browser.wait_until_element_is_visible('//select/option[@value="Lima"]', timeout=timedelta(seconds=2))
            self.browser.click_element('//select/option[@value="Lima"]')
            self.browser.wait_until_element_is_visible('//select/option[@value="Santiago de Surco"]', timeout=timedelta(seconds=2))
            self.browser.click_element('//select/option[@value="Santiago de Surco"]')
            self.browser.input_text_when_element_is_visible('//input[@id="StreetName"]', "Av. Primavera 1805")
            self.browser.input_text_when_element_is_visible('//input[@id="StreetNumber"]', "150")
            self.browser.input_text_when_element_is_visible('//textarea[@id="Delivery_Instructions"]', "Prueba")
            self.browser.click_element('//button[contains(text(), "Continuar")]')            
        except SeleniumLibrary.errors.ElementNotFound as ex:
            log_message(str(ex)) 
            raise Exception(str(ex))

        log_message("End - Go to Order Online")

    def create_the_pepperoni_pizza(self):
        """
        Select the pepperoni pizza to customize
        """
        log_message("Start - Create the pepperoni pizza")
        try:
            self.browser.wait_until_element_is_visible('//h1[contains(text(), "Menú")]', timeout=timedelta(seconds=2))
            self.browser.click_element('//a[contains(text(), "Pizzas")]')
            
            self.browser.wait_until_element_is_visible('//h1[contains(text(), "Pizza")]', timeout=timedelta(seconds=2))
            self.browser.click_element('//a[contains(text(), "Pizzas")]')

            pepperoni_pizza = self.browser.find_element('//div[contains(@data-dpz-track-group,"Pizza")][descendant::a[contains(text(), "Pepperoni")]]')
            customize_pepperoni = self.browser.find_element('xpath:.//a[contains(text(), "PERSONALIZAR")]', parent=pepperoni_pizza)
            self.browser.click_element(customize_pepperoni)
        except SeleniumLibrary.errors.ElementNotFound as ex:
            log_message(str(ex)) 
            raise Exception(str(ex))
        log_message("End - Create the pepperoni pizza")

    def customize_the_pizza(self):
        """
        Select the preferences for the pizza
        """
        log_message("Start - Customize the pizza")
        try:
            self.browser.wait_until_element_is_visible('//span[contains(text(), "Gigante")]', timeout=timedelta(seconds=2))
            self.browser.click_element('//span[contains(text(), "Gigante")]')
            self.browser.click_element('//label[contains(@for, "15")]/span[contains(text(), "Italiana")]')
            self.browser.click_element('//button[contains(text(), "Queso y Salsa")]')

            self.browser.wait_until_element_is_visible('//select[contains(@aria-label, "Cheese")]/option[contains(text(),"Extra")]', timeout=timedelta(seconds=3))
            self.browser.click_element('//select[contains(@aria-label, "Cheese")]/option[contains(text(),"Extra")]')
            self.browser.click_element('//select[contains(@aria-label, "Salsa de tomate")]/option[contains(text(),"Extra")]')
            self.browser.click_element('//button[contains(text(), "Ingredientes")]')

            self.browser.wait_until_element_is_visible('//h2[contains(text(), "Procede a ingresar")]', timeout=timedelta(seconds=3))
            self.browser.click_element('//span[contains(text(),"Carne Molida")]')
            self.browser.click_element('//span[contains(text(),"Tocino")]')
            self.browser.click_element('//span[contains(text(),"Cheddar")]')
            self.browser.click_element('//span[contains(text(),"Piña")]')

            self.browser.click_element('//select[contains(@aria-label, "Carne")]/option[contains(text(),"Extra")]')
            self.browser.click_element('//select[contains(@aria-label, "Tocino")]/option[contains(text(),"Extra")]')
            self.browser.click_element('//select[contains(@aria-label, "Pepperoni")]/option[contains(text(),"Extra")]')
            self.browser.click_element('//select[contains(@aria-label, "Mozzarella")]/option[contains(text(),"Extra")]')
            self.browser.click_element('//select[contains(@aria-label, "Salsa")]/option[contains(text(),"Extra")]')
            self.browser.click_element('//select[contains(@aria-label, "Cheddar")]/option[contains(text(),"Extra")]')
            self.browser.click_element('//select[contains(@aria-label, "Piña")]/option[contains(text(),"Extra")]')

            self.browser.click_element('//select[contains(@aria-label, "Cantidad")]/option[@value="2"]')
            self.browser.click_element('//button[contains(text(), "Agregar a la Orden")]')

        except SeleniumLibrary.errors.ElementNotFound as ex:
            log_message(str(ex)) 
            raise Exception(str(ex))
        log_message("End - Customize the pizza")

    def finish_the_order(self):
        """
        Select the add-ons for the order
        """
        log_message("Start - Finish the order")
        try:
            self.browser.wait_until_element_is_visible('//span[contains(text(), "Carrito")]', timeout=timedelta(seconds=2))
            self.browser.click_element('//span[contains(text(), "Carrito")]')
            self.browser.wait_until_element_is_visible('//span[contains(text(), "S/.")]', timeout=timedelta(seconds=5))
            self.browser.click_element('//button[@data-dpz-track-evt-name="Continuar"]')
            self.browser.wait_until_element_is_visible('//h1[contains(text(),"También te puede gustar")]', timeout=timedelta(seconds=2))
            self.browser.click_element('//a[contains(text(),"Checkout")]')
            
            self.browser.wait_until_element_is_visible('//h3[contains(text(),"paso 2")]', timeout=timedelta(seconds=2))
            self.browser.click_element('//button[contains(@data-quid,"COKE")]')

            self.browser.wait_until_element_is_visible('//h1[contains(text(),"Coca")]', timeout=timedelta(seconds=2))
            self.browser.click_element('//button[@data-quid="generic-quantity-increment"]')
            coke_amount = self.browser.find_element('//div[@class="quantity__label"]').text
            if(coke_amount=="2"):
                self.browser.click_element('//button[contains(text(),"Agregar a la Orden")]')  
            else:
                self.browser.click_element('//button[@data-quid="generic-quantity-increment"]')

            self.browser.wait_until_element_is_visible('//div[contains(@data-dpz-track-group,"upsell")]', timeout=timedelta(seconds=5))
            cheesy_bread = self.browser.find_element('//div[contains(@data-dpz-track-group,"upsell")][descendant::a[contains(@data-dpz-track-evt-name,"Cheesy Cheese Bread")]]')
            order_cheesy_bread = self.browser.find_element('xpath:./a', parent=cheesy_bread)
            self.browser.click_element(order_cheesy_bread)  
            self.browser.wait_until_element_is_visible('//h1[contains(text(),"Cheesy")]', timeout=timedelta(seconds=2))
            self.browser.click_element('//button[@data-quid="generic-quantity-increment"]')
            cheesy_amount = self.browser.find_element('//div[@class="quantity__label"]').text
            if(cheesy_amount=="2"):
                self.browser.click_element('//button[contains(text(),"Agregar a la Orden")]')  
            else:
                self.browser.click_element('//button[@data-quid="generic-quantity-increment"]')
            time.sleep(3)
            self.browser.wait_until_element_is_visible('//a[contains(text(),"Finalizar")]', timeout=timedelta(seconds=5))
            self.browser.click_element('//a[contains(text(),"Finalizar")]')

        except SeleniumLibrary.errors.ElementNotFound as ex:
            log_message(str(ex)) 
            raise Exception(str(ex))
        log_message("End - Finish the order")

    def get_order_information(self):
        """
        Gets the information from the order
        """
        log_message("Start - Get Order Information")
        try:
            self.browser.wait_until_element_is_visible('//span[contains(text(),"Ver resumen")]', timeout=timedelta(seconds=5))
            self.browser.click_element('//span[contains(text(),"Ver resumen")]')
            element_names = self.browser.find_elements('//h3[@class="order-summary__item__title"]')
            element_quantities = self.browser.find_elements('//td[@class="qty"]')
            element_prices = self.browser.find_elements('//td[@class="price"]')
            for name, quantity, price in zip(element_names,element_quantities,element_prices):
                self.order_information.append({"Element":name.text, "Amount":quantity.text, "Price":price.text})
            #print(self.order_information)
            
        except SeleniumLibrary.errors.ElementNotFound as ex:
            log_message(str(ex)) 
            raise Exception(str(ex))             
        log_message("End - Get Order Information")

    def create_excel(self):
        """
        Create the Excel file with the information
        """
        log_message("Start - Create Excel")
        files.create_workbook(path = "{}/Pizza.xlsx".format(OUTPUT_FOLDER))
        files.create_worksheet(name = "Pizza Order", content= None, exist_ok = True, header = False)
        files.append_rows_to_worksheet(self.order_information, name = "Pizza Order", header = True, start= None)
        files.remove_worksheet(name = "Sheet")
        files.save_workbook(path = None)
        files.close_workbook()
        log_message("End - Create Excel")

    def set_billing_information(self):
        """
        Set the information for the payment
        """
        log_message("Start - Set Billing Information")
        
        try:
            self.browser.input_text_when_element_is_visible('//input[@id="First_Name"]', "Enrique")
            self.browser.input_text_when_element_is_visible('//input[@id="Last_Name"]', "Gatica")
            self.browser.input_text_when_element_is_visible('//input[@id="Email"]', "egatica@thefunctionary.com")
            self.browser.input_text_when_element_is_visible('//input[@id="Callback_Phone"]', "123456789")
            self.browser.click_element('//input[@id="Agree_To_Terms_Of_Use"]')
            self.browser.input_text_when_element_is_visible('//textarea[@id="Delivery_Instructions"]', "prueba")
        
            self.browser.input_text_when_element_is_visible('//input[@id="InvoiceTaxID"]', "70001254")
            self.browser.input_text_when_element_is_visible('//input[@id="InvoiceName"]', "Enrique Gatica")
        
            self.browser.click_element('//input[@id="DoorCredit"]')
            self.browser.wait_until_element_is_visible('//select[@name="CardCreditTypeDelivery"]', timeout=timedelta(seconds=2))
            self.browser.click_element('//select[@name="CardCreditTypeDelivery"]/option[@value="Visa"]')
            capture_page_screenshot(OUTPUT_FOLDER,"Pizza_Form")
        except SeleniumLibrary.errors.ElementNotFound as ex:
            log_message(str(ex)) 
            raise Exception(str(ex))  
        finally:
            time.sleep(5)


        log_message("End - Set Billing Information")