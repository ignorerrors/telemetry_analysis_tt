import tkinter as tk
from tkinter import ttk


class MainApplication(ttk.Frame):  # Графический интерфейс
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)  # Наследование от предка Frame
        self.parent = parent
        self.parent.title("Анализатор телеметрии")
        self.parent.geometry("1200x800")
        icon = tk.PhotoImage(file="static/ping.png")
        self.parent.iconphoto(True, icon)

        self.interface_elements()

    def interface_elements(self):
        """Создание элементов интерфейса"""
        self.top_level_menu()

    def top_level_menu(self):
        """Верхнее меню"""
        menubar = tk.Menu(self.parent)
        self.parent.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)  # Добавил выпадающие окна, без открепления
        menubar.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Открыть...", accelerator="Ctrl+O")
        file_menu.add_separator()
        file_menu.add_command(label="Выход")
        
        export_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Экспорт", menu=export_menu)
        export_menu.add_command(label="Экспорт графиков...", state="disabled")  # Пункт 8.1.4 в tt
        export_menu.add_command(label="Экспорт статистики...", state="disabled")
        
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Справка", menu=help_menu)
        help_menu.add_command(label="О программе")


if __name__ == "__main__":  # Запуск для тестирования этого файла
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
