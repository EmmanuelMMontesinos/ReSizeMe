import os
from PIL import Image
from rembg import remove
from componets.options import Options
import flet as ft


def convert(
    output_text,
    input_folderl: list[str],
    output_folder: str,
    resulution: str,
    form="mismo",
    zip="misma",
    remove_bg=False) -> None:
    
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
            if input_folder.endswith(Options.FORMATS_OUTPUTS.value):

                items = input_folder.split("\\")
                filename = items[-1]
                image = Image.open(input_folder)
                if resulution[-1] == "%":
                    resulution_format = float(resulution[:-1]) / 100
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
                    filename_, form_ = filename.split(".")
                output_path = os.path.join(output_folder, filename)
                if zip == "misma":
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
                result = ft.Text(f"✔️ {filename} redimensionada\n")
                output_text.controls.append(result)
                output_text.update()
            elif not input_folder.endswith(Options.FORMATS_OUTPUTS.value):
                result=ft.Text(
                    f"Error de Formato {input_folder} no es un formato soportado")
                output_text.controls.append(result)
                output_text.update()
    result = ft.Text(f"Tarea Completada! {image_done} imagen/es ha/n sido guardada/s en {output_folder}")
    output_text.controls.append(result)
    output_text.update()