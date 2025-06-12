from nicegui import ui
from image import update_image

image_ui = ui.image("").props("no-transition")  # no animation
corr_im_path = "temp.jpg"


ui.timer(1, update_image)


ui.run()
