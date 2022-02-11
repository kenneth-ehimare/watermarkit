# def add_image():
#     image_dialog = Tk()
#     image_dialog.title('Select preferences')
#     image_dialog.config(padx=20, pady=20)
#
#     select_button = Button(image_dialog, text='Choose image', command=load_windows)
#     select_button.grid(row=0, column=0)
#
#     path = Entry(image_dialog)
#     path.insert(0, load_windows())
#     path.grid(row=0, column=1)
#     return image_dialog

# loaded_files = canvas.create_text(70, 70, text='Add files here.', anchor='nw')
# canvas.grid(row=1, column=0, columnspan=2

# with Image.open('img.jpg').convert('RGBA') as img:
#     text = Image.new('RGBA', img.size, (255, 255, 255, 0))
#
#     draw = ImageDraw.Draw(text)
#     font = ImageFont.truetype('Merriweather-Regular.ttf', 72)
#     logo = Image.open('logo.png').convert('RGBA')
#     mask = Image.new('RGBA', logo.size, (255, 255, 255, 128))
#
#     draw.text((960, 640), 'Leo Mendes', (255, 255, 255, 128), font, align='center', anchor='mm')
#     # draw.text((960, 640), logo, (255, 255, 255, 128), font, align='center', anchor='mm')
#
#     img.paste(logo, (960, 640), mask)
#
#     output = Image.alpha_composite(img, text)
#
#     print(img.size)

#     output.show()
#
#
# print(logo.size)
