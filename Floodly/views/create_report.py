# create_report.py - Pantalla para crear nuevo reporte

import customtkinter as ctk
from theme import PRIMARY_BLUE, SECONDARY_CYAN, BACKGROUND, TEXT_DARK, TEXT_LIGHT, CARD, SUCCESS_GREEN

class CreateReportScreen:
    """
    Pantalla para crear nuevo reporte de inundación.
    """
    
    def __init__(self, parent):
        self.parent = parent
        
        # Frame principal
        main_scroll = ctk.CTkScrollableFrame(parent, fg_color=BACKGROUND)
        main_scroll.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Título
        title_label = ctk.CTkLabel(
            main_scroll,
            text="📝 Crear Nuevo Reporte",
            font=("Helvetica", 28, "bold"),
            text_color=TEXT_DARK
        )
        title_label.pack(anchor="w", pady=(0, 20))
        
        # Formulario
        form_frame = ctk.CTkFrame(main_scroll, fg_color=CARD, corner_radius=10)
        form_frame.pack(fill="x", pady=(0, 20))
        
        # Tipo de problema
        type_label = ctk.CTkLabel(
            form_frame,
            text="Tipo de Problema",
            font=("Helvetica", 12, "bold"),
            text_color=TEXT_DARK
        )
        type_label.pack(anchor="w", padx=15, pady=(15, 5))
        
        self.type_var = ctk.StringVar(value="Calle inundada")
        type_menu = ctk.CTkComboBox(
            form_frame,
            values=["Calle inundada", "Lluvia intensa", "Zonas susceptibles", "Otros"],
            variable=self.type_var,
            height=40,
            fg_color="#FFFFFF",
            border_width=1,
            border_color=SECONDARY_CYAN
        )
        type_menu.pack(fill="x", padx=15, pady=(0, 15))
        
        # Ubicación
        location_label = ctk.CTkLabel(
            form_frame,
            text="Ubicación (Automática)",
            font=("Helvetica", 12, "bold"),
            text_color=TEXT_DARK
        )
        location_label.pack(anchor="w", padx=15, pady=(0, 5))
        
        location_entry = ctk.CTkEntry(
            form_frame,
            placeholder_text="📍 Tu ubicación actual",
            height=40,
            fg_color="#FFFFFF",
            border_width=1,
            border_color=SECONDARY_CYAN
        )
        location_entry.pack(fill="x", padx=15, pady=(0, 15))
        
        # Nivel de gravedad
        severity_label = ctk.CTkLabel(
            form_frame,
            text="Nivel de Gravedad",
            font=("Helvetica", 12, "bold"),
            text_color=TEXT_DARK
        )
        severity_label.pack(anchor="w", padx=15, pady=(0, 10))
        
        severity_frame = ctk.CTkFrame(form_frame, fg_color=CARD)
        severity_frame.pack(fill="x", padx=15, pady=(0, 15))
        
        self.severity_var = ctk.StringVar(value="Medio")
        severities = ["Bajo", "Medio", "Alto"]
        for severity in severities:
            radio_btn = ctk.CTkRadioButton(
                severity_frame,
                text=severity,
                variable=self.severity_var,
                value=severity,
                text_color=TEXT_DARK
            )
            radio_btn.pack(side="left", padx=10)
        
        # Foto/Imagen
        photo_label = ctk.CTkLabel(
            form_frame,
            text="Foto del Problema",
            font=("Helvetica", 12, "bold"),
            text_color=TEXT_DARK
        )
        photo_label.pack(anchor="w", padx=15, pady=(15, 10))
        
        photo_frame = ctk.CTkFrame(form_frame, fg_color=BACKGROUND, corner_radius=8)
        photo_frame.pack(fill="x", padx=15, pady=(0, 10))
        
        photo_btn = ctk.CTkButton(
            photo_frame,
            text="📷 Tomar foto con cámara",
            height=60,
            fg_color=PRIMARY_BLUE,
            hover_color=SECONDARY_CYAN,
            text_color="#FFFFFF",
            command=lambda: print("Abrir cámara")
        )
        photo_btn.pack(fill="both", padx=15, pady=(15, 5))
        
        upload_btn = ctk.CTkButton(
            photo_frame,
            text="📁 Subir imagen desde archivo",
            height=60,
            fg_color=SECONDARY_CYAN,
            hover_color=PRIMARY_BLUE,
            text_color="#FFFFFF",
            command=lambda: print("Seleccionar archivo")
        )
        upload_btn.pack(fill="both", padx=15, pady=(0, 15))
        
        # Descripción
        desc_label = ctk.CTkLabel(
            form_frame,
            text="Descripción del Problema",
            font=("Helvetica", 12, "bold"),
            text_color=TEXT_DARK
        )
        desc_label.pack(anchor="w", padx=15, pady=(0, 5))
        
        self.desc_text = ctk.CTkTextbox(
            form_frame,
            height=120,
            fg_color="#FFFFFF",
            border_width=1,
            border_color=SECONDARY_CYAN,
            text_color=TEXT_DARK
        )
        self.desc_text.pack(fill="both", padx=15, pady=(0, 15))
        
        # Botón enviar
        submit_btn = ctk.CTkButton(
            form_frame,
            text="✓ Enviar Reporte",
            height=45,
            fg_color=SUCCESS_GREEN,
            hover_color=PRIMARY_BLUE,
            text_color="#FFFFFF",
            font=("Helvetica", 13, "bold"),
            command=self.submit_report
        )
        submit_btn.pack(fill="x", padx=15, pady=15)
    
    def submit_report(self):
        """Enviar reporte."""
        print("Reporte enviado exitosamente")
