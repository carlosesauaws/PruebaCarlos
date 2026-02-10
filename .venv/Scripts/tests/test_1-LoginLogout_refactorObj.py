   
    #-------------------------------------------------------------------------------
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
from bibliotecaObjetos.loginPage import LoginPage
import pytest_playwright
import pytest

@pytest.mark.refactor
def test_login_exitoso():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Instanciamos nuestra biblioteca/página
        login_pg = LoginPage(page)
        
        # Llamamos a los elementos o métodos
        login_pg.navigate()
        login_pg.objCapturaCodigo.fill("UXTY789@!!1")
        login_pg.objBotonLogin.click()
        page.wait_for_timeout(10000)

        # Aserción de login
        expect(login_pg.page).to_have_url("https://candidates-qa.contalink.com/")
        page.wait_for_timeout(5000)
        login_pg.objBotonLogout.click()
        page.wait_for_timeout(5000)
        browser.close()
            
