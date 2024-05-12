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
        format_out = "mismo"
        compres = "misma"
        bg = False
        if switch_resolutions.value:
            if custom_resolution.value != "":
                resolution = custom_resolution.value
            else:
                resolution = combox_resolutions.value
        else:
            resolution = "misma"
        if switch_formats.value:
            if not switch_bg.value:
                format_out = combox_formats.value
            else:
                format_out = "mismo"
        else:
            format_out = ".png"
        if switch_compres.value:
            compres = combox_compres.value
        if switch_bg.value:
            bg = True
        if input_files.value and input_dir.value != "":
            convert(info_field,input_files.value,input_dir.value,resolution,format_out,compres,bg)
        else:
            info_field.controls.append(
                ft.OutlinedButton(
                    icon=ft.icons.ERROR,
                    text="ERROR: Por favor, revise los parametros.",
                    icon_color="red1000"))
            info_field.update()
            
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
        for images in e.files:
            if images.path:
                input_files.value += images.path + "*"
        # input_files.value = e.files.path if e.files else ""
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
            if switch_formats.value:     
                combox_formats.disabled = False
                combox_formats.update()
            switch_formats.disabled = False
            switch_formats.update()
            
    # Path
    path_field = ft.Column()
    file_field = ft.Row()
    dir_field = ft.Row()
    
    serch_files = ft.FilePicker(on_result=give_files)
    serch_dir = ft.FilePicker(on_result=give_dir)
    page.overlay.append(serch_files)
    page.overlay.append(serch_dir)     
    
    input_files = ft.TextField(
        hint_text="Imagen/es de origen",
        expand=True)
    
    input_dir = ft.TextField(
        hint_text="Carpeta salida",
        expand=True)
    
    button_files = ft.OutlinedButton(
        icon=ft.icons.IMAGE,
        icon_color="blue200",
        text="Seleccionar",
        on_click= lambda _: serch_files.pick_files(allow_multiple=True)
        )
    button_dir = ft.OutlinedButton(
        icon=ft.icons.DRIVE_FILE_MOVE_RTL,
        icon_color="blue200",
        text="Seleccionar",
        on_click= lambda _: serch_dir.get_directory_path())
    

    # Layout init
    layout = ft.Column(
        expand=True)
    
    
    # Options
    options_field = ft.Column(expand=True)
    
    # Resolutions
    resolutions_field = ft.Row()
    options_resolutions = ft.Column()
    switch_resolutions = ft.Switch(
        "Cambiar la resolución",
        on_change=change_status,
        active_color="green200",
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
        active_color="green200",
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
        active_color="green200",
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
        active_color="green200",
        label_position=ft.LabelPosition.LEFT,
        on_change=change_bg
        )
    
    # Button Convert
    button_converse = ft.FilledButton(
        text="Convertir",
        icon=ft.icons.VERTICAL_ALIGN_CENTER,
        icon_color="red800",
        on_click=send_info,
        expand=True,
        adaptive= True,
        style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN_200,)
        )
    
    # Info Output
    info_field = ft.ListView(
        auto_scroll=True,
        height=80,
        )
        
    layout_info = ft.Container(content=info_field,
                               adaptive= True)
    
    
    """ Add componets """
    
    file_field.controls.append(input_files)
    file_field.controls.append(button_files)
    
    dir_field.controls.append(input_dir)
    dir_field.controls.append(button_dir)
    
    path_field.controls.append(file_field)
    path_field.controls.append(dir_field)
    
    card_path = ft.Container(content=path_field)
    card_path.adaptive = True
    
    
    options_resolutions.controls.append(combox_resolutions)
    options_resolutions.controls.append(custom_resolution)
    options_resolutions.adaptive = True
    
    resolutions_field.controls.append(switch_resolutions)
    resolutions_field.controls.append(options_resolutions)
    card_resolutions = ft.Container(content=resolutions_field)
    card_resolutions.adaptive = True
    card_resolutions.expand = True
    
    options_formats.controls.append(combox_formats)
    formats_field.controls.append(switch_formats)
    formats_field.controls.append(options_formats)
    card_formats = ft.Container(content=formats_field)
    card_formats.adaptive = True
    card_formats.expand = True
    
    options_compres.controls.append(combox_compres)
    compres_field.controls.append(switch_compres)
    compres_field.controls.append(options_compres)
    card_compres = ft.Container(content=compres_field)
    card_compres.adaptive = True
    card_compres.expand = True
    
    options_field.controls.append(card_resolutions)
    options_field.controls.append(card_formats)
    options_field.controls.append(card_compres)
    
    options_field.controls.append(switch_bg)
    options_field.adaptive = True
    
    converst_field = ft.Row()
    converst_field.controls.append(button_converse)
    
    layout.controls.append(card_path)
    layout.controls.append(options_field)
    layout.controls.append(converst_field)
    layout.controls.append(layout_info)
    

    page.add(layout)
    page.title = "ReSizeME V2"
    page.window_height = 750
    page.window_width = 550
    # page.window_resizable = False
    page.update()
ft.app(target=main)
