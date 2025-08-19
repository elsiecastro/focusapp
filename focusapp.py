import streamlit as st
import time
from datetime import datetime

st.set_page_config(page_title="FocusUp", page_icon="📚", layout="centered")

# --- Variables de sesión ---
if "tasks" not in st.session_state:
    st.session_state.tasks = []
if "study_time" not in st.session_state:
    st.session_state.study_time = 0
if "mood_log" not in st.session_state:
    st.session_state.mood_log = []

# --- Encabezado ---
st.title("📚 FocusUp – Tu guía para estudiar con enfoque y bienestar")
st.write("✨ Una app para combinar productividad y bienestar emocional.")

# --- Frase motivacional ---
st.success("🌟 *“El éxito es la suma de pequeños esfuerzos repetidos cada día.”*")

# --- Registro de estado emocional ---
st.header("📝 Registro de Estado Emocional")
mood = st.radio("¿Cómo te sientes ahora?", ["😊 Bien", "😐 Normal", "😟 Cansado", "😢 Triste"])
if st.button("Registrar estado"):
    st.session_state.mood_log.append((datetime.now(), mood))
    st.success(f"Estado registrado: {mood}")

# --- Modo enfoque (Pomodoro) ---
st.header("⏳ Modo Enfoque (Pomodoro)")
study_minutes = st.slider("Duración de estudio (min)", 10, 60, 25)
break_minutes = st.slider("Duración del descanso (min)", 3, 15, 5)

if st.button("Iniciar sesión de estudio"):
    with st.spinner("Estudiando..."):
        time.sleep(2)  # Simulación rápida (para demo)
    st.session_state.study_time += study_minutes
    st.success(f"✅ Sesión completada: {study_minutes} min de estudio y {break_minutes} min de descanso")

# --- Microtareas ---
st.header("📌 Microtareas Diarias")
new_task = st.text_input("Agregar nueva tarea")
if st.button("Añadir tarea"):
    if new_task:
        st.session_state.tasks.append({"task": new_task, "done": False})

for i, task in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([0.8,0.2])
    with col1:
        st.write("✔️" if task["done"] else "⬜", task["task"])
    with col2:
        if st.button("Hecho", key=i):
            st.session_state.tasks[i]["done"] = True

# --- Métricas de progreso ---
st.header("📊 Métricas de Progreso")
st.write(f"⏱️ Tiempo total de estudio: **{st.session_state.study_time} min**")
st.write(f"📌 Tareas completadas: **{sum(t['done'] for t in st.session_state.tasks)} / {len(st.session_state.tasks)}**")
st.write(f"📝 Estados emocionales registrados: **{len(st.session_state.mood_log)}**")
