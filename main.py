from PIL import Image, ImageOps, ImageFilter

def ask_again():
    again = input("Do you want to apply another filter? ")
    if again.title() == "No":
        return False
    return True

def filter():
    # ask user which filter they want
    desired_filter = input("Which filter you would like to apply?: ")

    # Open the image
    image = Image.open("image.jpg")

    if desired_filter.title() == "Sepia":
        image = image.convert("L")

        # Apply the sepia filter
        image = image.point(lambda x: x * 0.9)

        # Save the sepia image
        image.save("image_sepia.jpg")
        return ask_again()

    if desired_filter.title() == "Black":
        # Convert the image to grayscale
        image = image.convert("L")

        # Save the grayscale image
        image.save("image_bw.jpg")
        return ask_again()

    if desired_filter.title() == "Invert":
        # Invert the image
        image = ImageOps.invert(image)

        # Save the inverted image
        image.save("image_inverted.jpg")
        return ask_again()

    if desired_filter.title() == "Blur":
        # Apply the blur filter
        image = image.filter(ImageFilter.BLUR)

        # Save the blurred image
        image.save("image_blurred.jpg")
        return ask_again()

again = True

while again:
    again = filter()
