from PIL import Image

def black_and_white(image_path, output_path):
    # Open the image
    image = Image.open(image_path).convert('RGB')
    pixels = image.load()
    
    # Define threshold
    threshold = 128
    
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = pixels[x, y]
            average = (r + g + b) // 3  
            
            pixels[x, y] = (0, 0, 0) if average < threshold else (255, 255, 255)
    
    image.save(output_path)
    image.show()


black_and_white(r"C:\Users\cenih\OneDrive\Pictures\download (1).png", "output_bw.jpg")
