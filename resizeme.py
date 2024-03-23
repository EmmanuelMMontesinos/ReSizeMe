import os
from PIL import Image
import tkinter as tk
from tkinter import Tk, filedialog, ttk, messagebox, END
from ttkbootstrap import Style

# Supported image formats and resolutions
FORMATOS = ('.jpg', '.jpeg', '.png', '.webp')

image_resolutions = [
    "50x50",
    "100x100",
    "200x200",
    "320x240",
    "400x300",
    "640x480",
    "800x600",
    "1024x768",
    "1280x720",
    "1366x768",
    "1600x900",
    "1920x1080",
    "2560x1440",
    "3840x2160",
    "4096x2160"
]


def resize_images(input_folderl: list[str], output_folder: str, resulution: str) -> None:
    """ Rescale the images according to the parameters given in the tkinder interface.

    :param input_folderl: Paths to file(s) for rescaling
    :type input_folderl: list[str]

    :param output_folder: Path where to save the rescaled file(s)
    :type output_folder: str

    :param resulution: Resolution desired by user for rescaling the image(s)
    :type resulution: str

    """
    image_done = 0
    resolutions = resulution.split("x")
    input_folders = input_folderl.split("*")
    target_width, target_height = resolutions
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for input_folder in input_folders:
        if len(input_folder) > 2:
            if input_folder[0] == "}":
                input_folder = input_folder[1:]
            if input_folder[0] == " ":
                input_folder = input_folder[1:]
            if input_folder[0] == "{":
                input_folder = input_folder[1:]
            if input_folder.endswith(FORMATOS):

                items = input_folder.split("/")
                filename = items[-1]
                image = Image.open(input_folder)
                resized_image = image.resize(
                    (int(target_width), int(target_height)))
                output_path = os.path.join(output_folder, filename)
                resized_image.save(output_path)
                image_done += 1
                print(f"✔️ {filename} redimensionada\n")
            elif not input_folder.endswith(FORMATOS):
                messagebox.showerror(
                    title="Error de Formato", message=f"{input_folder} no es un formato soportado")
    messagebox.showinfo(title="Tarea Completada!",
                        message=f"{image_done} imagen/es ha/n sido guardada/s en {output_folder}")


def select_value(camp: tuple[str]) -> None:
    """ Update source images for rescaling

    :param camp: Images previously selected
    :type camp: tuple[str]
    """
    new_camp = filedialog.askopenfilenames()
    new_camp_int = []
    for new in new_camp:
        new_camp_int.append(new+"*")
    camp.delete(0, END)
    camp.insert(0, new_camp_int)


def select_value_directory(camp: str) -> None:
    """ Update the desired directory to store the rescaled images

    :param camp: Path to the previously selected folder
    :type camp: str
    """
    new_camp = filedialog.askdirectory()
    camp.delete(0, END)
    camp.insert(0, new_camp)


def make_windows() -> None:
    """ Ui for users"""
    print("Programado por @emmanuelmmontesinos")
    windows = Tk()
    windows.title("ReSizeMe")
    windows.wm_iconbitmap("icono.ico")
    windows.resizable(0, 0)
    frame = tk.Frame(windows, borderwidth=20, border=10)
    frame_path = ttk.Labelframe(frame, text="Origen y Destino")
    frame_resolucion = ttk.Labelframe(frame, text="¿Que resolucion quieres?")
    style = Style(theme="flatly")
    style.configure("TButton")
    style.theme_use("superhero")
    origen = ttk.Entry(frame_path)
    destino = ttk.Entry(frame_path)
    ttk.Button(frame_path, text="Imagen/es Origen", padding=(15, 0, 15, 0), cursor="hand2",
               command=lambda: select_value(origen)).grid(row=1, column=0)
    ttk.Button(frame_path, text="Carpeta Destino", padding=(15, 0, 15, 0), cursor="hand2",
               command=lambda: select_value_directory(destino)).grid(row=3, column=0)
    origen.grid(row=0, column=0)
    destino.grid(row=2, column=0)
    resolution = ttk.Combobox(
        frame_resolucion, values=image_resolutions, cursor="hand2")
    resolution.grid(row=0, column=0)
    boton = ttk.Button(frame_resolucion, text="Ajustar", padding=(50, 0, 50, 0), command=lambda: resize_images(
        origen.get(), destino.get(), resolution.get()), cursor="hand2")
    frame.pack()
    resolution.current(11)
    boton.grid(row=1, column=0, ipady=10, pady=14)
    frame_resolucion.grid(row=0, column=1, padx=5)
    frame_path.grid(row=0, column=0)
    windows.mainloop()


if __name__ == "__main__":
    make_windows()
