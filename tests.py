from PIL import Image
import numpy as np


def generate_image():
    img_array = np.random.randint(0, 255, (200, 300, 3), dtype=np.uint8)
    img = Image.fromarray(img_array)

    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format="PNG")
    img_bytes = img_byte_arr.getvalue()

    img_base64 = base64.b64encode(img_bytes).decode("utf-8")
    return f"data:image/png;base64,{img_base64}"
