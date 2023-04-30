import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog

class PhotoViewer:
    def __init__(self, master):
        self.master = master
        self.master.title("Photo Viewer")
        self.master.geometry("1250x750")
        self.master.resizable(True, True)
        self.zoom_level = 100
        self.current_index = -1
        self.image_list = []

        # create a new frame for the buttons
        self.button_frame = tk.Frame(self.master)

        # add the buttons to the button frame
        button_specs = [
            ["Open", self.open_image],
            ["Save", self.save_image],
            ["+", self.zoom_in],
            ["-", self.zoom_out],
            ["Rotate Left", self.rotate_left],
            ["Rotate Right", self.rotate_right],
            ["Flip Horizontal", self.flip_horizontal],
            ["Flip Vertical", self.flip_vertical],
            ["<", self.prev_image],
            [">", self.next_image],
        ]
        for spec in button_specs:
            button = tk.Button(
                self.button_frame,
                text=spec[0],
                command=spec[1],
                relief="solid",
                bd=0,
                padx=10,
                pady=10,
                bg="#333",
                fg="white",
                font=("Helvetica", 12, "bold"),
                borderwidth=0,
                highlightthickness=0,
                activebackground="#555",
            )
            button.pack(side="left")

        self.button_frame.pack(side="bottom", pady=10)

        # create a new frame for the image
        self.image_frame = tk.Frame(self.master)
        self.image_frame.pack(fill="both", expand=True)

        # add a canvas to the image frame
        self.canvas = tk.Canvas(self.image_frame)
        self.canvas.pack(side="left", fill="both", expand=True)

        # add a scrollbar to the image frame
        self.scrollbar = tk.Scrollbar(self.image_frame, orient="vertical")
        self.scrollbar.pack(side="right", fill="y")

        # link the scrollbar to the canvas
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.canvas.yview)

        # create a new frame for the image in the canvas
        self.image_canvas = tk.Frame(self.canvas)

        # add the image frame to the canvas
        self.canvas.create_window(
            (0, 0), window=self.image_canvas, anchor="nw", tags="self.image_canvas"
        )

        # bind the mousewheel to the zoom function
        self.master.bind("<MouseWheel>", self.zoom)

    def open_image(self):
        file_path = filedialog.askopenfilename(
            title="Select Image", filetypes=("PNG .png", "*.jpg *.png")
        )
        if file_path:
            # create a new image object
            image = Image.open(file_path)

            # add the image to the list
            self.image_list.append(image)
            self.current_index = len(self.image_list) - 1

            self.display_image()

    def save_image(self):
        if self.current_index != -1:
            file_path = filedialog.asksaveasfilename(
                title="Save Image",
                filetypes=[("JPEG Image", "*.jpg"), ("PNG Image", "*.png")],
                defaultextension=".png",
            )
            if file_path:
                self.image_list[self.current_index].save(file_path)

    def zoom(self, event):
        if self.current_index != -1:
            if event.delta > 0:
                self.zoom_in()
            else:
                self.zoom_out()

    def zoom_in(self):
        if self.current_index != -1:
            image = self.image_list[self.current_index]
            width, height = image.size
            new_width = int(width * 1.1)
            new_height = int(height * 1.1)
            image = image.resize((new_width, new_height), Image.ANTIALIAS)
            self.image_list[self.current_index] = image
            self.display_image()

    def zoom_out(self):
        if self.current_index != -1:
            image = self.image_list[self.current_index]
            width, height = image.size
            new_width = int(width / 1.1)
            new_height = int(height / 1.1)
            image = image.resize((new_width, new_height), Image.ANTIALIAS)
            self.image_list[self.current_index] = image
            self.display_image()

    def rotate_left(self):
        if self.current_index != -1:
            image = self.image_list[self.current_index].rotate(90, expand=True)
            self.image_list[self.current_index] = image
            self.display_image()

    def rotate_right(self):
        if self.current_index != -1:
            image = self.image_list[self.current_index].rotate(-90, expand=True)
            self.image_list[self.current_index] = image
            self.display_image()

    def flip_horizontal(self):
        if self.current_index != -1:
            image = self.image_list[self.current_index].transpose(Image.FLIP_LEFT_RIGHT)
            self.image_list[self.current_index] = image
            self.display_image()

    def flip_vertical(self):
        if self.current_index != -1:
            image = self.image_list[self.current_index].transpose(Image.FLIP_TOP_BOTTOM)
            self.image_list[self.current_index] = image
            self.display_image()

    def prev_image(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.display_image()

    def next_image(self):
        if self.current_index < len(self.image_list) - 1:
            self.current_index += 1
            self.display_image()

    def display_image(self):
        if self.current_index != -1:
            # get the current image
            image = self.image_list[self.current_index]

            # resize the image to fit the window
            width, height = image.size
            ratio = width / height
            if width > height:
                width = min(width, 1000)
                height = width / ratio
            else:
                height = min(height, 500)
                width = height * ratio

           # image = image.resize((int(width), int(height)))
            # create a photo image from the PIL image
            photo = ImageTk.PhotoImage(image)
                    # set the photo image on the canvas
            self.canvas.delete("all")
            self.canvas.config(scrollregion=(0, 0, width, height))
            self.canvas.create_image(0, 0, image=photo, anchor="nw")

            # update the canvas
            self.canvas.update()

            # store a reference to the photo image to prevent garbage collection
            self.canvas.image = photo
 
root = tk.Tk()
app = PhotoViewer(root)
root.mainloop()

               

