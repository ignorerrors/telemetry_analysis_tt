import tkinter as tk
from tkinter import ttk, messagebox


class MainApplication(ttk.Frame):  # Графический интерфейс
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)  # Наследование от предка Frame
        self.parent = parent
        self.parent.title("Анализатор телеметрии")
        self.parent.geometry("1200x800")
        icon = tk.PhotoImage(file="static/ping.png")
        self.parent.iconphoto(True, icon)

        self.interface_elements()
        self.setup_layout()

    def interface_elements(self):
        """Создание элементов интерфейса"""
        self.top_level_menu()
        self.notebook = ttk.Notebook(self.parent) # Рабочая область
        
        self.status_var = tk.StringVar() #Статус бар
        self.status_var.set("Готов к работе") # RIDGE - эффект выпуклой выемки, W - левый край
        self.status_bar = ttk.Label(self.parent, textvariable=self.status_var, relief=tk.RIDGE, anchor=tk.W)

    def setup_layout(self):
        """Расстановка элементов в окне"""
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def top_level_menu(self):
        """Верхнее меню"""
        menubar = tk.Menu(self.parent)
        self.parent.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)  # Добавил выпадающие окна, без открепления
        menubar.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Открыть...", accelerator="Ctrl+O")
        self.parent.bind('<Control-o>', self.open()) # Горячие клавиши 
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.exit)
        
        export_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Экспорт", menu=export_menu)
        export_menu.add_command(label="Экспорт графиков...", state="disabled")  # Пункт 8.1.4 в tt
        export_menu.add_command(label="Экспорт статистики...", state="disabled")
        
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Справка", menu=help_menu)
        help_menu.add_command(label="О программе", command=self.about)

    def open(self): # Реализовать
        ...

    def export_graphs(self):
        """Обработчик кнопки 'Экспорт графиков'"""
        messagebox.showinfo("Экспорт", "Функция будет реализована...")

    def export_stats(self):
        """Обработчик кнопки 'Экспорт статистики'"""
        messagebox.showinfo("Экспорт", "Функция будет реализована...")

    def about(self):
        """Обработчик кнопки 'О программе'"""
        about_text = """
        Анализатор телеметрии
        Версия 0.1 (Pre-Alpha)
        
        Разработано для анализа и визуализации
        данных телеметрии uav.
        
        https://github.com/raiserror/telemetry_analysis_tt
        """
        messagebox.showinfo("О программе", about_text)

    def exit(self):
        """Выход из приложения"""
        self.parent.quit()

if __name__ == "__main__":  # Запуск для тестирования этого файла
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
