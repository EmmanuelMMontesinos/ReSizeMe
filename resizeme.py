import os
from PIL import Image
from rembg import remove
import tkinter as tk
from tkinter import Tk, filedialog, ttk, messagebox, END
from ttkbootstrap import Style

from Package_Update.Update import UpdateApp

# Supported image formats and resolutions
FORMATOS = ('.jpg', '.jpeg', '.png', '.webp', '.ico')
FORMATOS_OUTPUT = ('.jpg', '.jpeg', '.png', '.webp', "mismo")

image_resolutions = [
    "misma",
    "10%",
    "20%",
    "30%",
    "40%",
    "50%",
    "60%",
    "70%",
    "80%",
    "90%",
    "100%",
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
level_zip = [
    "mismo",
    "mínima",
    "normal",
    "máxima"
]


def resize_images(input_folderl: list[str], output_folder: str, resulution: str, form="mismo", zip="misma",remove_bg=False) -> None:
    """ Rescale the images according to the parameters given in the tkinder interface.

    :param input_folderl: Paths to file(s) for rescaling
    :type input_folderl: list[str]

    :param output_folder: Path where to save the rescaled file(s)
    :type output_folder: str

    :param resulution: Resolution desired by user for rescaling the image(s)
    :type resulution: str

    :param form: Format the image(s) output
    :type form: str

    """
    image_done = 0

    input_folders = input_folderl.split("*")
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
                if resulution[-1] == "%":
                    resulution_format = float(resulution[:-1]) / 100
                    print(resulution)
                    target_width, target_height = image.size
                    target_width, target_height = target_width * \
                        resulution_format, target_height * resulution_format
                elif resulution != "misma":
                    target_width, target_height = resulution.split("x")
                elif resulution == "misma":
                    target_width, target_height = image.size
                resized_image = image.resize(
                    (int(target_width), int(target_height)))
                if remove_bg == True:
                    resized_image = remove(resized_image)
                if form != "mismo":
                    filename_new, old_form = filename.split(".")

                    filename = filename_new + form
                else:
                    filename_, form = filename.split(".")
                output_path = os.path.join(output_folder, filename)
                if zip == "mismo":
                    resized_image.save(output_path)
                else:
                    if zip == "mínima":
                        zip = 100
                    elif zip == "normal":
                        zip = 60
                    elif zip == "máxima":
                        zip = 35
                    resized_image.save(
                        output_path, quality=zip)

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


def change_format(camp: bool,format):
    check = camp.get()
    if check == True:
        format.current(2)
        format.configure(state="disabled")
    else:
        format.configure(state="enabled")




def make_windows() -> None:
    """ Ui for users"""
    print("Programado por @emmanuelmmontesinos\nVisita mi web: emmanuelmmontesinos.dev")
    windows = Tk()
    windows.geometry("250x400")
    windows.title("ReSizeMe")
    windows.wm_iconbitmap("icono.ico")
    windows.resizable(True, True)
    frame = tk.Frame(windows, borderwidth=20, border=10)
    frame_resolucion = ttk.Labelframe(frame, text="¿Qué resolucion quieres?")
    frame_path = ttk.Labelframe(frame_resolucion, text="Origen y Destino")
    frame_remove = ttk.Labelframe(frame_resolucion, text="¿Eliminar Fondo?")
    frame_zip = ttk.Labelframe(
        frame_resolucion, text="¿Qué nivel de compresión?")
    style = Style(theme="flatly")
    style.configure("TButton")
    style.theme_use("superhero")
    origen = ttk.Entry(frame_path)
    destino = ttk.Entry(frame_path)
    ttk.Button(frame_path, text="Imagen/es Origen", cursor="hand2",
               command=lambda: select_value(origen)).grid(row=1, column=0)
    ttk.Button(frame_path, text="Carpeta Destino", cursor="hand2",
               command=lambda: select_value_directory(destino)).grid(row=3, column=0)
    origen.grid(row=0, column=0)
    destino.grid(row=2, column=0)
    image_zip = ttk.Combobox(frame_zip,
                             values=level_zip,
                             cursor="hand2")
    image_zip.pack()
    resolution = ttk.Combobox(
        frame_resolucion, values=image_resolutions, cursor="hand2",)
    resolution.grid(row=0, column=0)
    frame_format = ttk.LabelFrame(frame_resolucion, text="Formato")
    format_output = ttk.Combobox(
        frame_format, values=FORMATOS_OUTPUT, cursor="hand2")
    format_output.grid()
    value_remove = tk.BooleanVar(value=False)
    remove_back = ttk.Checkbutton(frame_format,
        text="Borrar fondo",
        variable=value_remove,
        cursor="hand2",
        command=lambda:change_format(value_remove,format_output))
    remove_back.grid(pady=2)
    boton = ttk.Button(frame_resolucion, text="Ajustar", padding=(50, 0, 50, 0), command=lambda: resize_images(
        origen.get(), destino.get(), resolution.get(), format_output.get(), image_zip.get(),value_remove.get()), cursor="hand2")
    frame.pack()
    format_output.current(4)
    image_zip.current(0)
    resolution.current(0)
    frame_path.grid(pady=2)
    frame_resolucion.grid(pady=2)
    frame_zip.grid(pady=2)
    frame_format.grid(pady=2)
    frame_remove.grid(pady=2)
    boton.grid(column=0, ipady=10, pady=14)
    windows.mainloop()


if __name__ == "__main__":
    print("Iniciando ReSizeMe.\nSi es la primera vez que se abre este programa, puede tardar un poco en cargar.\n")
    app_name = "ReSizeMe"
    app_version = "1.5.0"
    url_repo = "https://github.com/EmmanuelMMontesinos/ReSizeMe"
    update = UpdateApp(app_name, app_version, url_repo)

    if update.check_update():
        case_update = input("Hay una nueva versión disponible. ¿Desea actualizar? (s/n): ")
        match case_update.lower():
            case "s":
                update.update()
            case "n":
                print("Gracias por usar ReSizeMe.")


    make_windows()
