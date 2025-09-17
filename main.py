import tkinter as tk

from gui import MainApplication


def main():  # Точка входа в приложение
    root = tk.Tk()
    MainApplication(root)
    root.mainloop()


if __name__ == "__main__":
    main()
