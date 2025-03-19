import dash
from dash import html, dcc
from dash import dash_table
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import requests

# Функция получения данных из NocoDB
def get_nocodb_data():
    url = "http://backend:8000/nocodb-data/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            records = data.get('records', [])
            print("Полученные данные:", records)
            cleaned_records = [
                {k: v for k, v in record.items() if not k.startswith('_nc_m2m_')}
                for record in records
            ]
            return pd.DataFrame(cleaned_records)
        else:
            print("Ошибка при получении данных:", response.status_code)
            return pd.DataFrame()
    except Exception as e:
        print(f"Ошибка соединения: {e}")
        return pd.DataFrame()

# Инициализация приложения Dash
app = dash.Dash(__name__)

# Базовый макет приложения
app.layout = html.Div([
    html.H1('Самокат Dashboard'),
    dcc.Interval(
        id='interval-component',
        interval=1 * 1000,  # обновление каждую секунду при первой загрузке
        n_intervals=0,
        max_intervals=1   # выполняется только один раз при загрузке
    ),
    html.Div(id='dashboard-content')
])

# Callback для обновления содержимого при загрузке
@app.callback(
    Output('dashboard-content', 'children'),
    Input('interval-component', 'n_intervals')
)
def update_dashboard(n):
    # Получаем данные
    df = get_nocodb_data()

    # Проверяем, что DataFrame не пустой
    if df.empty:
        return html.P('Нет данных для отображения. Проверьте соединение с NocoDB.')
    
    # Преобразуем даты
    if 'CreatedAt' in df.columns:
        df['CreatedAt'] = pd.to_datetime(df['CreatedAt'])
    if 'UpdatedAt' in df.columns:
        df['UpdatedAt'] = pd.to_datetime(df['UpdatedAt'], errors='coerce')

    # Определяем колонки для таблицы
    table_columns = [
        {'name': 'ID', 'id': 'Id'},
        {'name': 'Модель', 'id': 'model'},
        {'name': 'Емкость батареи', 'id': 'battery_capacity'},
        {'name': 'Уровень заряда', 'id': 'battery_level'},
        {'name': 'Статус', 'id': 'status'},
        {'name': 'Последнее обслуживание', 'id': 'last_maintenance_date'}
    ]

    # Возвращаем содержимое dashboard
    return [
        html.Div([
            html.H3('Общая статистика'),
            html.P(f"Всего самокатов: {len(df)}"),
            html.P(f"Средний уровень заряда: {df['battery_level'].mean():.2f}%")
        ]),
        html.Div([
            html.H3('Детальная информация'),
            dash_table.DataTable(
                data=df.to_dict('records'),
                columns=table_columns,
                style_table={'overflowX': 'auto'},
            )
        ])
    ]

# Запуск приложения
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050, debug=True)