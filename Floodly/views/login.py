# login.py - Pantalla de inicio de sesión

import customtkinter as ctk
from views.dashboard import Dashboard
from theme import PRIMARY_BLUE, SECONDARY_CYAN, BACKGROUND, TEXT_DARK, TEXT_LIGHT

class LoginScreen:
    """
    Pantalla de inicio de sesión con opciones de email/contraseña
    y redes sociales.
    """
    
    def __init__(self, root):
        self.root = root
        self.root.title("Floodly - Login")
        self.root.geometry("500x700")
        self.root.resizable(False, False)
        self.center_window()
        
        # Configurar color de fondo
        self.root.configure(fg_color=BACKGROUND)
        
        # Crear frame principal con scroll
        main_frame = ctk.CTkFrame(self.root, fg_color=BACKGROUND)
        main_frame.pack(fill="both", expand=True, padx=30, pady=30)
        
        # Logo
        logo_label = ctk.CTkLabel(
            main_frame,
            text="🌊",
            font=("Helvetica", 60)
        )
        logo_label.pack(pady=(0, 10))
        
        # Título
        title_label = ctk.CTkLabel(
            main_frame,
            text="Inicia sesión o regístrate",
            font=("Helvetica", 22, "bold"),
            text_color=TEXT_DARK
        )
        title_label.pack(pady=(0, 30))
        
        # Campo de correo
        email_label = ctk.CTkLabel(
            main_frame,
            text="Correo electrónico",
            font=("Helvetica", 12),
            text_color=TEXT_DARK
        )
        email_label.pack(anchor="w", pady=(0, 5))
        
        self.email_entry = ctk.CTkEntry(
            main_frame,
            placeholder_text="tu@email.com",
            height=40,
            border_width=1,
            border_color=SECONDARY_CYAN,
            fg_color="#FFFFFF"
        )
        self.email_entry.pack(fill="x", pady=(0, 20))
        
        # Campo de contraseña
        password_label = ctk.CTkLabel(
            main_frame,
            text="Contraseña",
            font=("Helvetica", 12),
            text_color=TEXT_DARK
        )
        password_label.pack(anchor="w", pady=(0, 5))
        
        # Frame para contraseña y botón mostrar/ocultar
        password_frame = ctk.CTkFrame(main_frame, fg_color=BACKGROUND)
        password_frame.pack(fill="x", pady=(0, 10))
        
        self.password_entry = ctk.CTkEntry(
            password_frame,
            placeholder_text="Contraseña",
            height=40,
            border_width=1,
            border_color=SECONDARY_CYAN,
            fg_color="#FFFFFF",
            show="•"
        )
        self.password_entry.pack(side="left", fill="both", expand=True, padx=(0, 10))
        
        self.show_password_btn = ctk.CTkButton(
            password_frame,
            text="👁",
            width=40,
            height=40,
            fg_color=PRIMARY_BLUE,
            hover_color=SECONDARY_CYAN,
            command=self.toggle_password
        )
        self.show_password_btn.pack(side="right")
        
        self.password_visible = False
        
        # Link olvidar contraseña
        forgot_password_btn = ctk.CTkButton(
            main_frame,
            text="¿Olvidaste tu contraseña?",
            fg_color="transparent",
            text_color=PRIMARY_BLUE,
            hover_color="transparent",
            font=("Helvetica", 11),
            command=self.go_to_forgot_password
        )
        forgot_password_btn.pack(anchor="e", pady=(0, 30))
        
        # Botón Iniciar sesión
        login_btn = ctk.CTkButton(
            main_frame,
            text="Iniciar sesión",
            height=40,
            fg_color=PRIMARY_BLUE,
            hover_color=SECONDARY_CYAN,
            text_color="#FFFFFF",
            font=("Helvetica", 13, "bold"),
            command=self.login
        )
        login_btn.pack(fill="x", pady=(0, 20))
        
        # Divisor
        divider_label = ctk.CTkLabel(
            main_frame,
            text="o continúa con",
            font=("Helvetica", 11),
            text_color=TEXT_LIGHT
        )
        divider_label.pack(pady=20)
        
        # Botones de redes sociales
        buttons_frame = ctk.CTkFrame(main_frame, fg_color=BACKGROUND)
        buttons_frame.pack(fill="x", pady=(0, 30))
        
        google_btn = ctk.CTkButton(
            buttons_frame,
            text="Google",
            height=40,
            fg_color="#FFFFFF",
            text_color=TEXT_DARK,
            border_width=1,
            border_color=TEXT_LIGHT,
            command=self.login_google
        )
        google_btn.pack(side="left", fill="both", expand=True, padx=(0, 10))
        
        facebook_btn = ctk.CTkButton(
            buttons_frame,
            text="Facebook",
            height=40,
            fg_color="#1877F2",
            text_color="#FFFFFF",
            command=self.login_facebook
        )
        facebook_btn.pack(side="left", fill="both", expand=True)
        
        # Link registrarse
        register_label = ctk.CTkLabel(
            main_frame,
            text="¿No tienes cuenta? Regístrate",
            font=("Helvetica", 11),
            text_color=PRIMARY_BLUE
        )
        register_label.pack(pady=(0, 15))
        
        # Link continuar sin registrarse
        skip_login_btn = ctk.CTkButton(
            main_frame,
            text="Continuar sin registrarse",
            fg_color="transparent",
            text_color=TEXT_LIGHT,
            hover_color="transparent",
            font=("Helvetica", 10),
            command=self.skip_login
        )
        skip_login_btn.pack()
    
    def center_window(self):
        """Centrar la ventana en la pantalla."""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
    
    def toggle_password(self):
        """Mostrar/ocultar contraseña."""
        self.password_visible = not self.password_visible
        if self.password_visible:
            self.password_entry.configure(show="")
            self.show_password_btn.configure(text="🙈")
        else:
            self.password_entry.configure(show="•")
            self.show_password_btn.configure(text="👁")
    
    def login(self):
        """Procesar inicio de sesión."""
        email = self.email_entry.get()
        password = self.password_entry.get()
        
        if email and password:
            self.root.destroy()
            dashboard_root = ctk.CTk()
            dashboard = Dashboard(dashboard_root)
            dashboard_root.mainloop()
    
    def login_google(self):
        """Simulación de login con Google."""
        self.root.destroy()
        dashboard_root = ctk.CTk()
        dashboard = Dashboard(dashboard_root)
        dashboard_root.mainloop()
    
    def login_facebook(self):
        """Simulación de login con Facebook."""
        self.root.destroy()
        dashboard_root = ctk.CTk()
        dashboard = Dashboard(dashboard_root)
        dashboard_root.mainloop()
    
    def go_to_forgot_password(self):
        """Ir a pantalla de recuperar contraseña."""
        self.root.destroy()
        forgot_root = ctk.CTk()
        from views.forgot_password import ForgotPasswordScreen
        forgot = ForgotPasswordScreen(forgot_root)
        forgot_root.mainloop()
    
    def skip_login(self):
        """Continuar sin registrarse."""
        self.root.destroy()
        dashboard_root = ctk.CTk()
        dashboard = Dashboard(dashboard_root)
        dashboard_root.mainloop()
