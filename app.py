import sqlite3
import pandas as pd


def export_db_to_excel(db_path, excel_path):
    # Подключаемся к базе данных
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Получаем список таблиц в базе данных
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Создаем Excel-файл
    with pd.ExcelWriter(excel_path) as writer:
        for table_name in tables:
            table_name = table_name[0]
            df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
            df.to_excel(writer, sheet_name=table_name, index=False)

    # Закрываем соединение с БД
    conn.close()
    print(f"База данных экспортирована в {excel_path}")


# Использование
export_db_to_excel("bot_database.db", "database.xlsx")