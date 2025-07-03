import tkinter.font as tkfont


def configure():
    # family = "Segoe UI"
    family = "Helvetica"
    default_font = tkfont.nametofont("TkDefaultFont")
    default_font.configure(size=15, family=family)
    text_font = tkfont.nametofont("TkTextFont")
    text_font.configure(size=12, family=family)
    fixed_font = tkfont.nametofont("TkFixedFont")
    fixed_font.configure(size=12, family=family)

def get_h1_font(root=None):
    return tkfont.Font(root=root, family="Segoe UI", size=18, weight="bold")

def get_ht_font(root=None):
    return tkfont.Font(root=root, family="Segoe UI", size=8, weight="bold")