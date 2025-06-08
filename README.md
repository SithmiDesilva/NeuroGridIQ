# ⚡ NeuroGridIQ: Smart Grid Fuzzy Anomaly Detection and Correction System  
> - Detecting power anomalies using voltage, frequency, and load imbalance inputs  
> - A complete fuzzy logic project from reasoning to real-time deployment

## 🎯 What This Project Does  
This project addresses the challenge of **detecting and responding to anomalies** in a power grid system using fuzzy logic. It takes **three key inputs** from the power system:

- Voltage Deviation (%)
- Frequency Variation (Hz from 50Hz)
- Load Imbalance (%)

It then determines how **severe** the anomaly is and suggests **corrective actions** all based on expert-defined fuzzy rules and severity mapping.

Think of it as building an **intelligent assistant** for electrical grids that can say:  
*"Something’s wrong — and here’s what you should do about it!"*

## 🤔 Why This Matters  
Smart grids require **robust, interpretable, and flexible control** to avoid blackouts, damage to equipment, and instability.  
Fuzzy logic allows for **human-like reasoning** in uncertain or overlapping conditions.

- ⚡ Grid Reliability: Detect and correct abnormal behavior in real time  
- 🔄 Preventive Control: Catch issues before they escalate  
- 📈 Interpretability: Understand *why* a correction is needed not just *what*  

## 📊 The Data used 
Instead of a traditional dataset, this system relies on **live or simulated sensor inputs**:
- 🔌 Voltage Deviation (0–100%)
- 🔁 Frequency Variation (0.0–2.0 Hz deviation)
- ⚖️ Load Imbalance (0–100%)

We simulate multiple **test cases** to validate how well the system responds under varying grid conditions.

## 🔍 What I Discovered  
1. 🔥 Fuzzy Rules Make Intuition Programmable  
By carefully defining fuzzy membership functions and rule logic, we capture complex expert reasoning in a few lines of code.

2. 📈 The Severity Mapping is Clear and Effective  
Severity levels (0–3) translate directly into actions. For example:
- 3 → Isolate Faulty Section
- 2 → Balance Load or Adjust Frequency
- 1 → Tune Power Factor
- 0 → No Action Needed

3. 🎭 The Logic is Explainable  
Each decision is based on **simple, visible conditions** like:
> "If voltage is high, frequency is unstable, and load is unbalanced → High Severity"

## 📁 Project Structure 
📂 NeuroGridIQ  
├── 🧠 Source_code.py               
├── 🌐 app.py                 
└── 📖 README.md           

## 🚀 How to Use This Project  
### Quick Start  
1. Install dependencies (only Streamlit required):  
   ```bash
   pip install streamlit
   
2. Run the app locally
   ```bash
   streamlit run app.py
   
3. Use sliders to input:
   - Voltage deviation
   - Frequency variation
   - Load imbalance
     
4. View:
   - Severity Level (0–3)
   - Suggested Correction Action

## 🧪 Key Findings & Lessons

✅ What Works Well
   - Fuzzy membership functions for gradual transitions
   - Rule-based reasoning captures expert intuition
   - Clear mapping from severity to action
   - Streamlit provides excellent interactive demo

⚠️ Lessons Learned
   - Fuzzy logic is highly interpretable, but rule design must be carefully curated
   - Triangular membership functions are effective and simple to tune
   - Even a simple system with only three variables can model complex grid scenarios

## 🎓 What This Project Teaches

This is a real-world demonstration of:
 - 🧠 Applying fuzzy logic to real-time control systems
 - 📊 Translating sensor input into human-like decisions
 - 🎛️ Building interpretable automation for critical infrastructure
 - 💬 Explaining decision logic to engineers and operators

## 🚧 Current Status & Next Steps

✅ Completed
   - Core fuzzy rule system
   - Action mapping logic
   - Interactive Streamlit app

🎯 Future Enhancements
  - Integrate with real-time SCADA/IoT sensor feeds
  - Add logging system for anomaly pattern tracking
  - Deploy on Raspberry Pi or edge device for field use
  - Adaptive fuzzy system that learns from feedback

## 🤝 Contribution
This project is a demonstration of fuzzy control in smart grids. You’re welcome to:
     - Tune fuzzy rules and thresholds
     - Expand to new inputs like power factor or THD
     - Add graphical outputs like severity timelines
     
## 📌 Bottom Line
> NeuroGridIQ combines the intuition of grid engineers with the precision of fuzzy logic to detect and respond to anomalies in real time.
> It's lightweight, interpretable, expandable, and ready for real-world power system deployment.




    
    
     
