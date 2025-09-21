import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class PlotManager:
    """Менеджер для управления графиками"""

    def __init__(self, parent_frame, status_var=None):
        self.parent_frame = parent_frame
        self.status_var = status_var
        self.current_figure = None
        self.current_canvas = None  # Инициализирую переменную для хранения холста tkinter

    def create_plot(self, df, x_col, y_col):
        """Создает или обновляет график с выбранными данными"""
        # Очищаю предыдущий график
        self.clear_plot()

        if not x_col or not y_col:
            return

        try:
            # Создаю новую фигуру
            self.current_figure = Figure(figsize=(10, 6))
            ax = self.current_figure.add_subplot(111)

            # Строю график
            ax.plot(df[x_col], df[y_col])
            ax.set_xlabel(x_col)  # Подписи на графике
            ax.set_ylabel(y_col)
            ax.set_title(f"{x_col} | {y_col}")
            ax.grid(True)  # Отображение сетки

            # Встраиваю в Tkinter, следующая строчка - создаю холст в родительском фрейме
            self.current_canvas = FigureCanvasTkAgg(self.current_figure, self.parent_frame)
            self.current_canvas.draw()  # Рисую график на холсте
            self.current_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

            if self.status_var:
                self.status_var.set(f"Создан график: {x_col} | {y_col}")

            return self.current_figure

        except Exception as e:
            error_label = ttk.Label(self.parent_frame, text=f"Ошибка построения: {str(e)}", foreground="red")
            error_label.pack(pady=10)
            if self.status_var:
                self.status_var.set(f"Ошибка: {str(e)}")
            return None

    def clear_plot(self):
        """Очищает текущий график"""
        if self.current_canvas:
            self.current_canvas.get_tk_widget().destroy()
            self.current_canvas = None
        self.current_figure = None

        # Очищаю все виджеты в родительском фрейме
        for widget in self.parent_frame.winfo_children():
            widget.destroy()
