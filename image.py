from PIL import Image
import io
from pathlib import Path
from nicegui import ui
import base64

image_ui = ui.image("").props("no-transition")  # no animation


def update_image():
    corr_im_path = "temp.jpg"
    if Path(corr_im_path).exists():
        img = Image.open(corr_im_path)
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format="PNG")  # Конвертируем в PNG
        img_bytes = img_byte_arr.getvalue()

        img_base64 = base64.b64encode(img_bytes).decode("utf-8")
        image_ui.source = f"data:image/png;base64,{img_base64}"
