import tkinter.font as tkfont


def configure():    #This function customizes the default font styles
    # family = "Segoe UI"
    family = "Helvetica"    #The current default font being applied
    default_font = tkfont.nametofont("TkDefaultFont")   #Set the default font for widgets like Button, Label, etc.
    default_font.configure(size=15, family=family)
    text_font = tkfont.nametofont("TkTextFont")     #Set the default font for widgets like Text and ScrolledText.
    text_font.configure(size=12, family=family)
    fixed_font = tkfont.nametofont("TkFixedFont")   #Get the font for Fixed-Width text (like code or monospaced text)
    fixed_font.configure(size=12, family=family)

def get_h1_font(root=None):     #This function returns a bold, large-sized font suitable for main headers
    return tkfont.Font(root=root, family="Segoe UI", size=18, weight="bold")
