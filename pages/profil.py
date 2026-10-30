import streamlit as st

st.title("👤 Halaman Profil")
st.write("Selamat datang di halaman profil saya!")
st.markdown("---")

with st.container():
    st.header("Informasi Pribadi")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("pages/Ragil1.jpg", width=250)

    with col2:
        st.write("Nama : Ragil Prakoso")
        st.write("Program Studi : Sistem Informasi")
        st.write("Hobi : Membaca, Menolong Orang, Bergotong Royong, Mendengarkan Musik")
        st.write("Motto Hidup : Belajar tanpa henti, berkarya tanpa batas.")
        st.write("Minat Keilmuan : Web Development, Data Science, Artificial Intelligence")

st.markdown("---")
st.page_link("app.py", label="Kembali ke Halaman Home", icon="🏠")