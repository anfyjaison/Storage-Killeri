from PIL import Image, ImageDraw

# Create a simple 256x256 icon
img = Image.new('RGBA', (256, 256), (255, 0, 0, 255))  # Red icon
draw = ImageDraw.Draw(img)
draw.ellipse((50, 50, 206, 206), fill=(0, 0, 255, 255))  # Blue circle

# Save as ICO
img.save('icon.ico', sizes=[(256, 256)])