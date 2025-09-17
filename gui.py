import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from data_loader import load_telemetry_data, export_statistics_to_txt
from work_area import create_basic_info_tab, create_statics_tab, create_plots_tab

class MainApplication(ttk.Frame):  # Графический интерфейс
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)  # Наследование от предка Frame
        self.parent = parent
        self.parent.title("Анализатор телеметрии")
        self.parent.geometry("1200x800")
        icon = tk.PhotoImage(file="static/ping.png")
        self.parent.iconphoto(True, icon)

        self.export_menu = None  # Для обновления кнопок
        self.df = None  # Хранение загруженных данных

        self.interface_elements()
        self.setup_layout()

    def interface_elements(self):
        """Создание элементов интерфейса"""
        self.top_level_menu()
        self.notebook = ttk.Notebook(self.parent)  # Рабочая область

        self.status_var = tk.StringVar()  # Статус бар
        self.status_var.set("Готов к работе")  # RIDGE - эффект выпуклой выемки, W - левый край
        self.status_bar = ttk.Label(self.parent, textvariable=self.status_var, relief=tk.RIDGE, anchor=tk.W)

    def setup_layout(self):
        """Расстановка элементов в окне"""
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5) 
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X) 

    def top_level_menu(self):
        """Верхнее меню"""
        menubar = tk.Menu(self.parent)
        self.parent.config(menu=menubar)

        file_menu = tk.Menu(
            menubar, tearoff=0
        )  # Добавил выпадающие окна, без открепления
        menubar.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Открыть...", accelerator="Ctrl+O", command=self.btn_open)
        self.parent.bind("<Control-o>", lambda _: self.btn_open())  # Горячие клавиши
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.btn_exit)

        self.export_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Экспорт", menu=self.export_menu)  # Пункт 8.1.4 в tt
        self.export_menu.add_command(
            label="Экспорт графиков...", state="disabled", command=self.export_graphs
            )
        self.export_menu.add_command(
            label="Экспорт статистики...", state="disabled", command=self.export_stats
            )

        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Справка", menu=help_menu)
        help_menu.add_command(label="О программе", command=self.btn_about)

    def create_tabs(self):
        """Создание вкладок с данными"""
        # Очищаем существующие вкладки
        for tab in self.notebook.tabs():
            self.notebook.forget(tab)

        create_basic_info_tab(self.notebook, self.df)
        create_statics_tab(self.notebook, self.df)
        create_plots_tab(self.notebook, self.df)

    def btn_open(self):
        """Обработчик кнопки 'Открыть'"""
        file_path = filedialog.askopenfilename(
            title="Выберите файл телеметрии",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
        )
        if file_path:
            self.status_var.set(f"Загрузка файла: {file_path}...")
            self.update_idletasks()  # Обновляю статус-бар
            try:
                self.df = load_telemetry_data(file_path)
                self.status_var.set(f"Успех! Загружено: {len(self.df)} записей")
                self.enable_export_menus()
                self.create_tabs()
            except Exception as e:  # pylint: disable=W0718
                messagebox.showerror("Ошибка", f"Не удалось загрузить файл:\n{str(e)}")
                self.status_var.set("Ошибка загрузки файла")

    def enable_export_menus(self):
        """Активирует пункты меню экспорта после загрузки данных"""
        self.export_menu.entryconfig(0, state="normal")  # 0, 1 - пункты в выпадающей области 'Экспорт'
        self.export_menu.entryconfig(1, state="normal")

    def export_graphs(self):
        """Экспорт графиков"""
        file_path = filedialog.asksaveasfilename(
            title="Сохранить графики",
            defaultextension=".png",
            filetypes=[
                ("PNG files", "*.png"),
                ("PDF files", "*.pdf"),
                ("Все файлы", "*.*")
            ]
        )
        
        if file_path:
            # Здесь будет логика экспорта графиков
            messagebox.showinfo(
                "Экспорт графиков", 
                f"Графики будут сохранены в: {file_path}"
            )
    
    def export_stats(self):
        """Экспорт статистики"""
        default_filename = "telemetry_statistics.txt"
        file_path = filedialog.asksaveasfilename(
            title="Сохранить статистику",
            initialfile=default_filename,
            defaultextension=".txt",
            filetypes=[
                ("Текстовые файлы", "*.txt"),
                ("Все файлы", "*.*")
            ]
        )
        
        if file_path:
            try:
                export_statistics_to_txt(self.df, file_path)
                self.status_var.set(f"Статистика экспортирована: {file_path}")
                messagebox.showinfo(
                    "Успех", 
                    f"Статистика успешно экспортирована в:\n{file_path}"
                )
            except Exception as e:
                messagebox.showerror(
                    "Ошибка экспорта", 
                    f"Не удалось экспортировать статистику:\n{str(e)}"
                )

    def btn_about(self):
        """Обработчик кнопки 'О программе'"""
        about_text = """
        Анализатор телеметрии
        Версия 0.1 (Pre-Alpha)
        
        Разработано для анализа и визуализации
        данных телеметрии uav.
        
        https://github.com/raiserror/telemetry_analysis_tt
        """
        messagebox.showinfo("О программе", about_text)

    def btn_exit(self):
        """Выход из приложения"""
        self.parent.quit()

if __name__ == "__main__":  # Запуск для тестирования этого файла
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
