# home.py - Pantalla de inicio principal

import customtkinter as ctk
from theme import PRIMARY_BLUE, SECONDARY_CYAN, BACKGROUND, TEXT_DARK, TEXT_LIGHT, CARD, DANGER_RED, WARNING_ORANGE, SUCCESS_GREEN

class HomeScreen:
    """
    Pantalla principal que muestra mapa, zonas de riesgo,
    alertas recientes y estado general.
    """
    
    def __init__(self, parent):
        self.parent = parent
        
        # Crear contenedor principal con scroll
        main_scroll = ctk.CTkScrollableFrame(parent, fg_color=BACKGROUND)
        main_scroll.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Título
        title_label = ctk.CTkLabel(
            main_scroll,
            text="🏠 Inicio",
            font=("Helvetica", 28, "bold"),
            text_color=TEXT_DARK
        )
        title_label.pack(anchor="w", pady=(0, 20))
        
        # Crear dos columnas
        columns_frame = ctk.CTkFrame(main_scroll, fg_color=BACKGROUND)
        columns_frame.pack(fill="both", expand=True)
        
        # Columna izquierda - Mapa
        left_column = ctk.CTkFrame(columns_frame, fg_color=BACKGROUND)
        left_column.pack(side="left", fill="both", expand=True, padx=(0, 10))
        
        # Simulación de mapa
        map_frame = ctk.CTkFrame(left_column, fg_color="#E0E7FF", corner_radius=10)
        map_frame.pack(fill="both", expand=True, pady=(0, 15))
        
        map_label = ctk.CTkLabel(
            map_frame,
            text="🗺️ Mapa de Inundaciones\n(Simulado)",
            font=("Helvetica", 18),
            text_color=TEXT_DARK
        )
        map_label.pack(pady=60)
        
        # Leyenda del mapa
        legend_frame = ctk.CTkFrame(left_column, fg_color=CARD, corner_radius=8)
        legend_frame.pack(fill="x", pady=(0, 0))
        
        legend_title = ctk.CTkLabel(
            legend_frame,
            text="Leyenda",
            font=("Helvetica", 12, "bold"),
            text_color=TEXT_DARK
        )
        legend_title.pack(anchor="w", padx=15, pady=(10, 5))
        
        # Items de leyenda
        legend_items = [
            ("📍", "Tu ubicación", PRIMARY_BLUE),
            ("✓", "Ruta segura", SUCCESS_GREEN),
            ("⚠️", "Zona alto riesgo", DANGER_RED),
            ("⚠️", "Zona riesgo medio", WARNING_ORANGE),
            ("📢", "Reporte ciudadano", SECONDARY_CYAN),
        ]
        
        for icon, text, color in legend_items:
            item_frame = ctk.CTkFrame(legend_frame, fg_color=BACKGROUND)
            item_frame.pack(fill="x", padx=15, pady=5)
            
            icon_label = ctk.CTkLabel(
                item_frame,
                text=icon,
                font=("Helvetica", 14),
                text_color=color
            )
            icon_label.pack(side="left", padx=(0, 10))
            
            text_label = ctk.CTkLabel(
                item_frame,
                text=text,
                font=("Helvetica", 11),
                text_color=TEXT_DARK
            )
            text_label.pack(side="left")
        
        legend_frame.pack_configure(padx=0)
        
        # Columna derecha - Panel de información
        right_column = ctk.CTkFrame(columns_frame, fg_color=BACKGROUND)
        right_column.pack(side="right", fill="both", expand=True, padx=(10, 0))
        
        # Alertas recientes
        self.create_info_section(
            right_column,
            "🔔 Alertas Recientes",
            [
                "Lluvia intensa en sector norte",
                "Calle inundada - Avenida principal",
                "Zona de riesgo identificada",
            ]
        )
        
        # Clima simulado
        self.create_info_section(
            right_column,
            "🌤️ Clima",
            [
                "Temperatura: 28°C",
                "Humedad: 75%",
                "Lluvia esperada: 60%",
            ]
        )
        
        # Estado general
        state_frame = ctk.CTkFrame(right_column, fg_color=CARD, corner_radius=10)
        state_frame.pack(fill="x", pady=10)
        
        state_title = ctk.CTkLabel(
            state_frame,
            text="📊 Estado General",
            font=("Helvetica", 12, "bold"),
            text_color=TEXT_DARK
        )
        state_title.pack(anchor="w", padx=15, pady=(10, 10))
        
        # Indicadores de estado
        indicators = [
            ("Zonas en riesgo:", "5", DANGER_RED),
            ("Reportes activos:", "12", WARNING_ORANGE),
            ("Áreas seguras:", "8", SUCCESS_GREEN),
        ]
        
        for label, value, color in indicators:
            indicator_frame = ctk.CTkFrame(state_frame, fg_color=BACKGROUND)
            indicator_frame.pack(fill="x", padx=15, pady=5)
            
            label_widget = ctk.CTkLabel(
                indicator_frame,
                text=label,
                font=("Helvetica", 10),
                text_color=TEXT_LIGHT
            )
            label_widget.pack(side="left")
            
            value_widget = ctk.CTkLabel(
                indicator_frame,
                text=value,
                font=("Helvetica", 14, "bold"),
                text_color=color
            )
            value_widget.pack(side="right")
        
        # Espaciador
        ctk.CTkLabel(state_frame, text="", fg_color=BACKGROUND).pack(pady=5)
    
    def create_info_section(self, parent, title, items):
        """Crear una sección de información con título e items."""
        section_frame = ctk.CTkFrame(parent, fg_color=CARD, corner_radius=10)
        section_frame.pack(fill="x", pady=10)
        
        title_label = ctk.CTkLabel(
            section_frame,
            text=title,
            font=("Helvetica", 12, "bold"),
            text_color=TEXT_DARK
        )
        title_label.pack(anchor="w", padx=15, pady=(10, 10))
        
        for item in items:
            item_label = ctk.CTkLabel(
                section_frame,
                text="• " + item,
                font=("Helvetica", 10),
                text_color=TEXT_LIGHT,
                justify="left"
            )
            item_label.pack(anchor="w", padx=20, pady=3)
        
        ctk.CTkLabel(section_frame, text="", fg_color=CARD).pack(pady=5)
