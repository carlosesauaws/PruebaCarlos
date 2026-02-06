import pytest
import re
from playwright.sync_api import Page, expect
from datetime import date
from datetime import datetime
from playwright.sync_api import sync_playwright

@pytest.mark.contalink

def test_nueva_factura(page: Page):
    page.goto("https://candidates-qa.contalink.com/")

    #Se identifica el cuadro de texto y se manda el codigo
    capturacodigo = page.locator("//*[@id='access-code']")
    capturacodigo.fill("UXTY789@!!1")

    #Se identifica el boton login y se da click
    botonlogin = page.get_by_text("Validar Código").click()

    #Se identifica el boton para agregar factura
    botonfacturanueva = page.get_by_text("Nueva Factura").click()

    #Definir Num de Factura a capturar
    hoy = date.today()
    hora = datetime.now()
    idparafactura = str(hoy.year) + str(hoy.month) + str(hoy.day) + str(hora.hour) + str(hora.minute) + str(hora.second)
    print(idparafactura)

    #Identificar y llenar los elementos de la nueva factura
    numerofacturanueva = page.locator("//*[@id='invoiceNumber']").fill(idparafactura)
    totalfacturanueva = page.locator("//*[@id='total']").fill("50.00")
    estadofacturanueva = page.locator("//*[@id='status']").select_option("Vencido")
    botoncrearfactura = page.get_by_text("Crear Factura").click()
    page.wait_for_timeout(5000)


    #Consultar si la nueva factura se creo correctamente
    capturafactura = page.locator("//*[@id='invoiceName']")
    capturafactura.fill(idparafactura)
    botonconsultafactura = page.get_by_role("button", name="Buscar").click()

    # Ubicar el resultado de la busqueda
    tabla = page.get_by_role("table.table.table-zebra")
    fila = page.locator("tbody tr")
    idfacturaagregada = fila.locator("td").nth(0).inner_text()


    # assert idfacturaagregada == idparafactura
    if idfacturaagregada != idparafactura:
        pytest.fail("Factura incorrecta")
    print("factura correcta")

    #Atrapar el prompt
    page.on("dialog", lambda dialog: dialog.accept(prompt_text="¿Estás seguro de que deseas eliminar esta factura?"))


    #Eliminar la factura previamente agregada
    accionesfactura = fila.locator("td").nth(4)
    botoneliminarfactura = accionesfactura.get_by_role("button", name="Eliminar factura").click()
    # Confirma el prompt
    expect(page.locator("#output")).to_have_text("¿Estás seguro de que deseas eliminar esta factura?")

    botonpopup = driver.find_element(By.ID, "button-id")
    page.execute_script("arguments[0].click();", botonpopup)

    page.wait_for_timeout(5000)





    #assert idfacturaagregada == idparafactura

    # Ubicar el resultado de la busqueda


    #assert (cantidadlimpia + 1) == cantidadfacturaactualizada
    #botonconsultafactura.click()



