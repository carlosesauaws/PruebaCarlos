import pytest
from playwright.sync_api import Page

@pytest.mark.contalink
def test_login_logout(page: Page):
    page.goto("https://candidates-qa.contalink.com/")

    #Se identifica el cuadro de texto y se manda el codigo
    capturacodigo = page.locator("//*[@id='access-code']")
    capturacodigo.fill("UXTY789@!!1")

    #Se identifica el boton login y se da click
    botonlogin = page.get_by_text("Validar Código").click()

    #Se identifica el boton logout y se da click
    #botonlogout = page.get_by_text("Cerrar Sesión").click()

    botonlogout = page.get_by_role("button", name="Cerrar Sesión").click()
    page.wait_for_timeout(3000)

