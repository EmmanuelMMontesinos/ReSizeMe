import flet as ft
from componets.options import Options
from componets.convert import convert

def generate_combox(combox):
    data = []
    for n in combox.value:
        finale = ft.dropdown.Option(n)
        data.append(finale)
    return data

def main(page: ft.Page):
    def send_info(e):
        if switch_resolutions.value:
            if custom_resolution != "":
                resolution = custom_resolution.value
            else:
                resolution = combox_resolutions.value
        if switch_formats:
            format_out = combox_formats.value
        if switch_compres:
            compres = combox_compres.value
        if switch_bg:
            bg = True
        if (input_files,input_dir) != "":
            convert(page,input_files,input_dir,resolution,format_out,compres,bg)
            
    def change_status(e):   
        options_gui = [
            (switch_resolutions.value, combox_resolutions, custom_resolution),
            (switch_formats.value, combox_formats),
            (switch_compres.value, combox_compres),
            (switch_bg.value,)
        ]
        for option in options_gui:
            if not option[0]:
                for combox in option[1:]:            
                    combox.disabled = True
                    combox.update()
            else:
                for combox in option[1:]:            
                    combox.disabled =False
                    combox.update()
    
    def give_files(e):
        input_files.value = e.files if e.files else ""
        input_files.update()
    
    def give_dir(e):
        input_dir.value = e.path if e.path else ""
        input_dir.update()
        
    def change_bg(e):
        if switch_bg.value:
            combox_formats.value = Options.FORMATS.value[2]
            combox_formats.disabled = True
            combox_formats.update()
            switch_formats.disabled = True
            switch_formats.update()
        else:
            combox_formats.disabled = False
            combox_formats.update()
            switch_formats.disabled = False
            switch_formats.update()
            

    # Layout init
    layout = ft.Column(
        expand=True)
    
    # Path
    path_field = ft.Column()
    file_field = ft.Row()
    dir_field = ft.Row()
    
    # serch_files = ft.FilePicker(on_result=give_files)
    input_files = ft.TextField(
        hint_text="Imagen/es de origen",
        expand=True)
    
    # serch_dir = ft.FilePicker(on_result=give_dir)
    input_dir = ft.TextField(
        hint_text="Carpeta salida",
        expand=True)
    
    # page.overlay.append(serch_dir)     
    # page.overlay.append(serch_files)
    button_files = ft.OutlinedButton(
        icon=ft.icons.IMAGE,
        icon_color="blue800",
        text="Seleccionar",
        # on_click=serch_files.pick_files(allow_multiple=True)
        )
    button_dir = ft.OutlinedButton(
        icon=ft.icons.DRIVE_FILE_MOVE_RTL,
        icon_color="yellow800",
        text="Seleccionar")
    
    # Options
    options_field = ft.Column(expand=True)
    
    # Resolutions
    resolutions_field = ft.Row()
    options_resolutions = ft.Column()
    switch_resolutions = ft.Switch(
        "Cambiar la resolución",
        on_change=change_status,
        active_color="purple500",
        label_position=ft.LabelPosition.LEFT
    )
    custom_resolution = ft.TextField(
        hint_text="Ej: 1920x1080 o 350%",
        disabled= True
    )
    combox_resolutions = ft.Dropdown(
        label="Resoluciones Predefinidas",
        options=generate_combox(Options.RESOLUTIONS),
        disabled= True,
    )
    
    # Formats
    formats_field = ft.Column()
    options_formats = ft.Column()
    switch_formats = ft.Switch(
        "Cambiar el formato",
        on_change=change_status,
        active_color="purple500",
        label_position=ft.LabelPosition.LEFT
    )
    combox_formats = ft.Dropdown(
        label="Formatos Posibles",
        options=generate_combox(Options.FORMATS),
        disabled=True,
        alignment=ft.alignment.center_left
    )
    
    # Compres
    compres_field = ft.Column()
    options_compres = ft.Column()
    switch_compres = ft.Switch(
        "Comprimir",
        on_change=change_status,
        active_color="purple500",
        label_position=ft.LabelPosition.LEFT
        )
    combox_compres = ft.Dropdown(
        label="Nivel de Compresión",
        options=generate_combox(Options.COMPRES),
        disabled=True,
    )
    
    # Background
    switch_bg = ft.Switch(
        "Quiero quitar el fondo",
        active_color="purple500",
        label_position=ft.LabelPosition.LEFT,
        on_change=change_bg
        )
    
    # Button Convert
    button_converse = ft.OutlinedButton(
        text="Convertir",
        icon=ft.icons.VERTICAL_ALIGN_CENTER,
        icon_color="green400",
        on_click=send_info,
        expand=True
        )
    
    # Info Output
    info_field = ft.ListView(
        auto_scroll=True
        )
    
    """ Add componets """
    
    file_field.controls.append(input_files)
    file_field.controls.append(button_files)
    
    dir_field.controls.append(input_dir)
    dir_field.controls.append(button_dir)
    
    path_field.controls.append(file_field)
    path_field.controls.append(dir_field)
    
    card_path = ft.Container(content=path_field)
    
    options_resolutions.controls.append(combox_resolutions)
    options_resolutions.controls.append(custom_resolution)
    
    resolutions_field.controls.append(switch_resolutions)
    resolutions_field.controls.append(options_resolutions)
    card_resolutions = ft.Container(content=resolutions_field)
    
    options_formats.controls.append(combox_formats)
    formats_field.controls.append(switch_formats)
    formats_field.controls.append(options_formats)
    card_formats = ft.Container(content=formats_field)
    
    options_compres.controls.append(combox_compres)
    compres_field.controls.append(switch_compres)
    compres_field.controls.append(options_compres)
    card_compres = ft.Container(content=compres_field)
    
    options_field.controls.append(card_resolutions)
    options_field.controls.append(card_formats)
    options_field.controls.append(card_compres)
    
    options_field.controls.append(switch_bg)
    
    converst_field = ft.Row()
    converst_field.controls.append(button_converse)
    
    layout.controls.append(card_path)
    layout.controls.append(options_field)
    layout.controls.append(converst_field)
    layout.controls.append(info_field)
    
    page.add(layout)
    page.title = "ReSizeME V2"
    page.window_height = 680
    page.window_width = 550
    page.update()
ft.app(target=main)
