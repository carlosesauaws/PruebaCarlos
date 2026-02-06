import pytest
from playwright.sync_api import Page, expect
@pytest.mark.contalink

def test_consulta_factura_eliminada(page: Page):
    page.goto("https://candidates-qa.contalink.com/")

    #Se identifica el cuadro de texto y se manda el codigo
    capturacodigo = page.locator("//*[@id='access-code']")
    capturacodigo.fill("UXTY789@!!1")

    #Se identifica el boton login y se da click
    botonlogin = page.get_by_text("Validar Código").click()

    #Se marca el checkbox de incluir eliminadas
    checkeliminadas = page.locator("//*[@id='showDeleted']")
    checkeliminadas.click()

    #Se identifica el cuadro de texto de busqueda y se envia el valor de la consulta
    capturaestado = page.locator("//*[@id='status']")
    capturaestado.select_option("Vencido")
    botonconsultafactura = page.get_by_role("button", name="Buscar").click()

    #Ubicar el resultado de la busqueda
    tabla = page.get_by_role("table.table.table-zebra")
    fila = page.locator("tbody tr")
    isEliminada = fila.locator("td").nth(4).inner_text()

    print(isEliminada)
    assert isEliminada == "Eliminada"




