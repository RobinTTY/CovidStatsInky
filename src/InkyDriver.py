from PIL import Image, ImageFont, ImageDraw
from font_hanken_grotesk import HankenGroteskBold, HankenGroteskMedium
from inky import InkyPHAT


# Example Driver: https://github.com/pimoroni/inky/blob/master/examples/name-badge.py
class InkyDriver:
    def __init__(self):
        self.inky = InkyPHAT('yellow')

    def create_new_image(self, countries_cases):
        current_height = 0
        # inky_display.set_rotation(180)
        self.inky.set_border(self.inky.RED)

        # Create a new canvas to draw on
        img = Image.new("P", (self.inky.WIDTH, self.inky.HEIGHT))
        draw = ImageDraw.Draw(img)

        # Load the fonts
        font = ImageFont.truetype(HankenGroteskBold, 20)

        # Calculate the positioning and draw the text
        for key in countries_cases:
            text = str(key) + ": " + str(countries_cases[key])
            width, height = font.getsize(text)
            center = int((self.inky.WIDTH - width) / 2)
            draw.text((center, current_height), text, self.inky.BLACK, font=font)
            current_height += height

        # Display the completed picture
        self.inky.set_image(img)
        self.inky.show()
