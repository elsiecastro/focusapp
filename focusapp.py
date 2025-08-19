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

    # 🎵 Música integrada
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

