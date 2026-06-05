import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Mahindra University School of Management",
    page_icon="🎓",
    layout="wide"
)

# Header
st.title("🎓 Mahindra University School of Management")
st.subheader("Shaping Future Business Leaders Through Innovation, Excellence, and Impact")

# Hero Section
st.markdown("""
Welcome to the **School of Management at Mahindra University**, where academic rigor meets industry relevance.

Our programs are designed to develop visionary leaders equipped with the knowledge, skills, and ethical foundations needed to thrive in a rapidly evolving global business environment.
""")

# Features Section
st.header("Why Choose Us?")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 📚 Industry-Aligned Curriculum
    Learn through a modern curriculum that integrates business fundamentals, analytics, technology, and leadership.
    """)

with col2:
    st.markdown("""
    ### 🤝 Strong Industry Connections
    Benefit from collaborations, internships, live projects, and mentorship opportunities with leading organizations.
    """)

with col3:
    st.markdown("""
    ### 🌍 Global Perspective
    Develop a global mindset through interdisciplinary learning and exposure to contemporary business challenges.
    """)

# Programs Section
st.header("Our Programs")

st.markdown("""
- MBA and Management Programs
- Business Analytics
- Entrepreneurship & Innovation
- Finance, Marketing, and Operations
- Leadership Development
""")

# Vision Section
st.header("Our Mission")

st.info("""
To nurture responsible, innovative, and entrepreneurial leaders who create sustainable value for organizations and society.
""")

# Call to Action
st.header("Join the Next Generation of Leaders")

st.success("""
Explore opportunities at Mahindra University School of Management and begin your journey toward impactful leadership.
""")

if st.button("Learn More"):
    st.balloons()
    st.write("Thank you for your interest in Mahindra University School of Management!")

# Footer
st.markdown("---")
st.caption("© 2026 Mahindra University School of Management")
