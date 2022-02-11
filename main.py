import pathlib
from tkinter import *
from tkinter import filedialog, colorchooser, messagebox
from PIL import Image, ImageDraw, ImageFont

# filedialog.askopenfilenames()
colors = ()


def load_windows():
    file = filedialog.askopenfile(initialdir="C:/Users/Kenneth.Okhueleigbe/Downloads", title='Select file')
    path_label.config(text=file.name)
    return file.name


def select_image():
    file = filedialog.askopenfile(initialdir="C:/Users/Kenneth.Okhueleigbe/Downloads", title='Select file')
    image_path.config(text=file.name)
    return file.name


def load_color():
    global colors
    color_picker = colorchooser.askcolor(color=(255, 255, 255), title='Choose Color')
    colors = color_picker[0]


def add_image():
    try:
        with Image.open(path_label.cget('text')) as img:
            img_copy = img.copy()
    except [AttributeError, FileNotFoundError]:
        messagebox.showerror('Oops!', 'Invalid file path')
    else:
        im_format = img.format

        logo = Image.open(f"{image_path.cget('text')}").convert('RGBA')
        logo_copy = logo.copy()

        positionz = image_position(img_copy, logo_copy)

        mask = Image.new('RGBA', logo_copy.size, (255, 255, 255, 128))

        img_copy.paste(logo_copy, positionz[pos_var.get()], mask)
        # img_copy.show()
        img_copy.save(f"C:/Users/Kenneth.Okhueleigbe/Downloads/WatermarkIt/Image1.{im_format}")

        messagebox.showinfo('Add Image', 'Successful')

        path_label.config(text='')
        image_path.config(text='')


def add_text():
    try:
        img = Image.open(path_label.cget('text'))
        im_format = img.format
        conv_img = img.convert('RGBA')
        text = Image.new('RGBA', img.size, (255, 255, 255, 0))
    except [AttributeError, FileNotFoundError]:
        messagebox.showerror('Oops!', 'Invalid file path')
    else:
        draw = ImageDraw.Draw(text)

        font = ImageFont.truetype('Merriweather-Regular.ttf', int(font_size.get()))

        r = colors[0]
        g = colors[1]
        b = colors[2]

        position = text_location(img, font_size)

        draw.text(position[text_pos.get()], watermark_text.get(), (r, g, b, 128), font, anchor='mm')
        # print(font.getsize(watermark_text.get()))

        output = Image.alpha_composite(conv_img, text)
        img_file = output.convert('RGB')
        img_file.show()

        img_file.save(f"C:/Users/Kenneth.Okhueleigbe/Downloads/WatermarkIt/Image.{im_format}")

        messagebox.showinfo('Add Image', 'Successful')

        path_label.config(text='')
        watermark_text.delete(0, 'end')
        font_size.delete(0, 'end')


def image_position(image, watermark):
    positionz = {}

    isize_x = image.size[0]
    isize_y = image.size[1]

    wsize_x = watermark.size[0]
    wsize_y = watermark.size[1]

    positionz['top-left'] = (0, 0)
    positionz['top-right'] = (isize_x-wsize_x, 0)
    positionz['center'] = (int(isize_x/2-wsize_x/2), int(isize_y/2-wsize_y/2))
    positionz['bottom-left'] = (0, isize_y-wsize_y)
    positionz['bottom-right'] = (isize_x-wsize_x, isize_y-wsize_y)
    return positionz


def text_location(image, f_size):
    text_posit = {}

    i_x = image.size[0]
    i_y = image.size[1]

    w_x = 256 + 20
    w_y = int(f_size.get())

    text_posit['top-left'] = (w_x, w_y+20)
    text_posit['top-right'] = (i_x-w_x, w_y+20)
    text_posit['center'] = (int(i_x/2), int(i_y/2))
    text_posit['bottom-left'] = (w_x, i_y-w_y-20)
    text_posit['bottom-right'] = (i_x-w_x, i_y-w_y-20)
    return text_posit


window = Tk()
window.title('WatermarkIt')
window.config(width=600, height=400, pady=15)

# ----------------------------------------- Upper Level Container ------------------------------------------------------
# frame = Frame(window)
# frame.grid(row=0, column=0)

# ----------------------------------------- Select Image Container -----------------------------------------------------
add_file = Frame(window)
add_file.grid(row=0, column=0, columnspan=2, padx=30, pady=15)

load_button = Button(add_file, text='Load Image', command=load_windows)
load_button.grid(row=0, column=0, padx=6)

path_label = Label(add_file, width=100)
path_label.grid(row=0, column=1, padx=15)

# ----------------------------------------- Image Watermark Container --------------------------------------------------
add_image_frame = Frame(window)
add_image_frame.grid(row=1, column=0, padx=30)

# Sub-Container
shape_frame = LabelFrame(add_image_frame, text='Add Image', padx=15, pady=15, width=250, height=250)
shape_frame.grid(row=0, column=0)

# LabelFrame widgets
img_button = Button(shape_frame, text='Select Image', command=select_image)
img_button.grid(row=0, column=0)

image_path = Label(shape_frame, bg='aquamarine')
image_path.config(width=30)
image_path.grid(row=0, column=1, padx=30)

size_label = Label(shape_frame, text='Size')
size_label.grid(row=1, column=0, sticky='w')

size_options = ['small', 'medium', 'large']
size_var = StringVar()
size_var.set('Choose Size')
size_menu = OptionMenu(shape_frame, size_var, *size_options)
size_menu.config(width=30)
size_menu.grid(row=1, column=1, pady=15)

position_label = Label(shape_frame, text='Position')
position_label.grid(row=2, column=0, sticky='w')

positions = ['top-left', 'top-right', 'center', 'bottom-left', 'bottom-right']
pos_var = StringVar()
pos_var.set('Choose Position')
positions_menu = OptionMenu(shape_frame, pos_var, *positions)
positions_menu.config(width=30)
positions_menu.grid(row=2, column=1)

add_button = Button(shape_frame, text='Add Watermark', command=add_image, width=30)
add_button.grid(row=3, column=1, pady=15)

# ----------------------------------------- Text Watermark Container --------------------------------------------------
add_text_frame = Frame(window)
add_text_frame.grid(row=1, column=1, padx=30)

# Content Widgets
text_frame = LabelFrame(add_text_frame, text='Add Text', padx=15, pady=15, width=250, height=250)
text_frame.grid(row=1, column=1)

text_label = Label(text_frame, text='Type Text')
text_label.grid(row=0, column=0)

watermark_text = Entry(text_frame, width=35)
watermark_text.grid(row=0, column=1, padx=30)

text_size_label = Label(text_frame, text='Size')
text_size_label.grid(row=1, column=0, sticky='w')

font_size = Entry(text_frame, width=35)
font_size.grid(row=1, column=1, pady=15)

text_position = Label(text_frame, text='Position')
text_position.grid(row=2, column=0, sticky='w')

positions = ['top-left', 'top-right', 'center', 'bottom-left', 'bottom-right']
text_pos = StringVar()
text_pos.set('Choose Position')
positions_menu = OptionMenu(text_frame, text_pos, *positions)
positions_menu.config(width=30)
positions_menu.grid(row=2, column=1)

color = Button(text_frame, text='Color', command=load_color, width=30)
color.grid(row=3, column=1, pady=15)

add_button = Button(text_frame, text='Add Watermark', command=add_text, width=30)
add_button.grid(row=4, column=1)



window.mainloop()
