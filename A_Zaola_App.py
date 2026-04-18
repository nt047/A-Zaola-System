import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="A-ZAOLA VIP", layout="wide")

# التصميم بصيغة مبسطة لمنع أخطاء التنسيق
st.markdown("<style>body{background-color:#000;color:#D4AF37;}.stApp{background-color:#000;} h1{color:#D4AF37;text-align:center;}</style>", unsafe_allow_input=True)

st.title("⚡ A-ZAOLA SUPREME INTELLIGENCE ⚡")

# القائمة الجانبية
st.sidebar.title("⚜️ VIP COMMAND")
menu = st.sidebar.selectbox("القائمة", ["الأدوات", "الموسوعة", "المحلل"])

if menu == "الأدوات":
    st.write("### مرحباً بك سيدي A-Zaola في نظامك السحابي")
    st.button("بدء فحص الثغرات")
    
elif menu == "المحلل":
    st.write("### قسم تحليل الأكواد الممنوعة")
    st.text_area("ألصق الكود هنا")
    st.button("تحليل الآن")
