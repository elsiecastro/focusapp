import streamlit as st
import time
import pandas as pd

# Configuración de página
st.set_page_config(page_title="FocusUp", page_icon="📚", layout="centered")

# Variables de sesión
if "page" not in st.session_state:
    st.session_state.page = "home"
if "tasks" not in st.session_state:
    st.session_state.tasks = []
if "study_time" not in st.session_state:
    st.session_state.study_time = 0
if "moods" not in st.session_state:
    st.session_state.moods = []

# ---- LANDING PAGE ----
if st.session_state.page == "home":
    st.markdown(
        """
        <div style="text-align:center; padding:50px">
            <h1 style="color:#4CAF50;">📚 FocusUp</h1>
            <h3>Tu guía para estudiar con enfoque y bienestar ✨</h3>
            <p style="color:gray;">Organiza tu tiempo, gestiona tu ánimo y alcanza tus metas</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("🚀 Comenzar", use_container_width=True):
        st.session_state.page = "app"

# ---- MAIN APP ----
elif st.session_state.page == "app":
    st.title("📚 FocusUp")
    st.write("✨ Bienvenido de nuevo, ¿listo para concentrarte?")

    # Estado emocional
    st.subheader("📝 Estado Emocional")
    mood = st.radio("¿Cómo te sientes?", ["😊 Bien", "😐 Normal", "😟 Cansado", "😢 Triste"], horizontal=True)
    if st.button("Registrar estado"):
        st.session_state.moods.append(mood)
        st.success("Estado registrado correctamente ✅")

    # Pomodoro
    st.subheader("⏳ Modo Enfoque")
    study = st.slider("Minutos de estudio", 10, 60, 25)
    if st.button("▶️ Iniciar Pomodoro"):
        with st.spinner("Estudiando..."):
            for sec in range(5):  # 🔹 Simulación rápida de 5 seg
                mins, s = divmod(sec, 60)
                st.metric("Tiempo", f"{mins:02}:{s:02}")
                time.sleep(1)
        st.session_state.study_time += study
        st.success(f"¡Listo! Estudiaste {study} minutos 🎉")

    # Microtareas
    st.subheader("📌 Microtareas")
    new_task = st.text_input("Nueva tarea")
    if st.button("➕ Añadir"):
        if new_task:
            st.session_state.tasks.append({"task": new_task, "done": False})
    for i, t in enumerate(st.session_state.tasks):
        cols = st.columns([0.8,0.2])
        cols[0].write(("✔️ " if t["done"] else "⬜ ") + t["task"])
        if not t["done"]:
            if cols[1].button("Hecho", key=i):
                st.session_state.tasks[i]["done"] = True

    # ---- Música integrada ----
    st.subheader("🎧 Música para concentrarte")
    st.write("Selecciona una playlist recomendada para estudiar:")

    option = st.selectbox("Elige tu estilo", ["Lofi", "Clásica", "Ambiental"])

    if option == "Lofi":
        st.markdown(
            """
            <iframe style="border-radius:12px" 
            src="https://open.spotify.com/embed/playlist/5qapC9lRDU9?utm_source=generator" 
            width="100%" height="380" frameBorder="0" 
            allowfullscreen="" 
            allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>
            """, unsafe_allow_html=True
        )
    elif option == "Clásica":
        st.markdown(
            """
            <iframe style="border-radius:12px" 
            src="https://open.spotify.com/embed/playlist/37i9dQZF1DWWEJlAGA9gs0?utm_source=generator" 
            width="100%" height="380" frameBorder="0" 
            allowfullscreen="" 
            allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>
            """, unsafe_allow_html=True
        )
    elif option == "Ambiental":
        st.markdown(
            """
            <iframe style="border-radius:12px" 
            src="https://open.spotify.com/embed/playlist/7FUtIEYVWoxF2hxkDb1c5t?utm_source=generator" 
            width="100%" height="380" frameBorder="0" 
            allowfullscreen="" 
            allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>
            """, unsafe_allow_html=True
        )

    # Métricas
    st.subheader("📊 Progreso")
    st.info(f"⏱️ Tiempo total: {st.session_state.study_time} min")
    st.info(f"📌 Tareas completadas: {sum(t['done'] for t in st.session_state.tasks)} / {len(st.session_state.tasks)}")
    st.info(f"📝 Estados registrados: {len(st.session_state.moods)}")

    if st.button("⬅️ Volver al inicio", use_container_width=True):
        st.session_state.page = "home"

