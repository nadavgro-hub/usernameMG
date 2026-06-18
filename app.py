import streamlit as st
import pandas as pd

# הגדרת כותרת לעמוד הדפדפן והעיצוב
st.set_page_config(page_title="איתור שם משתמש", page_icon="🔑", layout="centered")

# כותרות באתר
st.title("🔑 מערכת לאחזור שם משתמש")
st.write("הזן את כתובת האימייל שלך כדי לקבל את שם המשתמש המערכתי.")

# נתוני המשתמשים (מוטמעים ישירות בקוד לנוחות מקסימלית)
data = {
    "Username": [
        "IL008637", "5000SSNW20", "ASILDT01SSNW05", "ASILDT01SSNW03", "ASIL04001SSNW02",
        "ASILDT01SSNW15", "ASILDT01SSNW14", "ASILDT01SSNW13", "ASILDT01SSNW16", "ASIL24013SSNW01",
        "ASIL24009SSNW02", "ASIL24016SSNW02", "ASIL25024SSNW01", "ASIL25026SSNW01", "ASIL25025SSNW01",
        "IL012430", "IL012429", "ASIL24017SSNW01", "ASIL24005SSNW01", "IL008418",
        "ASIL24009SSNW01", "ASIL24006SSNW01", "ASIL04001SSNW05", "IL008415", "IL012431",
        "ASIL04001SSNW01", "ASIL24010SSNW01", "ASIL24020SSNW01", "ASIL25023SSNW01", "ASIL25022SSNW01",
        "ASIL24018SSNW02", "ASIL25021SSNW01", "IL010601", "IL018712", "IL018740",
        "IL018730", "IL018708", "IL018709", "IL018718", "IL018710", "IL018714",
        "IL018711", "IL018736", "IL018742", "IL018741", "IL018713", "IL018743",
        "IL018721", "IL018739", "IL018717", "IL018735", "IL018738", "IL018720",
        "IL018715", "IL018737", "IL018719", "IL018724", "IL018734", "IL018727",
        "IL018732", "IL018716", "IL018729", "IL018731", "IL018723", "IL018733",
        "IL018726", "IL018725", "IL018728", "IL016195", "IL016275", "ASILDT01SSNW02",
        "ASIL25026SSNW02", "ASILDT01SSNW01", "IL018722"
    ],
    "User email": [
        "DANIIV@LUBINSKI.CO.IL", "jie.liu@smil.com", "alonha@lubinski.co.il", "orengu@lubinski.co.il", "DIAGNOZ@lubinski.co.il",
        "arikra@lubinski.co.il", "ofekuz@lubinski.co.il", "daniel.yvray@lubinski.co.il", "iziksg@lubinski.co.il", "eytan@goldmotors.co.il",
        "mosheb89h@gmail.com", "itayavigdor@gmail.com", "asa@hagavish.co.il", "dudio7872@gmail.com", "euro2016karmiel@gmail.com",
        "Office@euromotors.co.il", "avisi@lubinski.co.il", "asaf.haogen@gmail.com", "kibru12345@gmail.com", "ramib5855@gmail.com",
        "wampardiagnostic@gmail.com", "yg.barel@gmail.com", "michaelko@lubinski.co.il", "petah.tikva.lital@gmail.com", "Polskyvalery@gmail.com",
        "adamma@lubinski.co.il", "diagnostic@ymgarage.com", "monzadtm@gmail.com", "kamaktec@gmail.com", "mark@ramco-motors.com",
        "shlomicarmeli@gmail.com", "Sdabbah66@gmail.com", "sharaton27@gmail.com", "hamudi490@gmail.com", "ansan_mohmed@hotmail.com",
        "Wampar@walla.co.il", "Shalomno@lubinski.co.il", "shacharbs@lubinski.co.il", "hen94turgeman@gmail.com", "itasael1966@gmail.com",
        "mabwaldwlh075@gmail.com", "Abrashqa2788@hotmail.com", "orluzon14@gmail.com", "Heliassaf@gmail.com", "h.shami1702@gmail.com",
        "shlominn20@gmail.com", "dorigelbart@gmail.com", "tzahi1986@gmail.com", "Yifats22@gmail.com", "ghassant741@gmail.com",
        "swd941119@gmail.com", "tannous77@gmail.com", "raviv0542456103@gmail.com", "Oz@alfamoris.co.il", "Remon.bal81@gmail.com",
        "Leokill55@gmail.com", "Itzikife@gmail.com", "Nikitalitalpt@gmail.com", "yoni131313@gmail.com", "yurikchip@gmail.com",
        "amjadmhamed4@gmail.com", "Udi@lital.org.il", "Sndmasalha1@gmail.com", "testusertwo@gmdail.com", "Yossef100@gmail.com",
        "tomer.ostrovsky@gmail.com", "michael.moraeb@gmail.com", "lirazbarak4545@gmail.com", "Ormor.keren@gmail.com", "gabi@goldmotors.co.il",
        "alexbo@lubinski.co.il", "opelcircuit@gmail.com", "nadavgross@lubinski.co.il", "testuserone@gmdail.com"
    ]
}

# יצירת DataFrame וניקוי רווחים קצוות
df = pd.DataFrame(data)
df['User email'] = df['User email'].str.strip().str.lower()

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
