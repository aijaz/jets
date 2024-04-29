from PIL import Image, ImageDraw, ImageFont

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cell_bgs = [('gray', (58, 58, 60)), ('yellow', (181, 158, 59)), ('green', (83, 141, 78))]
key_bgs = [('gray', (58, 58, 60)), ('yellow', (181, 158, 59)), ('green', (83, 141, 78)), ('light_gray', (129, 131, 132))]

fnt = ImageFont.truetype('/Library/Fonts/SF-Pro-Display-Bold.otf', 24)
kfnt = ImageFont.truetype('/Library/Fonts/SF-Pro-Display-Bold.otf', 14)

for letter in letters:
    for dirname, bgcolor in cell_bgs:
        img = Image.new('RGB', (56, 56), color=bgcolor)
        d = ImageDraw.Draw(img)
        d.text((28, 36), letter, font=fnt, fill=(255, 255, 255), align='center', anchor='mb')

        img.save(f'images/cells/{dirname}/{letter}.png')

    img = Image.new('RGB', (56, 56), color=(0, 0, 0))
    d = ImageDraw.Draw(img)
    d.text((28, 36), letter, font=fnt, fill=(255, 255, 255), align='center', anchor='mb')
    d.line([(1, 0), (54, 0), (54, 55), (1, 55), (1, 0)], (79, 79, 79), width=2)
    img.save(f'images/cells/current/{letter}.png')

    for dirname, bgcolor in key_bgs:
        img = Image.new('RGB', (36, 60), color="black")
        d = ImageDraw.Draw(img)
        d.rounded_rectangle((0, 0, 36, 60), radius=12, fill=bgcolor)
        d.text((18, 34), letter, font=kfnt, fill=(255, 255, 255), align='center', anchor='mb')

        img.save(f'images/keys/{dirname}/{letter}.png')


img = Image.new('RGB', (56, 56), color=(0, 0, 0))
d = ImageDraw.Draw(img)
d.line([(1, 0), (54, 0), (54, 55), (1, 55), (1, 0)], (79, 79, 79), width=2)
img.save(f'images/cells/blank.png')

img = Image.new('RGB', (54, 60), color="black")
d = ImageDraw.Draw(img)
d.rounded_rectangle((0, 0, 54, 60), radius=12, fill=(129, 131, 132))
d.text((27, 34), "ENTER", font=kfnt, fill=(255, 255, 255), align='center', anchor='mb')
img.save(f'images/keys/enter.png')

img = Image.new('RGB', (54, 60), color="black")
d = ImageDraw.Draw(img)
d.rounded_rectangle((0, 0, 54, 60), radius=12, fill=(129, 131, 132))
d.text((27, 34), "⌫", font=kfnt, fill=(255, 255, 255), align='center', anchor='mb')
img.save(f'images/keys/backspace.png')



