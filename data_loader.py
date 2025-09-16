import pandas as pd

def load_telemetry_data(file_path):
    """Загружаю и обрабатываю CSV файл с телеметрией uav"""
    try:
        # Загружаем данные, обрабатываем спец. значения
        df = pd.read_csv(file_path, na_values=['--.--', 'nan', 'NaN', ''])

        # Timestamp в формат datetime
        if 'Timestamp' in df.columns:
            df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')

        return df
        
    except Exception as e:
        print(f"Ошибка загрузки данных: {e}")
        raise