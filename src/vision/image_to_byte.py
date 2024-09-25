from PIL import Image
import io

def image_to_bytes(image_path):
    with Image.open(image_path) as img:
        img_byte_array = io.BytesIO()
        img.save(img_byte_array, format='PNG')
        img_bytes = img_byte_array.getvalue()

    return img_bytes

image_path = '/home/seveneleven/pythonProjects/Archieve-hack/5306f0a1-7569-4fdb-b257-c98f2452cb56-141_1_32320010.png'  
image_bytes = image_to_bytes(image_path)

print(f"Размер изображения в байтах: {image_bytes}")
