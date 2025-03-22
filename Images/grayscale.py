from PIL import Image

def grayscale(image):
    """Converts the argument image to grayscale."""
    pixels = image.load()

    for y in range(image.height):
        for x in range(image.width):
            r, g, b = pixels[x, y]
            # Calculate luminance using weighted grayscale formula
            lum = int(r * 0.299 + g * 0.587 + b * 0.114)
            pixels[x, y] = (lum, lum, lum)

# Open and display the image
image = Image.open(r"C:\Users\cenih\OneDrive\Pictures\download (1).png").convert('RGB')
print('Close the image to see the grayscale image')
image.show()

grayscale(image)

image.show()
image.save('grayscale_smokey.gif')
