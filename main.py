from nicegui import ui
import numpy as np
from PIL import Image
import io
import base64
from pathlib import Path

image_ui = ui.image("").props("no-transition")  # no animation


corr_im_path = "temp.jpg"


# def update_image():
#     new_img = generate_image()
#     image_ui.source = new_img


def update_image():
    if Path(corr_im_path).exists():
        img = Image.open(corr_im_path)
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format="PNG")  # Конвертируем в PNG
        img_bytes = img_byte_arr.getvalue()

        img_base64 = base64.b64encode(img_bytes).decode("utf-8")
        image_ui.source = f"data:image/png;base64,{img_base64}"


ui.timer(1, update_image)
ui.run()
