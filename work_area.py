import tkinter as tk
from tkinter import ttk
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from constants import paremeter_categories

def create_basic_info_tab(notebook, df):
    """Вкладка с информацией о загруженных данных"""
    frame = ttk.Frame(notebook)
    notebook.add(frame, text="Информация")

    # Создаю текстовое поле с прокруткой
    text_widget = tk.Text(frame, wrap=tk.WORD, width=80, height=20)
    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=text_widget.yview)
    text_widget.configure(yscrollcommand=scrollbar.set)

    # Добавляю информацию о данных
    info_text = f"""
    📊 ИНФОРМАЦИЯ О ДАННЫХ:
    
    • Всего записей: {len(df):,}
    • Количество параметров: {len(df.columns)}
    • Временной диапазон: {df['Timestamp'].min()} - {df['Timestamp'].max()}
    • Длительность записи: {df['Timestamp'].max() - df['Timestamp'].min()}
    """
    text_widget.insert(tk.END, info_text)
    text_widget.config(state=tk.DISABLED)  # Только для чтения

    text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    return frame


def create_statics_tab(notebook, df):
    """Вкладка со статистикой параметров"""
    frame = ttk.Frame(notebook)
    notebook.add(frame, text="Статистика")  # Кнопка для статистики

    columns = ("Параметр", "Мин", "Макс", "Среднее", "Разброс", "Не-NaN")
    tree = ttk.Treeview(frame, columns=columns, show="headings", height=20)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):  # Проверка на число
            stats = [  # Строка
                column,
                f"{df[column].min():.3f}",
                f"{df[column].max():.3f}",
                f"{df[column].mean():.3f}",
                f"{df[column].std():.3f}",
                f"{df[column].count()}/{len(df)}",
            ]
            tree.insert("", "end", values=stats)  # Добавляю строку в таблицу

    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)

    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    return frame


def create_plots_tab(notebook, df, status_var=None):
    """Вкладка с графиками параметров"""
    frame = ttk.Frame(notebook)
    notebook.add(frame, text="Графики")  # Кнопка для статистики

    control_frame = ttk.Frame(frame) # Фрейм для выбора параметров
    control_frame.pack(fill=tk.X, padx=10, pady=5)

    # Выбор параметра для оси X
    ttk.Label(control_frame, text="Ось X:").grid(row=0, column=0, padx=5, pady=5)
    x_var = tk.StringVar(value="Timestamp")
    x_combobox = ttk.Combobox(control_frame, textvariable=x_var, state="readonly")
    x_combobox['values'] = list(df.columns)
    x_combobox.grid(row=0, column=1, padx=5, pady=5)

    # Выбор параметра для оси Y
    ttk.Label(control_frame, text="Ось Y:").grid(row=0, column=2, padx=5, pady=5)
    y_var = tk.StringVar(value="Timestamp")
    y_combobox = ttk.Combobox(control_frame, textvariable=y_var, state="readonly")
    y_combobox['values'] = list(df.columns)
    y_combobox.grid(row=0, column=3, padx=5, pady=5)

    plot_btn = ttk.Button(control_frame, text="Построить график", 
                         command=lambda: plot_data(df, x_var.get(), y_var.get(), plot_frame, status_var))
    
    plot_btn.grid(row=0, column=4, padx=5, pady=5) # Размещение кнопки
    plot_frame = ttk.Frame(frame) # Фрейм для графика
    plot_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    return [x_var.get(), y_var.get()]

def plot_data(df, x_col, y_col, parent_frame, status_var):
    """Строит график выбранных данных"""
    # Очищаю предыдущий график
    for widget in parent_frame.winfo_children():
        widget.destroy()
    
    # Проверка, передаются ли данные
    if not x_col or not y_col:
        return
    
    try:
        # Создаю фигуру matplotlib
        fig = Figure(figsize=(10, 6))  # В дюймах
        ax = fig.add_subplot(111)  #  1x1 сетка, первая позиция
        
        # Строю график
        ax.plot(df[x_col], df[y_col])
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.set_title(f"{x_col} | {y_col}")
        ax.grid(True) # Включение сетки на графике
        
        # Встраиваю в Tkinter
        canvas = FigureCanvasTkAgg(fig, parent_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        status_var.set(f"Создан график: {x_col} | {y_col}")
    except Exception as e:
        error_label = ttk.Label(parent_frame, text=f"Ошибка построения: {str(e)}", foreground="red")
        error_label.pack(pady=10)

def categorize_parameters(df_columns):
    """Функция для автоматической категоризации"""
    categorized = {category: [] for category in paremeter_categories.keys()}
    categorized["Другие"] = []  # Для параметров без категории, если будут допы
    
    for column in df_columns:
        found_category = False
        for category, patterns in paremeter_categories.items():
            # Проверяю совпадение по паттернам
            for pattern in patterns:
                if pattern.endswith('.*'):  # Будет шаблон типа estimatorStatus.*
                    prefix = pattern[:-2]
                    if column.startswith(prefix):
                        categorized[category].append(column)
                        found_category = True
                        break
                elif column == pattern:  # Точное совпадение
                    categorized[category].append(column)
                    found_category = True
                    break
            if found_category:
                break
        
        if not found_category:
            categorized["Другие"].append(column)
    
    # Удаляю пустые категории
    return {k: v for k, v in categorized.items() if v}