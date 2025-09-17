import tkinter as tk
from tkinter import ttk
import pandas as pd


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


def create_plots_tab(notebook, df):
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
            tree.insert("", "end", values=stats)  # Добавляем строку в таблицу

    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)

    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    return frame
