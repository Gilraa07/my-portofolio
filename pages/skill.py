import streamlit as st

st.title("⚡ Kemampuan & Skills")
st.write("Berikut adalah tingkat kemampuan dan perkembangan keahlian yang saya miliki:")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.write("Pemrograman Python")
    st.progress(80)
    
    st.write("Web Development")
    st.progress(80)
    
    st.write("Bahasa Inggris")
    st.progress(85)

with col2:
    st.write("Database & SQL")
    st.progress(80)
    
    st.write("Public Speaking")
    st.progress(80)

st.markdown("---")
st.page_link("app.py", label="Kembali ke Halaman Home", icon="🏠")