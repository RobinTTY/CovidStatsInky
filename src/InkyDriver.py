from PIL import Image, ImageFont, ImageDraw
from font_hanken_grotesk import HankenGroteskBold, HankenGroteskMedium
from inky import InkyPHAT


# Example Driver: https://github.com/pimoroni/inky/blob/master/examples/name-badge.py
class InkyDriver:
    def __init__(self):
        self.inky = InkyPHAT('yellow')
        self.current_height = 0

    def create_new_image(self, countries, new_cases):
        # inky_display.set_rotation(180)
        self.inky.set_border(self.inky.RED)

        # Create a new canvas to draw on
        img = Image.new("P", (self.inky.WIDTH, self.inky.HEIGHT))
        draw = ImageDraw.Draw(img)

        # Load the fonts
        font = ImageFont.truetype(HankenGroteskBold, 20)

        # Calculate the positioning and draw the text
        for country in countries:
            text = str(countries[country]) + ": " + str(new_cases[0])
            width, height = font.getsize(text)
            center = int((self.inky.WIDTH - width) / 2)
            draw.text((center, self.current_height), text, self.inky.BLACK, font=font)
            self.current_height += height
            new_cases.pop(0)

        # Display the completed picture
        self.inky.set_image(img)
        self.inky.show()
