import streamlit as st

st.title("☁️ Cloud Platform Referee")
st.write("This tool helps you compare cloud platforms instead of giving one fixed answer.")

budget = st.selectbox(
    "What is your budget?",
    ["Low", "Medium", "High"]
)

use_case = st.selectbox(
    "What will you use it for?",
    ["Learning", "Startup", "Enterprise"]
)

ease = st.selectbox(
    "How easy do you want it to be?",
    ["Very Easy", "Moderate", "I can handle complexity"]
)

if st.button("Compare Options"):
    st.header("🔍 Comparison")

    st.subheader("AWS")
    st.write("✅ Huge number of services")
    st.write("✅ Largest community and support")
    st.write("❌ Can feel complex")
    st.write("❌ Pricing is hard to understand")

    st.subheader("Azure")
    st.write("✅ Works very well with Microsoft tools")
    st.write("✅ Good for companies")
    st.write("❌ Smaller community than AWS")
    st.write("❌ Interface can feel confusing")

    st.subheader("GCP")
    st.write("✅ Excellent for data and AI work")
    st.write("✅ Clean and simple interface")
    st.write("❌ Smaller ecosystem")
    st.write("❌ Fewer learning resources")

    st.header("⚖️ Trade-Off Explanation")
    st.write(
        "There is no single best cloud platform. "
        "AWS offers the most flexibility but is complex. "
        "Azure is strong for enterprises already using Microsoft. "
        "GCP is easier for data-heavy and AI-focused projects but has fewer integrations."
    )
