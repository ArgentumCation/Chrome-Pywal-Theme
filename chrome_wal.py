import json
import os
from PIL import Image
import PIL

colors = json.loads(open( os.path.expanduser("~/.cache/wal/colors.json"), "r").read())['colors']


with Image.open('images/theme_frame.png') as im:
    im.paste(PIL.ImageColor.getrgb(colors['color3']),[0,0,im.size[0],im.size[1]])
    im.save('images/theme_frame.png')



with Image.open("images/theme_toolbar.png") as im:
    im.paste(PIL.ImageColor.getrgb(colors['color1']),[0,0,im.size[0],im.size[1]])
    im.save("images/theme_toolbar.png")

with Image.open( "images/theme_tab_background.png") as im:
    im.paste(PIL.ImageColor.getrgb(colors['color0']),[0,0,im.size[0],im.size[1]])
    im.save( "images/theme_tab_background.png")  

theme = {
    "name": "Pywal Chrome",
    "version": "1.0",
    "description": "",
    "manifest_version": 2,
    "theme": {
        "images": {
            "theme_frame": "images/theme_frame.png",
            "theme_toolbar": "images/theme_toolbar.png",
            "theme_tab_background": "images/theme_tab_background.png",
            "theme_frame_inactive":"images/theme_tab_background.png"
        },
        "colors": {
            "frame": PIL.ImageColor.getrgb(colors['color0']),
            "toolbar": PIL.ImageColor.getrgb(colors['color0']),
            "tab_text": PIL.ImageColor.getrgb(colors['color7']),
            "tab_background_text": PIL.ImageColor.getrgb(colors['color7']),
            "bookmark_text": PIL.ImageColor.getrgb(colors['color7']),
            "ntp_background": PIL.ImageColor.getrgb(colors['color0']),
            "ntp_text": PIL.ImageColor.getrgb(colors['color7']),
            "ntp_link": PIL.ImageColor.getrgb(colors['color7']),
            
            "button_background": PIL.ImageColor.getrgb(colors['color0']) + tuple([1])
        },
        "tints": {
            "buttons": [
                0.65,
                0.23,
                0.9
            ],
            "frame_inactive":[
                0,0,0]
        },
        "properties": {
            "ntp_background_alignment": "bottom",
            "ntp_background_repeat": "no-repeat"
        }
    }}
with open('manifest.json', 'w') as outfile:
    json.dump(theme, outfile)
