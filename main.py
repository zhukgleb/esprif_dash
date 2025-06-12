from nicegui import ui
from image import update_image


ui.timer(1, update_image)

ui.run()
