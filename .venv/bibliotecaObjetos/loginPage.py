###############################################################################################################
#--------------------------------------------------------------------------------------------------------------
from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        # --- Biblioteca de Elementos (Locators) ---
        self.objCapturaCodigo = page.locator("//*[@id='access-code']")
        self.objBotonLogin = page.get_by_text("Validar Código")
        self.objBotonLogout = page.get_by_role("button", name="Cerrar Sesión")

    # --- Acciones (Métodos) ---
    def navigate(self):
        self.page.goto("https://candidates-qa.contalink.com/")

    #def login(self, user, password):
    #    self.objCapturaCodigo.fill("UXTY789@!!1")
    #    self.objBotonLogin.click()