from PIL import Image
from PIL import ImageFilter

image = Image.open('flower.webp')

cropped_image = image.crop((10, 10, 200, 200))
cropped_image.save('cropped_result.jpg')

resized_image = cropped_image.resize((100, 100))
resized_image.save('resized_result.jpg')

filtered_image = resized_image.filter(ImageFilter.BLUR)
filtered_image.save('filtered_result.jpg')

if filtered_image.mode == 'RGBA':
    filtered_image = filtered_image.convert('RGB')

    image.save('result.jpg')