import pytest
from playwright.sync_api import Page, expect
@pytest.mark.contalink

def test_consulta_factura_existente(page: Page):
    page.goto("https://candidates-qa.contalink.com/")

    #Se identifica el cuadro de texto y se manda el codigo
    capturacodigo = page.locator("//*[@id='access-code']")
    capturacodigo.fill("UXTY789@!!1")

    #Se identifica el boton login y se da click
    botonlogin = page.get_by_text("Validar Código").click()

    #Se identifica el cuadro de texto de busqueda y se envia el valor de la consulta (Id de Factura 447046)
    capturafactura = page.locator("//*[@id='invoiceName']")
    capturafactura.fill("447046")
    botonconsultafactura = page.get_by_role("button", name="Buscar").click()

    #Ubicar el resultado de la busqueda
    tabla = page.get_by_role("table.table.table-zebra")
    fila = page.locator("tbody tr")
    idfactura = fila.locator("td").nth(0).inner_text()

    print(idfactura)
    assert idfactura == "447046"

    #page.wait_for_timeout(3000)





    #botonconsultafactura.click()



