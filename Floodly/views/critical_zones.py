# critical_zones.py - Pantalla de zonas críticas

import customtkinter as ctk
from theme import PRIMARY_BLUE, SECONDARY_CYAN, BACKGROUND, TEXT_DARK, TEXT_LIGHT, CARD, DANGER_RED, WARNING_ORANGE

class CriticalZonesScreen:
    """
    Pantalla que muestra tabla de zonas críticas con su nivel de riesgo
    y estado actualizado.
    """
    
    def __init__(self, parent):
        self.parent = parent
        
        # Crear scroll
        main_scroll = ctk.CTkScrollableFrame(parent, fg_color=BACKGROUND)
        main_scroll.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Título
        title_label = ctk.CTkLabel(
            main_scroll,
            text="🗺️ Zonas Críticas",
            font=("Helvetica", 28, "bold"),
            text_color=TEXT_DARK
        )
        title_label.pack(anchor="w", pady=(0, 20))
        
        # Descripción
        desc_label = ctk.CTkLabel(
            main_scroll,
            text="Áreas identificadas con mayor riesgo de inundación",
            font=("Helvetica", 12),
            text_color=TEXT_LIGHT
        )
        desc_label.pack(anchor="w", pady=(0, 20))
        
        # Datos de zonas críticas
        zones_data = [
            {"zona": "Mercado Oriental", "nivel": "Alto", "estado": "Crítico", "fecha": "Hace 2 horas"},
            {"zona": "El Riguero", "nivel": "Alto", "estado": "Crítico", "fecha": "Hace 1 hora"},
            {"zona": "Barrio Altagracia", "nivel": "Alto", "estado": "En riesgo", "fecha": "Hace 3 horas"},
            {"zona": "Barrio Pedro Árauz Palacios", "nivel": "Alto", "estado": "En riesgo", "fecha": "Hace 4 horas"},
            {"zona": "Barrio San Judas", "nivel": "Medio", "estado": "Monitoreado", "fecha": "Hace 1 hora"},
        ]
        
        # Crear tabla
        table_frame = ctk.CTkFrame(main_scroll, fg_color=CARD, corner_radius=10)
        table_frame.pack(fill="both", expand=True)
        
        # Header de tabla
        header_frame = ctk.CTkFrame(table_frame, fg_color=PRIMARY_BLUE, corner_radius=(10, 10, 0, 0))
        header_frame.pack(fill="x")
        
        headers = ["Zona", "Nivel", "Estado", "Última Actualización"]
        weights = [3, 1, 1, 2]
        
        for header, weight in zip(headers, weights):
            header_label = ctk.CTkLabel(
                header_frame,
                text=header,
                font=("Helvetica", 12, "bold"),
                text_color="#FFFFFF"
            )
            header_label.pack(side="left", fill="both", expand=True, weight=weight, padx=15, pady=15)
        
        # Rows de datos
        for i, zone in enumerate(zones_data):
            row_frame = ctk.CTkFrame(
                table_frame,
                fg_color=CARD if i % 2 == 0 else BACKGROUND,
                corner_radius=0
            )
            row_frame.pack(fill="x")
            
            # Zona
            zona_label = ctk.CTkLabel(
                row_frame,
                text=zone["zona"],
                font=("Helvetica", 11),
                text_color=TEXT_DARK
            )
            zona_label.pack(side="left", fill="both", expand=True, weight=3, padx=15, pady=12)
            
            # Nivel con color
            nivel_color = DANGER_RED if zone["nivel"] == "Alto" else WARNING_ORANGE
            nivel_frame = ctk.CTkFrame(row_frame, fg_color="transparent")
            nivel_frame.pack(side="left", fill="both", expand=True, weight=1, padx=15, pady=12)
            
            nivel_badge = ctk.CTkLabel(
                nivel_frame,
                text=zone["nivel"],
                font=("Helvetica", 10, "bold"),
                text_color="#FFFFFF",
                fg_color=nivel_color,
                corner_radius=5,
                padx=10,
                pady=5
            )
            nivel_badge.pack()
            
            # Estado
            estado_label = ctk.CTkLabel(
                row_frame,
                text=zone["estado"],
                font=("Helvetica", 10),
                text_color=TEXT_LIGHT
            )
            estado_label.pack(side="left", fill="both", expand=True, weight=1, padx=15, pady=12)
            
            # Fecha
            fecha_label = ctk.CTkLabel(
                row_frame,
                text=zone["fecha"],
                font=("Helvetica", 10),
                text_color=TEXT_LIGHT
            )
            fecha_label.pack(side="left", fill="both", expand=True, weight=2, padx=15, pady=12)
        
        # Footer
        footer_frame = ctk.CTkFrame(table_frame, fg_color=BACKGROUND, corner_radius=(0, 0, 10, 10))
        footer_frame.pack(fill="x")
        
        footer_label = ctk.CTkLabel(
            footer_frame,
            text="Total de zonas críticas monitoreadas: 5",
            font=("Helvetica", 10),
            text_color=TEXT_LIGHT
        )
        footer_label.pack(pady=10)
