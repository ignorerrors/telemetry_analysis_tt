import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sv_ttk
from data_loader import (
    load_telemetry_data,
    export_statistics_to_txt,
    export_plot_as_png,
)
from work_area import create_basic_info_tab, create_statics_tab, create_plots_tab
from work_area import create_categorized_tabs

class MainApplication(ttk.Frame):  # Графический интерфейс
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)  # Наследование от предка Frame
        self.parent = parent
        self.parent.title("Анализатор телеметрии")
        self.parent.geometry("1200x800")
        self.export_menu = None  # Для обновления кнопок
        self.df = None  # Хранение загруженных данных
        self.create_plots_tab = None  # Будет сохранять значения x, y графиков
        try:
            icon = tk.PhotoImage(file="static/ping.png")
            self.parent.iconphoto(True, icon)
        except:  # pylint: disable=W0702
            pass
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
        self.status_var.set("Готов к работе")  # убрал anchor=tk.W, relief=tk.GROOVE, не подходит к теме
        self.status_bar = ttk.Label(self.parent, textvariable=self.status_var)

    def setup_layout(self):
        """Расстановка элементов в окне"""
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=4)

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
        self.export_menu.add_command(label="Экспорт графиков...", state="disabled", command=self.export_graphs)
        self.export_menu.add_command(label="Экспорт статистики...", state="disabled", command=self.export_stats)

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
        create_statics_tab(self.notebook, self.df)
        self.create_plots_tab = create_plots_tab(self.notebook, self.df, self.status_var)
        create_categorized_tabs(self.notebook, self.df)

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
            except Exception as e:
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
                ("Все файлы", "*.*"),
            ],
        )

        if file_path:
            try:
                a = export_plot_as_png(self.df, self.create_plots_tab, file_path)
                a.savefig(file_path, dpi=300, bbox_inches="tight")
                self.status_var.set(f"График сохранен как: {file_path}")
                messagebox.showinfo(
                    "Успех", f"График успешно экспортирован в:\n{file_path}"
                )
            except Exception as e:
                messagebox.showerror(
                    "Ошибка экспорта", f"Не удалось экспортировать график:\n{str(e)}"
                )

    def export_stats(self):
        """Экспорт статистики"""
        default_filename = "telemetry_statistics.txt"
        file_path = filedialog.asksaveasfilename(
            title="Сохранить статистику",
            initialfile=default_filename,
            defaultextension=".txt",
            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")],
        )

        if file_path:
            try:
                export_statistics_to_txt(self.df, file_path)
                self.status_var.set(f"Статистика экспортирована: {file_path}")
                messagebox.showinfo("Успех", f"Статистика успешно экспортирована в:\n{file_path}")
            except Exception as e:
                messagebox.showerror(
                    "Ошибка экспорта",
                    f"Не удалось экспортировать статистику:\n{str(e)}",
                )

    def user_manual(self):
        """Обработчик кнопки 'Пользователю'"""
        about_text = """
        📖 Руководство пользователя
        🗂️ Загрузка данных
        Откройте меню Файл → Открыть (Ctrl+O)
        Выберите CSV файл с телеметрией
        Данные автоматически загрузятся и проанализируются
        📊 Просмотр статистики
        Вкладка "Статистика" показывает детальную информацию по каждому параметру
        Включает минимальные/максимальные значения, среднее, стандартное отклонение
        Отображает количество заполненных значений
        📈 Построение графиков
        Перейдите на вкладку "Графики"
        Выберите параметры для осей X и Y из выпадающих списков
        Нажмите "Построить график"
        График автоматически построится с сеткой и подписями осей
        💾 Экспорт данных
        Экспорт статистики - Сохраняет текстовый файл с полной статистикой
        Экспорт графиков - Сохраняет графики в формате PNG/PDF
        ПРИМЕЧАНИЕ:
        • Если ещё не был построен не один график, то при экспорте будет построен график Timestamp | Timestamp
        """
        messagebox.showinfo("Пользователю", about_text, icon="question")

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
