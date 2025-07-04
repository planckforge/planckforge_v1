import streamlit as st
import datetime
import requests

# Set page config
st.set_page_config(page_title="PlanckForge ΣΣτ v1", layout="centered")

# Header animation feel
st.markdown("<h1 style='text-align: center;'>🚀 PlanckForge ΣΣτ v1</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Experimental Simulation Engine | Emotional Multiverse Projection</p>", unsafe_allow_html=True)
st.markdown("---")

# Simulate matrix scan
with st.spinner("🧠 Scanning emotional grid..."):
    st.markdown("`Initializing quantum modules...`")
    st.markdown("`Locating you in decision fabric...`")
    st.markdown("`Connecting to the Planck Forge...`")

# Timestamp & Location info
now = datetime.datetime.now()
st.markdown(f"**🕒 Current Time:** `{now.strftime('%A, %d %B %Y, %I:%M %p')}`")

# Try to get location using IP
try:
    ip_data = requests.get("https://ipinfo.io").json()
    city = ip_data.get("city", "Unknown")
    region = ip_data.get("region", "")
    st.markdown(f"**📍 Location Detected:** `{city}, {region}`")
except:
    st.markdown("**📍 Location:** Unable to detect.")

st.markdown("---")

# Emotion Input
st.subheader("🔍 Emotional Signature Input")
mood = st.selectbox("Current mood", ["Anxious", "Hopeful", "Happy", "Lost", "Motivated"])
clarity = st.selectbox("Clarity of mind", ["Clear", "Foggy", "Racing thoughts"])
hope = st.radio("Do you believe something good will happen soon?", ["Yes", "No"])
desire = st.text_input("What do you desire most right now? (One line)")

if st.button("🔮 Begin Simulation"):
    st.markdown("### 🧬 Timeline Possibilities Detected:")
    st.success("🟢 Timeline A: A peaceful outcome. Something unexpectedly good lifts your spirit.")
    st.warning("🟡 Timeline B: Delay in results, but your mental clarity will sharpen.")
    st.error("🔴 Timeline C: An emotional push from someone forces introspection.")
    st.info("🔵 Timeline D: A breakthrough idea arrives. You surprise even yourself.")

    st.markdown("---")
    st.markdown("#### ✅ Recommended Action")
    st.markdown(f"If you focus on **{desire}**, your Timeline B may merge into A.")

    st.markdown("---")
    st.markdown("⚠️ *Remember: The future is a mirror of your current intention. You are the source code.*")

