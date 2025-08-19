import streamlit as st
import time
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- Configuración de página ---
st.set_page_config(page_title="FocusUp", page_icon="📚", layout="wide")

# --- Variables de sesión ---
if "tasks" not in st.session_state:
    st.session_state.tasks = []
if "study_time" not in st.session_state:
    st.session_state.study_time = 0
if "mood_log" not in st.session_state:
    st.session_state.mood_log = []
if "timer_running" not in st.session_state:
    st.session_state.timer_running = False

# --- Encabezado ---
st.markdown("<h1 style='text-align:center; color:#4CAF50;'>📚 FocusUp</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>✨ Estudia con enfoque y bienestar ✨</h4>", unsafe_allow_html=True)
st.markdown("---")

# --- Frase motivacional ---
st.success("🌟 *“El éxito es la suma de pequeños esfuerzos repetidos cada día.”*")

# --- Registro de estado emocional ---
st.header("📝 Registro de Estado Emocional")
mood = st.radio("¿Cómo te sientes ahora?", ["😊 Bien", "😐 Normal", "😟 Cansado", "😢 Triste"], horizontal=True)
if st.button("Registrar estado"):
    st.session_state.mood_log.append((datetime.now(), mood))
    st.success(f"Estado registrado: {mood}")

# Mostrar gráfico de estados
if st.session_state.mood_log:
    df_moods = pd.DataFrame(st.session_state.mood_log, columns=["Tiempo", "Estado"])
    mood_counts = df_moods["Estado"].value_counts().reset_index()
    mood_counts.columns = ["Estado", "Cantidad"]
    fig = px.bar(mood_counts, x="Estado", y="Cantidad", title="Historial de Estados Emocionales",
                 color="Estado", text="Cantidad")
    st.plotly_chart(fig, use_container_width=True)

# --- Modo enfoque (Pomodoro) ---
st.header("⏳ Modo Enfoque (Pomodoro)")
col1, col2 = st.columns(2)

with col1:
    study_minutes = st.slider("Duración de estudio (min)", 10, 60, 25)
    break_minutes = st.slider("Duración del descanso (min)", 3, 15, 5)

with col2:
    if st.button("▶️ Iniciar sesión"):
        st.session_state.timer_running = True
        total_seconds = study_minutes * 60
        start = time.time()
        while time.time() - start < total_seconds:
            elapsed = int(time.time() - start)
            remaining = total_seconds - elapsed
            mins, secs = divmod(remaining, 60)
            timer_text = f"{mins:02d}:{secs:02d}"
            st.metric("⏰ Tiempo restante", timer_text)
            time.sleep(1)
        st.session_state.study_time += study_minutes
        st.success(f"✅ ¡Sesión completada! {study_minutes} min de estudio + {break_minutes} min de descanso")
        st.session_state.timer_running = False

# --- Microtareas ---
st.header("📌 Microtareas Diarias")
new_task = st.text_input("Agregar nueva tarea")
if st.button("➕ Añadir tarea"):
    if new_task:
        st.session_state.tasks.append({"task": new_task, "done": False})

for i, task in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        st.write("✔️" if task["done"] else "⬜", task["task"])
    with col2:
        if not task["done"]:
            if st.button("Hecho", key=f"done_{i}"):
                st.session_state.tasks[i]["done"] = True

# --- Métricas de progreso ---
st.header("📊 Métricas de Progreso")
st.write(f"⏱️ Tiempo total de estudio: **{st.session_state.study_time} min**")
st.write(f"📌 Tareas completadas: **{sum(t['done'] for t in st.session_state.tasks)} / {len(st.session_state.tasks)}**")
st.write(f"📝 Estados emocionales registrados: **{len(st.session_state.mood_log)}**")

