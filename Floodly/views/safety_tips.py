# safety_tips.py - Pantalla de consejos de seguridad

import customtkinter as ctk
from theme import PRIMARY_BLUE, SECONDARY_CYAN, BACKGROUND, TEXT_DARK, TEXT_LIGHT, CARD, DANGER_RED, WARNING_ORANGE, SUCCESS_GREEN

class SafetyTipsScreen:
    """
    Pantalla que muestra consejos de seguridad antes, durante y después
    de una inundación.
    """
    
    def __init__(self, parent):
        self.parent = parent
        
        # Crear scroll
        main_scroll = ctk.CTkScrollableFrame(parent, fg_color=BACKGROUND)
        main_scroll.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Título
        title_label = ctk.CTkLabel(
            main_scroll,
            text="💡 Consejos de Seguridad",
            font=("Helvetica", 28, "bold"),
            text_color=TEXT_DARK
        )
        title_label.pack(anchor="w", pady=(0, 20))
        
        # Descripción
        desc_label = ctk.CTkLabel(
            main_scroll,
            text="Conoce las acciones recomendadas antes, durante y después de una inundación",
            font=("Helvetica", 12),
            text_color=TEXT_LIGHT,
            justify="left"
        )
        desc_label.pack(anchor="w", pady=(0, 30))
        
        # Sección ANTES
        self.create_tip_section(
            main_scroll,
            "ANTES DE LA INUNDACIÓN",
            "🔴",
            DANGER_RED,
            [
                "Preparar mochila de emergencia con documentos, medicinas y agua",
                "Identificar rutas de evacuación seguras en tu zona",
                "Mantener documentos importantes en lugares protegidos",
                "Llevar un registro de bienes de valor (fotos, videos)",
                "Establecer plan de reunión con la familia",
                "Tener números de emergencia a mano",
            ]
        )
        
        # Sección DURANTE
        self.create_tip_section(
            main_scroll,
            "DURANTE LA INUNDACIÓN",
            "🟠",
            WARNING_ORANGE,
            [
                "No cruzar calles o puentes inundados",
                "Desconectar suministro de electricidad en el hogar",
                "Buscar zonas seguras en pisos superiores",
                "Evitar contacto con el agua de inundación",
                "Mantener contacto con autoridades y servicios de emergencia",
                "No manejar en zonas inundadas",
                "Mantener linterna y pilas a mano",
            ]
        )
        
        # Sección DESPUÉS
        self.create_tip_section(
            main_scroll,
            "DESPUÉS DE LA INUNDACIÓN",
            "🟢",
            SUCCESS_GREEN,
            [
                "Evitar agua contaminada de la inundación",
                "Revisar daños estructurales del inmueble",
                "Seguir indicaciones de autoridades sanitarias",
                "Desinfectar y limpiar pisos y superficies",
                "Desechar alimentos contaminados",
                "Documentar daños para seguros",
                "Buscar ayuda profesional si es necesario",
            ]
        )
    
    def create_tip_section(self, parent, title, icon, color, tips):
        """Crear una sección de consejos."""
        section_frame = ctk.CTkFrame(parent, fg_color=CARD, corner_radius=10)
        section_frame.pack(fill="x", pady=15)
        
        # Header con color
        header_frame = ctk.CTkFrame(section_frame, fg_color=color, corner_radius=(10, 10, 0, 0))
        header_frame.pack(fill="x")
        
        header_label = ctk.CTkLabel(
            header_frame,
            text=f"{icon} {title}",
            font=("Helvetica", 14, "bold"),
            text_color="#FFFFFF"
        )
        header_label.pack(pady=15)
        
        # Contenido de tips
        content_frame = ctk.CTkFrame(section_frame, fg_color=CARD)
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        for tip in tips:
            tip_frame = ctk.CTkFrame(content_frame, fg_color=BACKGROUND, corner_radius=5)
            tip_frame.pack(fill="x", pady=8)
            
            tip_label = ctk.CTkLabel(
                tip_frame,
                text="✓ " + tip,
                font=("Helvetica", 11),
                text_color=TEXT_DARK,
                justify="left",
                wraplength=400
            )
            tip_label.pack(anchor="w", padx=10, pady=8)
