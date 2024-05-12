from enum import Enum

class Options(Enum):
    RESOLUTIONS = (
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
    )
    
    FORMATS = (
        '.jpg',
        '.jpeg',
        '.png',
        '.webp',
        '.svg'
    )
    
    FORMATS_OUTPUTS = (
        '.jpg',
        '.jpeg',
        '.png',
        '.webp',
    )
    
    COMPRES = (
        "mínima",
        "normal",
        "máxima"
    )