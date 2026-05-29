
import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os
from datetime import date, timedelta

load_dotenv()

st.set_page_config(page_title="OvaCare", page_icon="🌸", layout="wide")
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family:'Poppins',sans-serif;
}

/* Main App */

.stApp{
    background:
    linear-gradient(
    135deg,
    #FFF7FB 0%,
    #FFE6F0 50%,
    #FFF7FB 100%
    );
}

/* Hide Streamlit Branding */

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

/* Sidebar */

[data-testid="stSidebar"]{
    background:
    linear-gradient(
    180deg,
    #FFD9E8,
    #FFF0F6
    );

    border-right:1px solid rgba(255,255,255,0.3);
}

/* Hero Section */

.hero{

padding:60px;

border-radius:35px;

background:
rgba(255,255,255,0.55);

backdrop-filter: blur(15px);

box-shadow:
0 8px 32px rgba(0,0,0,0.08);

text-align:center;

margin-bottom:25px;
}

.hero h1{
font-size:58px;
font-weight:700;
color:#C2185B;
margin-bottom:10px;
}

.hero p{
font-size:20px;
color:#555;
}

/* Dashboard Cards */

.card{

background:
rgba(255,255,255,0.7);

backdrop-filter: blur(10px);

padding:30px;

border-radius:28px;

box-shadow:
0 10px 30px rgba(0,0,0,0.08);

transition:0.4s ease;

margin-bottom:20px;
}

.card:hover{

transform:
translateY(-8px)
scale(1.02);

box-shadow:
0 18px 40px rgba(214,51,132,0.18);
}

/* Section Cards */

.module{

background:white;

padding:25px;

border-radius:25px;

box-shadow:
0 10px 25px rgba(0,0,0,0.08);

margin-top:15px;
}

/* Buttons */

.stButton>button{

width:100% !important;

background:
linear-gradient(
90deg,
#D63384,
#FF66B2
) !important;

color:white !important;

border:none !important;

font-weight:600 !important;
}

.stButton>button p{
    color:white !important;
}

.stButton>button span{
    color:white !important;
}
color:white;

border:none;

border-radius:18px;

padding:14px;

font-size:16px;

font-weight:600;

transition:0.3s;
}

.stButton>button:hover{

transform:translateY(-3px);

box-shadow:
0 10px 25px rgba(214,51,132,0.35);
}

/* Inputs */

.stTextInput input,
.stNumberInput input,
.stTextArea textarea{

border-radius:15px !important;
border:1px solid #F5B5D2 !important;
}

/* Tabs */

button[data-baseweb="tab"]{

font-size:16px;
font-weight:600;

border-radius:12px;

padding:10px 20px;
}

button[data-baseweb="tab"][aria-selected="true"]{

background:#FADAE7 !important;

color:#C2185B !important;
}

/* Metrics */

[data-testid="stMetric"]{

background:white;

padding:20px;

border-radius:20px;

box-shadow:
0 5px 15px rgba(0,0,0,0.05);
}

/* Chat */

.stChatMessage{

border-radius:20px;

padding:10px;

background:white;
}

/* Scrollbar */

::-webkit-scrollbar{
width:8px;
}

::-webkit-scrollbar-thumb{
background:#F5B5D2;
border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

client = Groq(api_key=os.getenv("GROQ_API_KEY")) if os.getenv("GROQ_API_KEY") else None

def ask_ai(prompt):
    if not client:
        return "Add GROQ_API_KEY to .env"
    r = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role":"system","content":"You are OvaCare Pro, a women's health AI assistant."},
            {"role":"user","content":prompt}
        ]
    )
    return r.choices[0].message.content

for k in ["pain_log","flash_log","pcos_chat","endo_chat","fertility_chat","meno_chat"]:
    if k not in st.session_state:
        st.session_state[k] = []

st.markdown("""
<div class="hero">

<h1>🌸 OvaCare </h1>

<p>
AI-Powered Women's Health Ecosystem
</p>

<p>
PCOS • Endometriosis • Fertility • Menopause
</p>

</div>
""", unsafe_allow_html=True)
st.caption("Women's Health AI Ecosystem")

st.warning("Medical Disclaimer: Educational purposes only. Consult a qualified doctor for diagnosis and treatment.")

module = st.sidebar.radio(
    "Health Journey",
    ["🏠 Home","🧬 PCOS / PCOD","🩸 Endometriosis","👶 Fertility Optimization","🍂 Menopause & Perimenopause"]
)

if module == "🏠 Home":
    c1,c2 = st.columns(2)
    with c1:
        st.info("🧬 PCOS / PCOD")
        st.info("🩸 Endometriosis")
    with c2:
        st.info("👶 Fertility")
        st.info("🍂 Menopause")
    st.success("AI Diet Plans • Fitness • Symptom Analysis • Mental Wellness • Predictors")

elif module == "🧬 PCOS / PCOD":
    st.sidebar.header("Clinical Profile")
    focus = st.sidebar.selectbox("Condition", ["PCOD","PCOS"])
    pcos_type = st.sidebar.selectbox("Type",["Insulin Resistant","Inflammatory","Adrenal","Post-Pill"])
    age = st.sidebar.number_input("Age",12,60,22)
    weight = st.sidebar.number_input("Weight (kg)",30,150,60)
    height = st.sidebar.number_input("Height (cm)",100,220,160)
    cycle = st.sidebar.slider("Cycle Length",21,90,30)

    tabs = st.tabs(["🥗 Diet Planner","🏃 Fitness Coach","🩺 Symptom Analyzer","💊 Medicine Reminder","🧠 Mental Health","📅 Period Predictor","⚖️ BMI Calculator","🤖 AI Chat"])

    with tabs[0]:
        if st.button("Generate Diet Plan"):
            st.write(ask_ai(f"Create PCOS diet plan for {pcos_type}"))

    with tabs[1]:
        if st.button("Generate Fitness Plan"):
            st.write(ask_ai("Create PCOS fitness plan"))

    with tabs[2]:
        acne=st.checkbox("Acne")
        hair=st.checkbox("Hair Fall")
        wg=st.checkbox("Weight Gain")
        ip=st.checkbox("Irregular Periods")
        if st.button("Analyze Symptoms"):
            st.write(ask_ai(f"Acne={acne}, Hair Fall={hair}, Weight Gain={wg}, Irregular Periods={ip}"))

    with tabs[3]:
        med=st.text_input("Medicine Name")
        tm=st.time_input("Reminder Time")
        if st.button("Save Reminder"):
            st.success(f"Reminder saved for {med} at {tm}")

    with tabs[4]:
        mood=st.text_area("How are you feeling today?")
        if st.button("Get Support"):
            st.write(ask_ai(f"Mental support: {mood}"))

    with tabs[5]:
        lp=st.date_input("Last Period Date", date.today())
        st.info(f"Predicted Next Period: {lp + timedelta(days=cycle)}")

    with tabs[6]:
        bmi=weight/((height/100)**2)
        st.metric("BMI", round(bmi,2))

    with tabs[7]:
        q=st.text_input("Ask AI", key="pcos_q")
        if st.button("Send", key="pcos_send"):
            st.write(ask_ai(q))

elif module == "🩸 Endometriosis":
    st.header("Endometriosis Support")
    tabs = st.tabs(["🔥 Pain Tracker","🥗 Anti-Inflammatory Diet","🩺 Symptom Checker","💊 Medication Support","🧠 Mental Wellness","🤖 AI Chat"])

    with tabs[0]:
        pain = st.slider("Pain Level",0,10,5)
        if st.button("Save Pain"):
            st.session_state.pain_log.append(pain)
        if st.session_state.pain_log:
            st.line_chart(st.session_state.pain_log)

    with tabs[1]:
        if st.button("Generate Diet"):
            st.write(ask_ai("Anti-inflammatory diet for endometriosis"))

    with tabs[2]:
        vals = [
            st.checkbox("Pelvic Pain"),
            st.checkbox("Painful Periods"),
            st.checkbox("Painful Intercourse"),
            st.checkbox("Fatigue"),
            st.checkbox("Bloating"),
        ]
        if st.button("Check Symptoms"):
            st.write(ask_ai(f"Endometriosis symptoms {vals}"))

    with tabs[3]:
        st.text_input("Medicine")
        st.time_input("Time", key="endo_time")

    with tabs[4]:
        mood=st.text_area("Mental Wellness", key="endo_mood")
        if st.button("Support Me"):
            st.write(ask_ai(mood))

    with tabs[5]:
        q=st.text_input("Ask AI", key="endo_q")
        if st.button("Send", key="endo_send"):
            st.write(ask_ai(q))

elif module == "👶 Fertility Optimization":
    st.header("Fertility Optimization")
    tabs = st.tabs(["📅 Ovulation Tracker","🥗 Fertility Nutrition","🧬 Fertility Assessment","🧠 Stress Management","🤖 AI Chat"])

    with tabs[0]:
        lp = st.date_input("Last Period", date.today())
        cl = st.slider("Cycle Length",21,40,28)
        ov = lp + timedelta(days=cl-14)
        st.success(f"Ovulation: {ov}")
        st.info(f"Fertile Window: {ov-timedelta(days=5)} to {ov+timedelta(days=1)}")

    with tabs[1]:
        if st.button("Nutrition Plan"):
            st.write(ask_ai("Fertility nutrition plan"))

    with tabs[2]:
        age = st.number_input("Age",18,50,25)
        rc = st.selectbox("Regular Cycles?",["Yes","No"])
        stress = st.selectbox("Stress Level",["Low","Medium","High"])
        if st.button("Assess"):
            st.write(ask_ai(f"Age {age}, cycles {rc}, stress {stress}"))

    with tabs[3]:
        if st.button("Stress Tips"):
            st.write(ask_ai("Fertility stress management"))

    with tabs[4]:
        q=st.text_input("Ask AI", key="fert_q")
        if st.button("Send", key="fert_send"):
            st.write(ask_ai(q))

elif module == "🍂 Menopause & Perimenopause":
    st.header("Menopause Transition Support")
    tabs = st.tabs(["🔥 Hot Flash Tracker","🥗 Nutrition","🦴 Bone Health","😴 Sleep Support","🧠 Mental Wellness","🤖 AI Chat"])

    with tabs[0]:
        sev = st.selectbox("Severity",["Mild","Moderate","Severe"])
        if st.button("Save Flash"):
            st.session_state.flash_log.append({"Mild":1,"Moderate":2,"Severe":3}[sev])
        if st.session_state.flash_log:
            st.line_chart(st.session_state.flash_log)

    with tabs[1]:
        if st.button("Nutrition Guide"):
            st.write(ask_ai("Menopause nutrition guide"))

    with tabs[2]:
        calcium = st.slider("Calcium",0,100,50)
        vitd = st.slider("Vitamin D",0,100,50)
        ex = st.slider("Exercise",0,100,50)
        st.progress(min((calcium+vitd+ex)/300,1.0))

    with tabs[3]:
        if st.button("Sleep Tips"):
            st.write(ask_ai("Menopause sleep support"))

    with tabs[4]:
        mood = st.text_area("How do you feel?", key="meno_mood")
        if st.button("Get Wellness Support"):
            st.write(ask_ai(mood))

    with tabs[5]:
        q=st.text_input("Ask AI", key="meno_q")
        if st.button("Send", key="meno_send"):
            st.write(ask_ai(q))
