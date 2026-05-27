from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_end_to_end_purchase(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_item_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_info("Joao", "Silva", "12345")
    
    # Espera a página de overview carregar
    wait = WebDriverWait(driver, 5)
    wait.until(EC.url_contains("checkout-step-two"))
    
    checkout_page.finish_order()

    msg = checkout_page.get_success_message()
    assert "Thank you for your order" in msg