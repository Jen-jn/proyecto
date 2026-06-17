# report_detail.py - Pantalla de detalle del reporte

import customtkinter as ctk
from theme import PRIMARY_BLUE, SECONDARY_CYAN, BACKGROUND, TEXT_DARK, TEXT_LIGHT, CARD, DANGER_RED

class ReportDetailScreen:
    """
    Pantalla que muestra los detalles completos de un reporte específico.
    """
    
    def __init__(self, parent, report_data=None):
        self.parent = parent
        self.report_data = report_data or {
            "tipo": "Calle Inundada",
            "ubicacion": "Avenida Principal, Sector Norte",
            "fecha": "2024-06-17",
            "hora": "14:30",
            "nivel": "Alto",
            "descripcion": "La calle se encuentra completamente inundada debido a las lluvias intensas de las últimas horas. Se recomienda no transitar por esta zona.",
            "estado": "En revisión"
        }
        
        # Frame principal
        main_scroll = ctk.CTkScrollableFrame(parent, fg_color=BACKGROUND)
        main_scroll.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Botón regresar
        back_btn = ctk.CTkButton(
            main_scroll,
            text="← Regresar",
            fg_color="transparent",
            text_color=PRIMARY_BLUE,
            hover_color="transparent",
            font=("Helvetica", 11),
            command=self.go_back
        )
        back_btn.pack(anchor="w", pady=(0, 20))
        
        # Card principal
        detail_frame = ctk.CTkFrame(main_scroll, fg_color=CARD, corner_radius=10)
        detail_frame.pack(fill="both", expand=True)
        
        # Imagen simulada
        image_frame = ctk.CTkFrame(detail_frame, fg_color="#E0E7FF", corner_radius=(10, 10, 0, 0))
        image_frame.pack(fill="x")
        
        image_label = ctk.CTkLabel(
            image_frame,
            text="📸 Imagen del Reporte",
            font=("Helvetica", 18),
            text_color=TEXT_DARK
        )
        image_label.pack(pady=60)
        
        # Contenido
        content_frame = ctk.CTkFrame(detail_frame, fg_color=CARD)
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Tipo y estado
        header_frame = ctk.CTkFrame(content_frame, fg_color=CARD)
        header_frame.pack(fill="x", pady=(0, 20))
        
        type_label = ctk.CTkLabel(
            header_frame,
            text=self.report_data["tipo"],
            font=("Helvetica", 22, "bold"),
            text_color=TEXT_DARK
        )
        type_label.pack(side="left")
        
        status_badge = ctk.CTkLabel(
            header_frame,
            text=self.report_data["estado"].upper(),
            font=("Helvetica", 10, "bold"),
            text_color="#FFFFFF",
            fg_color=PRIMARY_BLUE,
            corner_radius=5,
            padx=10,
            pady=5
        )
        status_badge.pack(side="right")
        
        # Información de detalle
        info_items = [
            ("📍 Ubicación", self.report_data["ubicacion"]),
            ("📅 Fecha", self.report_data["fecha"]),
            ("⏰ Hora", self.report_data["hora"]),
            ("⚠️ Nivel", self.report_data["nivel"]),
        ]
        
        for label, value in info_items:
            self._create_info_row(content_frame, label, value)
        
        # Separador
        sep = ctk.CTkFrame(content_frame, height=2, fg_color=SECONDARY_CYAN)
        sep.pack(fill="x", pady=20)
        
        # Descripción
        desc_title = ctk.CTkLabel(
            content_frame,
            text="Descripción",
            font=("Helvetica", 14, "bold"),
            text_color=TEXT_DARK
        )
        desc_title.pack(anchor="w", pady=(0, 10))
        
        desc_text = ctk.CTkLabel(
            content_frame,
            text=self.report_data["descripcion"],
            font=("Helvetica", 11),
            text_color=TEXT_LIGHT,
            justify="left",
            wraplength=500
        )
        desc_text.pack(anchor="w", pady=(0, 20))
        
        # Botones de acción
        buttons_frame = ctk.CTkFrame(content_frame, fg_color=CARD)
        buttons_frame.pack(fill="x", pady=(20, 0))
        
        edit_btn = ctk.CTkButton(
            buttons_frame,
            text="✏️ Editar",
            height=40,
            fg_color=PRIMARY_BLUE,
            hover_color=SECONDARY_CYAN,
            text_color="#FFFFFF",
            command=lambda: print("Editar reporte")
        )
        edit_btn.pack(side="left", fill="both", expand=True, padx=(0, 10))
        
        delete_btn = ctk.CTkButton(
            buttons_frame,
            text="🗑️ Eliminar",
            height=40,
            fg_color=DANGER_RED,
            hover_color="#FF5A50",
            text_color="#FFFFFF",
            command=lambda: print("Eliminar reporte")
        )
        delete_btn.pack(side="left", fill="both", expand=True)
    
    def _create_info_row(self, parent, label, value):
        """Crear fila de información."""
        row_frame = ctk.CTkFrame(parent, fg_color=BACKGROUND, corner_radius=5)
        row_frame.pack(fill="x", pady=8)
        
        label_widget = ctk.CTkLabel(
            row_frame,
            text=label,
            font=("Helvetica", 11),
            text_color=TEXT_DARK,
            width=80
        )
        label_widget.pack(side="left", padx=10, pady=10)
        
        value_widget = ctk.CTkLabel(
            row_frame,
            text=value,
            font=("Helvetica", 11, "bold"),
            text_color=PRIMARY_BLUE
        )
        value_widget.pack(side="left", padx=10, pady=10)
    
    def go_back(self):
        """Regresar a lista de reportes."""
        pass
