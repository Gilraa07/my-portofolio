import streamlit as st

st.set_page_config(
    page_title="Portofolio Interaktif - Ragil",
    page_icon="✨",
    layout="wide"
)

st.markdown("<h1 style='text-align: center;'>✨ Selamat Datang di Portofolio Saya ✨</h1>", unsafe_allow_html=True)
st.markdown("---")

st.subheader("📌 Navigasi Cepat")
st.write("Silakan pilih menu di bawah ini atau gunakan sidebar di sebelah kiri untuk menjelajahi halaman:")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.markdown("👤 Profil")
        st.write("Kenali saya lebih dekat, latar belakang, dan hobi.")
        st.page_link("pages/profil.py", label="Buka Profil", icon="🔍")

with col2:
    with st.container(border=True):
        st.markdown("⚡ Skill")
        st.write("Lihat daftar keahlian dan tingkat kemampuan saya.")
        st.page_link("pages/skill.py", label="Buka Skill", icon="📊")

with col3:
    with st.container(border=True):
        st.markdown("🌐 Sosmed")
        st.write("Terhubung dengan saya melalui media sosial.")
        st.page_link("pages/sosmed.py", label="Buka Sosmed", icon="🔗")

st.markdown("---")