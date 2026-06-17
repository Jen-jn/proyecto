# dashboard.py - Panel principal del dashboard

import customtkinter as ctk
from views.home import HomeScreen
from views.safety_tips import SafetyTipsScreen
from views.critical_zones import CriticalZonesScreen
from views.reports import ReportsScreen
from views.alerts import AlertsScreen
from views.login import LoginScreen
from theme import PRIMARY_BLUE, SECONDARY_CYAN, BACKGROUND, TEXT_DARK, TEXT_LIGHT, CARD

class Dashboard:
    """
    Dashboard principal con navegación lateral.
    Controla todas las vistas de la aplicación.
    """
    
    def __init__(self, root):
        self.root = root
        self.root.title("Floodly - Dashboard")
        self.root.geometry("1400x850")
        self.root.resizable(False, False)
        self.center_window()
        self.root.configure(fg_color=BACKGROUND)
        
        # Crear frame principal con dos secciones
        main_container = ctk.CTkFrame(self.root, fg_color=BACKGROUND)
        main_container.pack(fill="both", expand=True)
        
        # Barra lateral
        self.sidebar = ctk.CTkFrame(main_container, fg_color=PRIMARY_BLUE, width=250)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)
        
        # Logo en sidebar
        logo_label = ctk.CTkLabel(
            self.sidebar,
            text="🌊 FLOODLY",
            font=("Helvetica", 18, "bold"),
            text_color="#FFFFFF"
        )
        logo_label.pack(pady=20)
        
        # Separador
        sep1 = ctk.CTkFrame(self.sidebar, height=2, fg_color=SECONDARY_CYAN)
        sep1.pack(fill="x", padx=20)
        
        # Botones de navegación
        self.home_btn = self.create_nav_button(
            self.sidebar,
            "🏠 Inicio",
            self.show_home
        )
        
        self.safety_btn = self.create_nav_button(
            self.sidebar,
            "💡 Consejos",
            self.show_safety_tips
        )
        
        self.zones_btn = self.create_nav_button(
            self.sidebar,
            "🗺️ Zonas Críticas",
            self.show_critical_zones
        )
        
        self.reports_btn = self.create_nav_button(
            self.sidebar,
            "📋 Reportes",
            self.show_reports
        )
        
        self.alerts_btn = self.create_nav_button(
            self.sidebar,
            "🔔 Alertas",
            self.show_alerts
        )
        
        self.settings_btn = self.create_nav_button(
            self.sidebar,
            "⚙️ Configuración",
            self.show_settings
        )
        
        # Separador inferior
        sep2 = ctk.CTkFrame(self.sidebar, height=2, fg_color=SECONDARY_CYAN)
        sep2.pack(fill="x", padx=20, pady=(20, 0), side="bottom")
        
        # Botón cerrar sesión
        logout_btn = self.create_nav_button(
            self.sidebar,
            "🚪 Cerrar sesión",
            self.logout,
            color="#FF3B30"
        )
        logout_btn.pack(side="bottom", fill="x", padx=10, pady=10)
        
        # Área de contenido
        self.content_frame = ctk.CTkFrame(main_container, fg_color=BACKGROUND)
        self.content_frame.pack(side="right", fill="both", expand=True)
        
        # Mostrar pantalla de inicio por defecto
        self.show_home()
    
    def create_nav_button(self, parent, text, command, color=PRIMARY_BLUE):
        """Crear botón de navegación en la barra lateral."""
        btn = ctk.CTkButton(
            parent,
            text=text,
            height=50,
            fg_color="transparent" if color == PRIMARY_BLUE else color,
            text_color="#FFFFFF",
            font=("Helvetica", 13),
            hover_color=SECONDARY_CYAN if color == PRIMARY_BLUE else "#FF5A50",
            command=command
        )
        btn.pack(fill="x", padx=10, pady=8)
        return btn
    
    def clear_content(self):
        """Limpiar el área de contenido."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def show_home(self):
        """Mostrar pantalla de inicio."""
        self.clear_content()
        HomeScreen(self.content_frame)
    
    def show_safety_tips(self):
        """Mostrar consejos de seguridad."""
        self.clear_content()
        SafetyTipsScreen(self.content_frame)
    
    def show_critical_zones(self):
        """Mostrar zonas críticas."""
        self.clear_content()
        CriticalZonesScreen(self.content_frame)
    
    def show_reports(self):
        """Mostrar reportes ciudadanos."""
        self.clear_content()
        ReportsScreen(self.content_frame)
    
    def show_alerts(self):
        """Mostrar alertas."""
        self.clear_content()
        AlertsScreen(self.content_frame)
    
    def show_settings(self):
        """Mostrar configuración."""
        self.clear_content()
        settings_label = ctk.CTkLabel(
            self.content_frame,
            text="⚙️ Configuración",
            font=("Helvetica", 28, "bold"),
            text_color=TEXT_DARK
        )
        settings_label.pack(pady=40, padx=40, anchor="nw")
    
    def logout(self):
        """Cerrar sesión y volver a login."""
        self.root.destroy()
        login_root = ctk.CTk()
        login = LoginScreen(login_root)
        login_root.mainloop()
    
    def center_window(self):
        """Centrar la ventana en la pantalla."""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
