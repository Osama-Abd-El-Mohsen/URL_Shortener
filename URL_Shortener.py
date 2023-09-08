import customtkinter as ctk
import pyshorteners,os
import pyperclip
from pyshorteners import tinyurl
from CTkMessagebox import CTkMessagebox

color_mode_list = ['Dark', 'Light']
shorten_url = ' '


def convert_button_func():
    global shorten_url
    copy_button.configure(
        text="Copy URL",
        fg_color='#2888C9',
        hover=True,
        text_color='white',
        font=ctk.CTkFont('Arial', 20)
    )
    py_shorten = pyshorteners.Shortener()
    url = input_Entry.get()

    if '.' in (url):
        try:
            output_Entry.delete(0, ctk.END)
            shorten_url = py_shorten.tinyurl.short(input_Entry.get())
            output_Entry.insert(ctk.END, shorten_url)
        except:
            output_Entry.delete(0, ctk.END)
            output_Entry.insert(ctk.END, 'Error')
    else:
        output_Entry.delete(0, ctk.END)
        output_Entry.insert(ctk.END, 'Error')


def change_apperance_mode(new_appearance_mode: str):
    ctk.AppearanceModeTracker.set_appearance_mode(new_appearance_mode)


def copy_button_func():
    if shorten_url != ' ':
        pyperclip.copy(shorten_url)
        copy_button.configure(text='Copied !',
                              fg_color='white', text_color='black', hover=False
                              )


if __name__ == '__main__':

    # config my app
    ctk.ThemeManager.load_theme('blue')
    ctk.AppearanceModeTracker.set_appearance_mode('system')
    ctk.deactivate_automatic_dpi_awareness()
    app = ctk.CTk()
    icon_path="\icon.ico"
    app.iconbitmap(os.getcwd()+icon_path)   
    app.title("Driver_Maker_Script\n ")
    app.geometry('600x380')
    app.resizable(False, False)
    app.grid_columnconfigure(2, weight=1)

    # opp

    titel_frame = ctk.CTkFrame(
        app,
        border_width=0
    )

    setting_frame = ctk.CTkFrame(
        app,
        border_width=0
    )

    owner_frame = ctk.CTkFrame(
        app,
        border_width=0
    )

    entry_frame = ctk.CTkFrame(
        app,
        border_width=0
    )

    shorten_label = ctk.CTkLabel(
        titel_frame,
        width=600,
        text="URL Shortener",
        font=ctk.CTkFont('Arial', 48, weight='bold'),
        text_color="#2888C9"
    )

    apperance_Label = ctk.CTkLabel(
        setting_frame,
        text="Appearance Mode",
        font=ctk.CTkFont('Arial', 18, weight='bold'),
    )

    owner_label1 = ctk.CTkLabel(
        owner_frame,
        text="Made with 💖 By",
        font=ctk.CTkFont('Arial', 18, weight='bold'),
    )
    owner_label2 = ctk.CTkLabel(
        owner_frame,
        text="Osama Abd EL Mohsen",
        font=ctk.CTkFont('Arial', 18, weight='bold'),
        text_color="#2888C9"
    )

    input_Entry = ctk.CTkEntry(
        entry_frame,
        placeholder_text="Enter URL",
        font=ctk.CTkFont('Arial', 20),
        width=400,
        height=48,
        border_width=0)

    output_Entry = ctk.CTkEntry(
        entry_frame,
        placeholder_text="URL output",
        font=ctk.CTkFont('Arial', 20),
        width=400,
        height=48,
        border_width=0)

    convert_button = ctk.CTkButton(
        entry_frame,
        text="Shorten URL",
        font=ctk.CTkFont('Arial', 20),
        command=convert_button_func,
        height=48
    )

    copy_button = ctk.CTkButton(
        entry_frame,
        text="Copy URL",
        font=ctk.CTkFont('Arial', 20),
        command=copy_button_func,
        height=48,
    )

    apperance_button = ctk.CTkOptionMenu(
        setting_frame,
        font=ctk.CTkFont('Arial', 20),
        values=['system', 'dark', 'light'],
        height=40,
        command=change_apperance_mode)

    owner_frame.grid(row=4, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew")

    titel_frame.grid(row=0, column=0, padx=10, pady=10,columnspan=3, sticky="ew")
    entry_frame.grid(row=1, column=0, padx=(10, 10),columnspan=2,  pady=(10, 10), sticky="nsew")
    setting_frame.grid(row=4, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

    shorten_label.grid(row=1, column=0, padx=10, pady=10)

    input_Entry.grid(row=2, column=0, padx=(10, 10), pady=(10, 10))
    output_Entry.grid(row=3, column=0, padx=(10, 10), pady=(10, 10))
    convert_button.grid(row=2, column=4, padx=(10, 10), pady=(10, 10))
    copy_button.grid(row=3, column=4, padx=(10, 10), pady=(10, 10))

    apperance_Label.grid(row=4, column=0, padx=(40, 10), pady=(10, 10), sticky="we")
    apperance_button.grid(row=5, column=0, padx=(40, 10),pady=(10, 10), sticky="we")

    owner_label1.grid(row=4, column=1, padx=(60, 10), pady=(30, 0), sticky="nsew")
    owner_label2.grid(row=5, column=1, padx=(60, 10), pady=(0, 10), sticky="nsew")

    app.mainloop()
