# main.py - Punto de entrada principal de la aplicación Floodly

import customtkinter as ctk
from views.splash import SplashScreen

def main():
    """
    Función principal que inicia la aplicación Floodly.
    Comienza con la pantalla de splash.
    """
    # Configurar tema oscuro por defecto
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    
    # Crear ventana principal
    app = ctk.CTk()
    app.withdraw()  # Ocultar ventana principal inicialmente
    
    # Mostrar splash screen
    splash = SplashScreen(app)
    app.mainloop()

if __name__ == "__main__":
    main()
