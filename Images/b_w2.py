from PIL import Image

def blackAndWhite(image):
    """Converts the argument image to black and white."""
    blackPixel = (0, 0, 0)
    whitePixel = (255, 255, 255)
    pixels = image.load()

    for y in range(image.height):
        for x in range(image.width):
            r, g, b = pixels[x, y]
            average = (r + g + b) // 3
            pixels[x, y] = blackPixel if average < 128 else whitePixel

# Load the image
image_path = r"C:\Users\cenih\OneDrive\Pictures\download (1).png"
image = Image.open(image_path).convert("RGB")

# Show original image
print('Close the image to see the black and white image')
image.show()

# Convert to black and white
blackAndWhite(image)

# Show and save the result
image.show()
image.save("black_and_white_image.png")
