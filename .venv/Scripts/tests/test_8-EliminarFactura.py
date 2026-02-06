import pytest
import re
from playwright.sync_api import Page, expect
@pytest.mark.contalink

def test_eliminar_factura(page: Page):
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
    page.wait_for_timeout(2000)
    #Ubicar el resultado de la busqueda
    tabla = page.get_by_role("table.table.table-zebra")
    fila = page.locator("tbody tr")
    accionesfactura = fila.locator("td").nth(4)

    botoneditarfactura = accionesfactura.get_by_role("button", name="Editar factura").click()
    #page.wait_for_timeout(5000)

    totalfactura = page.locator("//*[@name='total']")
    totalfactura.click()

    cantidadfactura = totalfactura.input_value()
    cantidadfacturaactualizada = float(cantidadfactura) + 1
    totalfactura.fill(str(cantidadfacturaactualizada))

    botonactualizafactura = page.get_by_text("Actualizar Factura").click()
    #page.wait_for_timeout(5000)

    #assert cantidadfacturaactualizada == "447046"
    #page.wait_for_timeout(5000)

    #Lee de nuevo la cantidad (ahora actualizada y la convierte en float)
    tabla = page.get_by_role("table.table.table-zebra")
    fila = page.locator("tbody tr")
    cantidadafter = fila.locator("td").nth(1).inner_text()

    ##Convertir cantidad after a numero limpio
    limpio = cantidadafter.strip()
    limpio = limpio.replace(",", "")
    limpio = re.sub(r'[^\d.]', '', limpio)
    cantidadlimpia = float(limpio)

    assert (cantidadlimpia + 1) == cantidadfacturaactualizada
    #botonconsultafactura.click()



