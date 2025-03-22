from PIL import Image

def grayscale(image):
    """Converts the argument image to grayscale."""
    pixels = image.load()

    for y in range(image.height):
        for x in range(image.width):
            r, g, b = pixels[x, y]
    
            lum = int(r * 0.299 + g * 0.587 + b * 0.114)
            pixels[x, y] = (lum, lum, lum)

image = Image.open("path_of_the_image").convert('RGB') #provide path for the image in raw format or filename
print('Close the image to see the grayscale image')
image.show()

grayscale(image)

image.show()
image.save('grayscale_smokey.gif')
