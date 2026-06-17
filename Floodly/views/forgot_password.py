# forgot_password.py - Pantalla de recuperación de contraseña

import customtkinter as ctk
from views.login import LoginScreen
from theme import PRIMARY_BLUE, SECONDARY_CYAN, BACKGROUND, TEXT_DARK, TEXT_LIGHT, SUCCESS_GREEN

class ForgotPasswordScreen:
    """
    Pantalla para recuperar contraseña mediante correo electrónico.
    """
    
    def __init__(self, root):
        self.root = root
        self.root.title("Floodly - Recuperar Contraseña")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.center_window()
        self.root.configure(fg_color=BACKGROUND)
        
        # Frame principal
        main_frame = ctk.CTkFrame(self.root, fg_color=BACKGROUND)
        main_frame.pack(fill="both", expand=True, padx=30, pady=30)
        
        # Botón regresar
        back_btn = ctk.CTkButton(
            main_frame,
            text="← Regresar",
            fg_color="transparent",
            text_color=PRIMARY_BLUE,
            hover_color="transparent",
            font=("Helvetica", 11),
            command=self.go_back
        )
        back_btn.pack(anchor="w", pady=(0, 20))
        
        # Título
        title_label = ctk.CTkLabel(
            main_frame,
            text="Recuperar Contraseña",
            font=("Helvetica", 24, "bold"),
            text_color=TEXT_DARK
        )
        title_label.pack(pady=(0, 10))
        
        # Descripción
        desc_label = ctk.CTkLabel(
            main_frame,
            text="Ingresa tu correo electrónico y enviaremos un enlace para\nrecuperar tu contraseña.",
            font=("Helvetica", 12),
            text_color=TEXT_LIGHT,
            justify="center"
        )
        desc_label.pack(pady=(0, 30))
        
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
        self.email_entry.pack(fill="x", pady=(0, 30))
        
        # Botón enviar
        send_btn = ctk.CTkButton(
            main_frame,
            text="Enviar enlace",
            height=40,
            fg_color=PRIMARY_BLUE,
            hover_color=SECONDARY_CYAN,
            text_color="#FFFFFF",
            font=("Helvetica", 13, "bold"),
            command=self.send_email
        )
        send_btn.pack(fill="x", pady=(0, 20))
        
        # Mensaje de confirmación (inicialmente oculto)
        self.message_frame = ctk.CTkFrame(main_frame, fg_color=SUCCESS_GREEN, corner_radius=8)
        self.message_frame.pack(fill="x", pady=(0, 0))
        
        self.message_label = ctk.CTkLabel(
            self.message_frame,
            text="✓ Correo enviado correctamente",
            font=("Helvetica", 12),
            text_color="#FFFFFF"
        )
        self.message_label.pack(pady=15)
        self.message_frame.pack_forget()  # Ocultar inicialmente
    
    def center_window(self):
        """Centrar la ventana en la pantalla."""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
    
    def send_email(self):
        """Enviar enlace de recuperación."""
        email = self.email_entry.get()
        
        if email:
            self.message_frame.pack(fill="x", pady=(0, 0))
            self.root.after(2000, self.go_back)
    
    def go_back(self):
        """Regresar a pantalla de login."""
        self.root.destroy()
        login_root = ctk.CTk()
        login = LoginScreen(login_root)
        login_root.mainloop()
