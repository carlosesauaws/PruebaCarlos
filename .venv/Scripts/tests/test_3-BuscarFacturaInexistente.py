import pytest
from playwright.sync_api import Page, expect
@pytest.mark.contalink
def test_consulta_factura_inexistente(page: Page):
    page.goto("https://candidates-qa.contalink.com/")

    #Se identifica el cuadro de texto y se manda el codigo
    capturacodigo = page.locator("//*[@id='access-code']")
    capturacodigo.fill("UXTY789@!!1")

    #Se identifica el boton login y se da click
    botonlogin = page.get_by_text("Validar Código").click()

    #Se identifica el cuadro de texto de busqueda y se envia el valor de la consulta (Id de Factura 447046)
    capturafactura = page.locator("//*[@id='invoiceName']")
    capturafactura.fill("A998100")
    botonconsultafactura = page.get_by_role("button", name="Buscar").click()

    #Ubicar el resultado de la busqueda y comparar para resultado de la prueba
    tabla = page.locator("table.table-zebra")
    fila = tabla.locator("tbody tr")
    factura = fila.locator("td").nth(0).inner_text()

    print(factura)
    assert factura == "No se encontraron facturas"

    #page.wait_for_timeout(3000)





    #botonconsultafactura.click()



