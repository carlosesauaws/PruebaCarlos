import pytest
from playwright.sync_api import Page, expect
@pytest.mark.contalink

def test_consulta_factura_por_estatus(page: Page):
    page.goto("https://candidates-qa.contalink.com/")

    #Se identifica el cuadro de texto y se manda el codigo
    capturacodigo = page.locator("//*[@id='access-code']")
    capturacodigo.fill("UXTY789@!!1")

    #Se identifica el boton login y se da click
    botonlogin = page.get_by_text("Validar Código").click()

    #Se identifica el cuadro de texto de busqueda y se envia el valor de la consulta (Id de Factura 447046)
    capturaestado = page.locator("//*[@id='status']")
    capturaestado.select_option("Vencido")
    botonconsultafactura = page.get_by_role("button", name="Buscar").click()

    #Ubicar el resultado de la busqueda
    tabla = page.get_by_role("table.table.table-zebra")
    fila = page.locator("tbody tr")
    estadofactura = fila.locator("td").nth(3).inner_text()

    print(estadofactura)
    assert estadofactura == "Vencido"

    #page.wait_for_timeout(3000)





    #botonconsultafactura.click()



