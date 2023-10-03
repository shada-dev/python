import cv2

# Define a mapping of basic color names to RGB value ranges
basic_colors = {
    "black": ((0, 0, 0), (40, 40, 40)),
    "white": ((200, 200, 200), (255, 255, 255)),
    "red": ((150, 0, 0), (255, 60, 60)),
    "green": ((0, 150, 0), (60, 255, 60)),
    "blue": ((0, 0, 150), (60, 60, 255)),
    "yellow": ((150, 150, 0), (255, 255, 60)),
    "brown": ((90, 45, 0), (140, 70, 40)),
    "orange": ((200, 100, 0), (255, 150, 60)),
    "pink": ((200, 100, 100), (255, 150, 150)),
    "purple": ((100, 0, 100), (150, 60, 150)),
    "gray": ((100, 100, 100), (180, 180, 180)),
    "cyan": ((0, 150, 150), (60, 255, 255)),
    "magenta": ((150, 0, 150), (255, 60, 255)),
    "olive": ((100, 100, 0), (150, 150, 60)),
    "lime": ((0, 100, 0), (60, 255, 60)),
    "teal": ((0, 100, 100), (60, 150, 150)),
    "navy": ((0, 0, 100), (60, 60, 150)),
    "maroon": ((100, 0, 0), (150, 60, 60)),
    "forest green": ((0, 60, 0), (60, 150, 60)),
    "royal blue": ((0, 0, 100), (60, 60, 150)),
    "gold": ((150, 100, 0), (255, 200, 60)),
    "pink": ((200, 100, 150), (255, 150, 200)),
    "violet": ((100, 0, 100), (150, 60, 150)),
    "silver": ((150, 150, 150), (200, 200, 200)),
    "turquoise": ((0, 150, 150), (60, 255, 255)),
    "fuchsia": ((150, 0, 150), (255, 60, 255)),
    "olive green": ((60, 60, 0), (150, 150, 60)),
    "lime green": ((0, 100, 0), (60, 255, 60)),
    "teal blue": ((0, 60, 60), (60, 150, 150)),
    "navy blue": ((0, 0, 100), (60, 60, 150)),
    "purple red": ((100, 0, 60), (150, 60, 100)),
    "beige": ((245, 245, 220), (255, 255, 230)),
    "indigo": ((75, 0, 130), (128, 0, 128)),
    "lavender": ((230, 230, 250), (255, 240, 245)),
    "turquoise": ((64, 224, 208), (0, 206, 209)),
    "coral": ((255, 127, 80), (255, 160, 122)),
    "salmon": ((250, 128, 114), (255, 160, 122)),
    "khaki": ((240, 230, 140), (255, 255, 102)),
    "plum": ((221, 160, 221), (255, 240, 245)),
    "gold": ((255, 215, 0), (255, 223, 0)),
    "silver": ((192, 192, 192), (211, 211, 211)),
    "peach": ((255, 218, 185), (255, 228, 196)),
    "turquoise": ((64, 224, 208), (70, 130, 180)),
    "tan": ((210, 180, 140), (244, 164, 96)),
    "chocolate": ((139, 69, 19), (210, 105, 30)),
    "ivory": ((255, 255, 240), (255, 255, 224)),
    "lavender": ((230, 230, 250), (230, 230, 250)),
    "orchid": ((218, 112, 214), (255, 131, 250)),
    "azure": ((240, 255, 255), (240, 255, 255)),
    "blue2": ((2, 70, 230),(2, 70, 230)),
    # Add more basic color definitions as needed
}


def get_basic_color(rgb_value):
    for color_name, (lower_bound, upper_bound) in basic_colors.items():
        if all(lb <= value <= ub for value, (lb, ub) in zip(rgb_value, zip(lower_bound, upper_bound))):
            return color_name
    return "unknown"

def get_dominant_color_name(image_path, crop_size):
    # Read the image
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Image not found or could not be loaded.")
        return None

    # Get the dimensions of the image
    height, width, _ = image.shape

    # Calculate the center coordinates
    center_x = width // 2
    center_y = height // 2

    # Calculate the cropping boundaries
    half_crop = crop_size // 2
    crop_x1 = max(center_x - half_crop, 0)
    crop_x2 = min(center_x + half_crop, width)
    crop_y1 = max(center_y - half_crop, 0)
    crop_y2 = min(center_y + half_crop, height)

    # Crop the center region
    cropped_image = image[crop_y1:crop_y2, crop_x1:crop_x2]

    # Convert the BGR value to RGB
    rgb_value = (int(cropped_image[0, 0, 2]), int(cropped_image[0, 0, 1]), int(cropped_image[0, 0, 0]))

    # Get the basic color name
    basic_color_name = get_basic_color(rgb_value)

    return basic_color_name

if __name__ == "__main__":
    image_path = "blue.jpg"  # Replace with the path to your image
    crop_size = 500 # Adjust the size of the center region as needed
    basic_color_name = get_dominant_color_name("D:\\program_files\\python\\imag2.jpg", crop_size)

    if basic_color_name is not None:
        print("Color:", basic_color_name)
