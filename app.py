# streamlit_app.py

from Source_code import fuzzy_rule, correction_action
import streamlit as st # type: ignore

st.title("Smart Grid Fuzzy Anomaly Detector")

voltage = st.slider("Voltage Deviation", 0, 100)
freq = st.slider("Frequency Variation (Hz)", 0.0, 2.0, step=0.1)
load = st.slider("Load Imbalance (%)", 0, 100)

severity = fuzzy_rule(voltage, freq, load)
action = correction_action(severity)

st.write(f"Anomaly Severity: {severity}")
st.write(f"Suggested Action: {action}")
