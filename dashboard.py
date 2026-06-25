import streamlit as st
import pandas as pd

st.set_page_config(page_title="Портфолио аналитика", layout="wide")

# Заголовок
st.title("📊 Интерактивный дашборд портфолио")
st.markdown("---")

# Боковое меню
option = st.sidebar.selectbox(
    "Выбери отчёт",
    [
        "🏠 Главная",
        "🎤 Топ-10 исполнителей",
        "🎶 Количество треков по жанрам",
        "📦 Данные из PostgreSQL"
    ]
)

# Загрузка данных
@st.cache_data
def load_data(file):
    try:
        return pd.read_csv(file)
    except:
        return None

# --- Главная ---
if option == "🏠 Главная":
    st.subheader("👋 Привет! Это моё портфолио аналитика")
    st.markdown("""
    Здесь собраны:
    - SQL-запросы из DBeaver
    - Экспортированные данные
    - Визуализация результатов
    """)
    st.info("Выбери отчёт в левой панели 👈")

# --- Топ-10 исполнителей ---
elif option == "🎤 Топ-10 исполнителей":
    df = load_data("exports/top_artists.csv")
    if df is not None:
        st.subheader("🎤 Топ-10 исполнителей по количеству треков")
        st.bar_chart(data=df.set_index("Исполнитель"))
        st.dataframe(df)
    else:
        st.error("Файл top_artists.csv не найден")

# --- Количество треков по жанрам ---
elif option == "🎶 Количество треков по жанрам":
    df = load_data("exports/genre_count_chinook.csv")
    if df is not None:
        st.subheader("🎶 Количество треков по жанрам")
        st.bar_chart(data=df.set_index("Жанр"))
        st.dataframe(df)
    else:
        st.error("Файл genre_count_chinook.csv не найден")

# --- Данные из PostgreSQL ---
elif option == "📦 Данные из PostgreSQL":
    df = load_data("exports/artists_data.csv")
    if df is not None:
        st.subheader("📦 Данные из PostgreSQL")
        st.dataframe(df)
    else:
        st.warning("Файл artists_data.csv пока не добавлен")
        st.markdown("Экспортируй данные из PostgreSQL и сохрани как `exports/artists_data.csv`")
