import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from data_loader import load_telemetry_data, export_statistics_to_txt, export_plot_as_png
from work_area import create_basic_info_tab, create_statics_tab, create_plots_tab
from work_area import categorize_parameters
import sv_ttk

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
        self.create_plots_tab = None # Будет сохранять значения x, y графиков

        self.interface_style()
        self.interface_elements()
        self.setup_layout()
    def interface_style(self):
        sv_ttk.set_theme("light")

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
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X, padx = 10, pady = 4) 

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
        menubar.add_cascade(label="Руководство", menu=help_menu)
        help_menu.add_command(label="Пользователю", command=self.user_manual)
        help_menu.add_command(label="О программе", command=self.btn_about)

    def create_tabs(self):
        """Создание вкладок с данными"""
        # Очищаем существующие вкладки
        for tab in self.notebook.tabs():
            self.notebook.forget(tab)

        create_basic_info_tab(self.notebook, self.df)
        # self.create_categorized_tabs(self.notebook, self.df)
        create_statics_tab(self.notebook, self.df)
        self.create_plots_tab = create_plots_tab(self.notebook, self.df, self.status_var)

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
        default_filename = "telemetry_graph.png"
        file_path = filedialog.asksaveasfilename(
            title="Сохранить статистику",
            initialfile=default_filename,
            defaultextension=".png",
            filetypes=[
                ("PNG files", "*.png"),
                ("PDF files", "*.pdf"),
                ("Все файлы", "*.*")
            ]
        )
        
        if file_path:
            try:
                a = export_plot_as_png(self.df, self.create_plots_tab, file_path)
                a.savefig(file_path, dpi=300, bbox_inches='tight')
                self.status_var.set(f"График сохранен как: {file_path}")
                messagebox.showinfo(
                    "Успех", 
                    f"График успешно экспортирован в:\n{file_path}"
                )
            except Exception as e:
                messagebox.showerror(
                    "Ошибка экспорта", 
                    f"Не удалось экспортировать график:\n{str(e)}"
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
    # FIXME: Не знаю как реализовать
    def create_categorized_tabs(self, notebook, df):
        """Создает вкладки для каждой категории параметров"""
        # Автоматически categorizing параметров
        categorized = categorize_parameters(df.columns)
        
        # Создаем вкладку для каждой категории
        for category, parameters in categorized.items():
            frame = ttk.Frame(notebook)
            notebook.add(frame, text=category)
            
            # Заголовок
            title_label = ttk.Label(frame, text=f"Категория: {category}", 
                                font=("Arial", 12, "bold"))
            title_label.pack(pady=10)
            
            # Список параметров
            if parameters:
                text_widget = tk.Text(frame, wrap=tk.WORD, width=80, height=15)
                scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=text_widget.yview)
                text_widget.configure(yscrollcommand=scrollbar.set)
                
                info_text = f"Параметры ({len(parameters)}):\n\n"
                for param in sorted(parameters):
                    non_null = df[param].count()
                    dtype = str(df[param].dtype)
                    info_text += f"• {param} ({dtype}, заполнено: {non_null}/{len(df)})\n"
                
                text_widget.insert(tk.END, info_text)
                text_widget.config(state=tk.DISABLED)
                
                text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)
                scrollbar.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 10))
            else:
                ttk.Label(frame, text="Нет параметров в этой категории").pack(pady=20)
        
        return notebook

    def user_manual(self):
        """Обработчик кнопки 'Пользователю'"""
        about_text = """
        • Загрузите файл в формате csv: 
          В левом верзнем углу нажмите на кнопку "Файл" -> "Открыть..."
          Или на английской раскладке нажать  комбинацию клавиш "Ctrl + O"
        • Рабочая область будет содержать пункты: 
          Информация, Статистика, Графики
        • В которых будет находиться: 
          Информация о данных, Общая статистика, Построение графиков
        • После успешной загрузки файла будет доступно:
        Экспорт графиков...
        Экспорт статистики... \n
        ПРИМЕЧАНИЕ:
        • Если ещё не был построе не один график, то при экспорте будет построен график Timestamp | Timestamp
        """
        messagebox.showinfo("Пользователю", about_text)

    def btn_about(self):
        """Обработчик кнопки 'О программе'"""
        about_text = """
        Анализатор телеметрии
        Версия 0.2 (Pre-Alpha)
        
        Разработано для анализа и визуализации
        данных телеметрии uav.
        
        https://github.com/raiserror/telemetry_analysis_tt
        """
        messagebox.showinfo("О программе", about_text)

    def btn_exit(self):
        """Выход из приложения"""
        if messagebox.askyesno("Выход", "Вы уверены, что хотите выйти?"):
            self.parent.quit()

if __name__ == "__main__":  # Запуск для тестирования этого файла
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
