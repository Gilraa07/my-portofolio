import streamlit as st

st.title("🌐 Sosial Media & Kontak")
st.write("Temukan dan terhubung dengan saya melalui platform di bawah ini:")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.subheader("📸 Instagram")
        st.image("pages/ig.jpeg", width=200)
        st.write("Akun: @gil.raa__")
        st.link_button("Buka Instagram", "https://www.instagram.com/gil.raa__")

with col2:
    with st.container(border=True):
        st.subheader("📧 Email")
        st.markdown("<br>", unsafe_allow_html=True)
        st.write("Kirimkan pesan atau pertanyaan kepada saya melalui email:")
        st.code("ragiljambi122@gmail.com")
        st.link_button("Kirim Email", "mailto:ragiljambi122@gmail.com")

st.markdown("---")
st.page_link("app.py", label="Kembali ke Halaman Home", icon="🏠")