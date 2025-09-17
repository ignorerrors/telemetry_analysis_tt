import pandas as pd


def load_telemetry_data(file_path):
    """Загружаю и обрабатываю CSV файл с телеметрией uav"""
    try:
        # Загружаем данные, обрабатываем спец. значения
        df = pd.read_csv(file_path, na_values=["--.--", "nan", "NaN", ""])

        if "Timestamp" in df.columns:  # Timestamp в формат datetime
            df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")
        return df

    except Exception as e:
        print(f"Ошибка загрузки данных: {e}")
        raise


def export_statistics_to_txt(df, filename):
    """Экспортирую статистику параметров в текстовый файл"""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("СТАТИСТИКА ПАРАМЕТРОВ ТЕЛЕМЕТРИИ\n")
            f.write("=" * 32 + "\n")
            f.write(f"Всего записей: {len(df):,}\n")
            numeric_type = [col for col in df.columns if pd.api.types.is_numeric_dtype(df[col])]
            max_param_length = max(len(str(col)) for col in df.columns)
            f.write(f"Анализируемых параметров: {len(numeric_type)}\n")
            f.write("=" * (max_param_length + 52 + len(str(len(df)))) + "\n\n")

            # Шапка таблицы
            f.write(f"{'Параметр':<{max_param_length}} {'Мин':<10} {'Макс':<10} {'Среднее':<10} {'Разброс':<10} {'Заполнено':<12}\n")
            f.write("-" * (max_param_length + 52 + len(str(len(df)))) + "\n")

            for column in df.columns:  # Данные по каждому параметру
                if pd.api.types.is_numeric_dtype(df[column]):
                    stats = [
                        column,
                        f"{df[column].min():.3f}",
                        f"{df[column].max():.3f}",
                        f"{df[column].mean():.3f}",
                        f"{df[column].std():.3f}",
                        f"{df[column].count()}/{len(df)}",
                    ]
                    f.write(f"{stats[0]:<{max_param_length}} {stats[1]:<10} {stats[2]:<10} {stats[3]:<10} {stats[4]:<10} {stats[5]:<12}\n")

            f.write("\n" + "=" * 50 + "\n")
            f.write(f"Файл сгенерирован: {pd.Timestamp.now()}\n")
        return True

    except Exception as e: # pylint: disable=W0718
        print(f"Ошибка экспорта статистики: {e}")
        return False
