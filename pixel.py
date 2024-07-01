'Task 2:Develop a simple image encryption tool using pixel manipulation.'
'You can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel.'
'Allow users to encrypt and decrypt images.'

from PIL import Image


def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()
    
    width, height = img.size  
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            encrypted_pixel = (r, b, g)
            pixels[i, j] = encrypted_pixel

    img.save(output_path)
    print("Image encrypted successfully!")


def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            decrypted_pixel = (b, g, r)
            pixels[i, j] = decrypted_pixel

    img.save(output_path)
    print("Image decrypted successfully!")


input_image = r"C:\Users\Krathan\Pictures\Saved Pictures\input.jpg"
encrypted_image = r"C:\Users\Krathan\Pictures\Saved Pictures\encrypted_image.jpg"
decrypted_image = r"C:\Users\Krathan\Pictures\Saved Pictures\decrypted_image.jpg"


encrypt_image(input_image, encrypted_image, key=None)
decrypt_image(encrypted_image, decrypted_image, key=None)
