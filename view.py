import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from rail_fence import decrypt_message_rail_fence, encrypt_message_rail_fence
from columnar_transposition import (
    decrypt_columnar_transposition_b,
    encrypt_columnar_transposition_b,
    decrypt_columnar_transposition_a,
    encrypt_columnar_transposition_a,
)


NORM_FONT = ("Verdana", 10)


def start_app():
    root = BskApp()
    root.geometry("720x500")
    root.mainloop()


class BskApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        self.frame = MainPage(self, container)
        self.frame.pack()


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.top_frame = tk.Frame(
            self, bg="gray22", width=600, height=100, pady=5, padx=5
        )
        self.center_frame = CenterFrame(self, controller)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.top_frame.grid(row=0, sticky="ew")
        self.center_frame.grid(row=1, sticky="nsew")

        self.logo = tk.Label(
            self.top_frame,
            text="BSK APP",
            bg="gray22",
            fg="gray63",
            width="100",
            height="2",
            font=("Verdana", 20, "bold"),
        ).pack()


class CenterFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg="gray5", width=1280, height=620)
        self.menu = Menu(self)
        self.user_data = RightFrame(self, controller)
        self.data = None
        self.switch_frame(DataFrame)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.menu.grid(row=0, column=0, sticky="ns")
        self.user_data.grid(row=0, column=2, sticky="ns")

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self.data is not None:
            self.data.destroy()
        self.data = new_frame
        self.data.grid(row=0, column=1, sticky="nsew")


class DataFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.config(width=880, height=620, padx=3, pady=3)


class RightFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg="gray31", width=50, height=620, padx=3, pady=3)


class Menu(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.config(bg="gray30", width=200, height=620, padx=3)
        button1 = tk.Button(
            self,
            text="Implementacja podstawowych modułów kryptograficznych",
            fg="gray68",
            bg="gray14",
            font=("calibri", 10, "bold"),
            height=3,
            command=lambda: parent.switch_frame(BasicCryptographyFrame),
        )
        button1.grid(column=0, row=1, pady=3)


class BasicCryptographyFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.config(width=880, height=620, padx=3, pady=3, bg="gray70")
        self.option_frame = tk.Frame(self)
        self.data_frame = tk.Frame(self)
        self.option_frame.config(width=300, height=620, padx=3, pady=3, bg="gray70")
        self.data_frame.config(width=580, height=620, padx=3, pady=3, bg="snow")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.option_frame.grid(row=0, column=1, sticky="nsew")
        self.data_frame.grid(row=0, column=0, sticky="nsew")
        self.option_label = tk.Label(
            self.option_frame,
            text="OPCJE",
            bg="gray70",
            fg="gray21",
            font=("calibri", 11, "bold"),
        ).pack()
        sep = tk.Frame(self.option_frame, width=1, bg="gray30")
        sep.pack(fill="x")

        self.coded_or_decoded = tk.IntVar()
        self.coded_or_decoded.set(1)

        options = [("Szyfrowanie", 101), ("Deszyfrowanie", 102)]

        def ShowChoice():
            print(self.coded_or_decoded.get())

        for option, val in options:
            tk.Radiobutton(
                self.option_frame,
                text=option,
                padx=20,
                variable=self.coded_or_decoded,
                command=ShowChoice,
                value=val,
                bg="gray70",
            ).pack(anchor=tk.W)

        sep = tk.Frame(self.option_frame, width=1, bg="gray30")
        sep.pack(fill="x")

        ciphers = [
            "Rail Fence",
            "Przestawienie macierzowe A",
            "Przestawienie macierzowe B",
        ]

        self.cipher_label = tk.Label(
            self.option_frame,
            text="Wybierz metode szyfrowania: ",
            bg="gray70",
            fg="gray16",
        ).pack()
        self.cipher = tk.StringVar()
        cipher_choosen = ttk.Combobox(
            self.option_frame, textvariable=self.cipher, state="readonly", width=25
        )
        cipher_choosen["values"] = ciphers
        cipher_choosen.pack(pady=10)
        cipher_choosen.current(0)
        open_file_button = tk.Button(
            self.option_frame,
            text="wczytaj plik tekstowy",
            width=20,
            command=lambda: self.open_file(),
        ).pack()
        save_file_button = tk.Button(
            self.option_frame,
            text="zapisz jako plik tekstowy",
            width=20,
            bg="grey21",
            fg="snow",
            command=lambda: self.save_file(),
        ).pack()

        l_key = tk.Label(self.data_frame, text="Wprowadz klucz:")
        self.key = tk.Text(self.data_frame, width=30, height=1, wrap=tk.WORD)
        l1 = tk.Label(self.data_frame, text="Wprowadź tekst:")
        self.entry = tk.Text(self.data_frame, width=85, height=3, wrap=tk.WORD)
        button = tk.Button(
            self.data_frame,
            text="Szyfruj / Deszyfruj ",
            width=20,
            command=lambda: self.decrypt_encrypt(),
        )
        l2 = tk.Label(self.data_frame, text="Zaszyfrowany/ Zdeszyfrowany tekst:")
        self.output = tk.Text(self.data_frame, width=85, height=3, wrap=tk.WORD)

        l_key.grid(row=0, column=1, padx=5, sticky="w")
        self.key.grid(row=1, column=1, padx=5, pady=(0, 10), sticky="w")
        l1.grid(row=2, column=1, padx=5, sticky="w")
        self.entry.grid(row=3, column=1, columnspan=2, padx=5, pady=(0, 10))
        button.grid(row=4, column=1, columnspan=2, pady=5)
        l2.grid(row=5, column=1, padx=5, sticky="w")
        self.output.grid(row=6, column=1, columnspan=2, padx=5, pady=(0, 10))

    def open_file(self):
        filename = fd.askopenfilename(
            filetypes=[("Plik tekstowy", "*.txt")]
        )  # wywołanie okna dialogowego open file

        if filename:
            with open(filename, "r", -1, "utf-8") as file:
                self.entry.delete(1.0, tk.END)
                self.entry.insert(tk.END, file.read())

    def save_file(self):
        filename = fd.asksaveasfilename(
            filetypes=[("Plik tekstowy", "*.txt")], defaultextension="*.txt"
        )  # wywołanie okna dialogowego save file

        if filename:
            with open(filename, "w", -1, "utf-8") as file:
                file.write(self.output.get(1.0, tk.END))

    def decrypt_encrypt(self):
        decrypt_or_encrypt = self.coded_or_decoded.get()
        cipher = self.cipher.get()
        message = self.entry.get("1.0", tk.END).rstrip()
        key = self.key.get("1.0", tk.END).rstrip()
        result = ""

        if decrypt_or_encrypt == 101:
            if cipher.upper() == "RAIL FENCE":
                if self.rail_fence_validation(key):
                    key = int(key)
                    result = encrypt_message_rail_fence(message, key)
            if cipher.upper() == "PRZESTAWIENIE MACIERZOWE A":
                if self.columnar_transposition_validation_A(key):
                    result = encrypt_columnar_transposition_a(message, key)
            if cipher.upper() == "PRZESTAWIENIE MACIERZOWE B":
                if self.columnar_transposition_validation_B(key):

                    result = encrypt_columnar_transposition_b(message, key)
        elif decrypt_or_encrypt == 102:
            if cipher.upper() == "RAIL FENCE":
                if self.rail_fence_validation(key):
                    key = int(key)
                    result = decrypt_message_rail_fence(message, key)
            if cipher.upper() == "PRZESTAWIENIE MACIERZOWE A":
                if self.columnar_transposition_validation_A(key):
                    result = decrypt_columnar_transposition_a(message, key)
            if cipher.upper() == "PRZESTAWIENIE MACIERZOWE B":
                if self.columnar_transposition_validation_B(key):
                    result = decrypt_columnar_transposition_b(message, key)

        self.output.insert(tk.END, str(result))

    def rail_fence_validation(self, key):
        if not is_integer(key):
            popupmsg("klucz musi być liczbą dodatnią")
            return False
        elif int(key) <= 0:
            popupmsg("klucz musi być większy od zera")
            return False
        else:
            return True

    def columnar_transposition_validation_B(self, key):
        if key.isalpha():
            return True
        else:
            popupmsg("Klucz musi składać się tylko z liter alfabetu")
            return False

    def columnar_transposition_validation_A(self, key):
        if not check_key_format_col_trans_A(key):
            popupmsg("Zły format klucza! Poprawny to np. 1-4-3-2")
            return False
        elif not check_numbers_sequence(key):
            popupmsg("Klucz musi być sekwencją liczb np. 1-3-2")
        else:
            return True


def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


def check_key_format_col_trans_A(key):
    check = 0
    for i in range(len(key)):
        if is_integer(key[i]):
            check += 1
        if key[i] == "-" and i != 0:
            if is_integer(key[i - 1]) and i == len(key):
                check += 1
            elif is_integer(key[i - 1]) and is_integer(key[i + 1]):
                check += 1

    if check == len(key):
        return True
    else:
        return False


def checkConsecutive(l):
    return sorted(l) == list(range(1, len(l) + 1))


def check_numbers_sequence(key):
    key_numbers_list = []
    number = ""
    for i in key:
        if i != "-":
            number += i
        else:
            key_numbers_list.append((int(number)))
            number = ""

    key_numbers_list.append((int(number)))
    print(key_numbers_list)
    if checkConsecutive(key_numbers_list):
        return True
    else:
        return False


def popupmsg(msg):
    popup = tk.Tk()
    popup.geometry("400x100")
    popup.wm_title("!")
    label = tk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="OK", command=popup.destroy)
    B1.pack()
    popup.mainloop()
