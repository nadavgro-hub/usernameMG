import streamlit as st
import pandas as pd

# הגדרת עמוד ועיצוב בסיסי
st.set_page_config(page_title="איתור שם משתמש", page_icon="🔑", layout="centered")

# 🔒 קוד אבטחה: חסימת תפריטים, כפתור ה-GitHub ואפשרות צפייה בקוד (View Source)
hide_streamlit_style = """
    <style>
    /* מחביא את תפריט ההמבורגר בצד ימין/שמאל */
    #MainMenu {visibility: hidden;}
    /* מחביא את כפתורי ה-Deploy והאיקונים של Streamlit למעלה */
    header {visibility: hidden;}
    /* מחביא את כפתור ה-Made with Streamlit למטה */
    footer {visibility: hidden;}
    /* חוסם אלמנטים נוספים של צפייה בקוד של חשבונות גיטהאב מחוברים */
    .stAppDeployButton {display:none;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# כותרות האתר
st.title("🔑 מערכת לאחזור שם משתמש")
st.write("הזן את כתובת האימייל שלך כדי לקבל את שם המשתמש המערכתי.")

# טעינת הנתונים בצורה מאובטחת מקובץ האקסל
@st.cache_data # שומר בזיכרון כדי שהאתר יעבוד מהר
def load_data():
    # קריאת קובץ ה-Excel, דילוג על שתי השורות הריקות הראשונות (skiprows=2)
    df = pd.read_excel("Users_-_detailed_rep_1781759942638.xlsx - sheet1.csv", skiprows=2)
    
    # ניקוי שם העמודות למקרה שיש רווחים נסתרים בכותרת
    df.columns = df.columns.str.strip()
    
    # ניקוי רווחים והפיכה לאותיות קטנות לצורך חיפוש אמין
    df['User email'] = df['User email'].astype(str).str.strip().str.lower()
    return df

try:
    df = load_data()

    # תיבת קלט מהמשתמש
    email_input = st.text_input("כתובת אימייל:", value="").strip().lower()

    # כפתור בדיקה
    if st.button("הצג שם משתמש"):
        if email_input:
            # חיפוש המייל בטבלה
            result = df[df['User email'] == email_input]
            
            if not result.empty:
                username = result.iloc[0]['Username']
                st.success(f"שם המשתמש שלך הוא: **{username}**")
            else:
                st.error("כתובת האימייל לא נמצאה במערכת. אנא ודא שהקלדת אותה נכון.")
        else:
            st.warning("אנא הכנס כתובת אימייל.")

except Exception as e:
    st.error("שגיאה בטעינת בסיס הנתונים. אנא ודא שקובץ האקסל נמצא בתיקייה עם השם המדויק.")
