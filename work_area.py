import tkinter as tk
from tkinter import ttk


def create_basic_info_tab(self):
    """Вкладка с информацией о загруженных данных"""
    frame = ttk.Frame(self.notebook)
    self.notebook.add(frame, text="Информация")

    # Создаю текстовое поле с прокруткой
    text_widget = tk.Text(frame, wrap=tk.WORD, width=80, height=20)
    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=text_widget.yview)
    text_widget.configure(yscrollcommand=scrollbar.set)

    # Добавляю информацию о данных
    info_text = f"""
    📊 ИНФОРМАЦИЯ О ДАННЫХ:
    
    • Всего записей: {len(self.df):,}
    • Количество параметров: {len(self.df.columns)}
    • Временной диапазон: {self.df['Timestamp'].min()} - {self.df['Timestamp'].max()}
    • Длительность записи: {self.df['Timestamp'].max() - self.df['Timestamp'].min()}
    """
    text_widget.insert(tk.END, info_text)
    text_widget.config(state=tk.DISABLED)  # Только для чтения

    text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Размещаю на вкладке
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
