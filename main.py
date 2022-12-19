import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageOps, ImageFilter

# Create a tkinter window
window = tk.Tk()
window.title("Image Filter")

# Add a file selection button
def select_file():
    # Open a file selection dialog
    file_path = filedialog.askopenfilename()

    # Print the selected file path
    print(file_path)

    # Set the file label to show the selected file
    file_label.config(text=file_path)

file_button = tk.Button(text="Select Image", command=select_file)
file_button.pack()

# Add a label to show the selected file
file_label = tk.Label(text="No image selected")
file_label.pack()

# Add a dropdown menu to select the filter
def apply_filter():
    # Get the selected file
    file_path = file_label["text"]

    # Get the selected filter
    filter = selected_filter.get()

    # Print the selected filter
    print(filter)

    # Open the image
    image = Image.open(file_path)

    if filter == "Sepia":
        image = image.convert("L")

        # Apply the sepia filter
        image = image.point(lambda x: x * 0.9)

        # Save the sepia image
        image.save("image_sepia.jpg")

    if filter == "Black and White":
        # Convert the image to grayscale
        image = image.convert("L")

        # Save the grayscale image
        image.save("image_bw.jpg")

    if filter == "Invert":
        # Invert the image
        image = ImageOps.invert(image)

        # Save the inverted image
        image.save("image_inverted.jpg")

    if filter == "Blur":
        # Apply the blur filter
        image = image.filter(ImageFilter.BLUR)

        # Save the blurred image
        image.save("image_blurred.jpg")

# Create a tkinter variable to store the selected filter
selected_filter = tk.StringVar()
selected_filter.set("Select a filter")

# Create a dropdown menu
filter_menu = tk.OptionMenu(window, selected_filter, "Sepia", "Black and White", "Invert", "Blur")
filter_menu.pack()

# Add an apply button
apply_button = tk.Button(text="Apply Filter", command=apply_filter)
apply_button.pack()

# Run the tkinter loop
window.mainloop()
