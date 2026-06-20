from PIL import Image
import os

# Load the logo
logo_path = "C:/Users/Zoe Francois/.openclaw/workspace/site-publish/assets/ai-fluency-logo-standard.png"
output_dir = "C:/Users/Zoe Francois/.openclaw/workspace/site-publish"

# Open the image
img = Image.open(logo_path)

# Convert to RGBA if not already
if img.mode != 'RGBA':
    img = img.convert('RGBA')

# Create a square version by cropping to center
width, height = img.size
min_dim = min(width, height)
left = (width - min_dim) // 2
top = (height - min_dim) // 2
right = left + min_dim
bottom = top + min_dim

# Crop to square
square_img = img.crop((left, top, right, bottom))

# Favicon sizes to generate
sizes = {
    'favicon-16x16.png': (16, 16),
    'favicon-32x32.png': (32, 32),
    'favicon-48x48.png': (48, 48),
    'apple-touch-icon.png': (180, 180),
    'android-chrome-192x192.png': (192, 192),
    'android-chrome-512x512.png': (512, 512),
    'mstile-150x150.png': (150, 150),
}

# Generate each size
for filename, size in sizes.items():
    resized = square_img.resize(size, Image.Resampling.LANCZOS)
    output_path = os.path.join(output_dir, filename)
    resized.save(output_path, 'PNG')
    print(f"Created: {filename}")

# Create ICO file (contains 16x16, 32x32, 48x48)
ico_sizes = [(16, 16), (32, 32), (48, 48)]
ico_images = [square_img.resize(size, Image.Resampling.LANCZOS) for size in ico_sizes]

ico_path = os.path.join(output_dir, 'favicon.ico')
ico_images[0].save(ico_path, format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])
print(f"Created: favicon.ico")

print("\nAll favicon files generated successfully!")
print(f"\nFiles saved to: {output_dir}")
