import streamlit as st
from brett_data_backend import get_indicator_status, get_current_alignment

st.set_page_config(page_title="🚀 Brett Euphoria Meter", layout="centered")

st.title("🚀 Brett Euphoria Meter")
st.write("Track Brett coin euphoria indicators and simulate scale-out strategy.")

# --- Current Indicator Alignment ---
status = get_indicator_status()
alignment = get_current_alignment(status)

fired = sum(status.values())
total = len(status)
euphoria = fired >= 7

st.subheader("Current Indicator Alignment")
st.write(f"**{fired} out of {total} indicators fired** {'(Euphoria!)' if euphoria else ''}")
st.progress(fired / total)

# --- Exit Strategy Mode Toggle ---
st.subheader("Exit Strategy Mode")
mode = st.radio("Choose your scale-out mode:", ["Strict 9/9 Mode", "Flexible 7+ Mode"])
if mode == "Strict 9/9 Mode":
    st.markdown("🔴 **Strict 9/9 Mode**: Only exit if all 9 indicators are active.")
else:
    st.markdown("🟢 **Flexible 7+ Mode**: Begin exit once 7 or more indicators are active.")

# --- Simulate Future Exit Price ---
st.subheader("🔮 Simulate Future Exit Price")
future_price = st.number_input("Enter Brett Price ($)", min_value=0.01, value=0.06, step=0.01)
st.success(f"At ${future_price:.2f}, your exit strategy will trigger if indicators align with selected mode.")

# --- Simulate Historical Date ---
st.subheader("📅 Simulate Historical Date")
st.date_input("Pick a Date")
st.info("📌 Historical simulation feature coming soon!")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Bestie & Jake")
