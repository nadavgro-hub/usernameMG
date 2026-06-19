import streamlit as st

# הגדרת עמוד ועיצוב בסיסי
st.set_page_config(page_title="איתור שם משתמש", page_icon="🔑", layout="centered")

# 🔒 קוד אבטחה: חסימת תפריטים, כפתור ה-GitHub ואפשרות צפייה בקוד (View Source)
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stAppDeployButton {display:none;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# כותרות האתר
st.title("🔑 מערכת לאחזור שם משתמש")
st.write("הזן את כתובת האימייל שלך כדי לקבל את שם המשתמש המערכתי.")

try:
    # שליפת המידע המאובטח מתוך ה-Secrets של האפליקציה
    user_dict = st.secrets["user_data"]

    # תיבת קלט מהמשתמש
    email_input = st.text_input("כתובת אימייל:", value="").strip().lower()

    # כפתור בדיקה
    if st.button("הצג שם משתמש"):
        if email_input:
            # בדיקה ישירה במילון הנתונים
            if email_input in user_dict:
                username = user_dict[email_input]
                st.success(f"שם המשתמש שלך הוא: **{username}**")
            else:
                st.error("כתובת האימייל לא נמצאה במערכת. אנא ודא שהקלדת אותה נכון.")
        else:
            st.warning("אנא הכנס כתובת אימייל.")

except Exception as e:
    st.error("שגיאה בתצורת המערכת. אנא ודא שהגדרת את ה-Secrets בלוח הבקרה.")
