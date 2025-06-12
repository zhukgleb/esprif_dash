from nicegui import ui


def content() -> None:
    with ui.card().style("width: 100%; height: 80vh; display: grid; grid-template-columns: 1fr 1fr;"):
        ui.label("Объект").style(
            'color: black; font-family: "Rational Display", sans-serif; font-size:28px; '
            'grid-column: 1 / span 2;'  # Заголовок на всю ширину
        )

        # Левая колонка - элементы управления
        with ui.column().style("padding: 1rem; overflow-y: auto; height: 100%;"):
            ui.label(
                "manipulators"
            ).style(
                'color: black; font-family: "Rational Display", sans-serif; font-size:18px;'
            )
            
            # Примеры элементов управления
            slider = ui.slider(min=0, max=100, value=50).classes("w-full")
            checkbox = ui.checkbox("Check").classes("w-full")
            dropdown = ui.select(["Option 1", "Option 2", "Option 3"], value="Option 1").classes("w-full")
            text_input = ui.input(label="Input text").classes("w-full")
            
        # Правая колонка - изображение
        with ui.column().style("padding: 1rem; height: 100%; display: flex; align-items: center; justify-content: center;"):
            try:
                image_path = "temp.jpg"  
                ui.image(image_path).style("max-width: 100%; max-height: 100%; object-fit: contain;")
            except Exception as e:
                ui.label(f"Slit image error: {str(e)}").classes("text-red")