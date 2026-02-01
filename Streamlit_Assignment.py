import streamlit as st

st.set_page_config(
    page_title="Asiphe Tsokotsiyana | Research Profile",
    layout="wide"
)

# ==================================================
# HEADER
# ==================================================
st.title("Asiphe Tsokotsiyana, BSc (Hons)")
st.subheader(
    "Ocean Research Intern | "
    "Department of Forestry, Fisheries and the Environment (DFFE)"
)

st.markdown("""
📍 Cape Town, South Africa   
📧 Email: asiphetsokotsiyane@gmail.com  
🔗 LinkedIn: www.linkedin.com/in/asiphe-tsokotsiyana-0ab534197 
""")

st.divider()

# ==================================================
# 1. PROFESSIONAL SUMMARY
# ==================================================
st.header("Professional Summary")

st.markdown("""
I am a graduate in Ichthyology and Fisheries Science from Rhodes University with training in
fisheries science, and marine science. My current research focuses on analysing
oceanographic datasets to investigate variability of the
Agulhas Current in the southwestern Indian Ocean, across the ASCA transect. I peform data analysis using Python and MATLAB.
with hands-on field experience in marine, estuarine, and coastal ecosystems.
My broader research interests include climate change impacts, fisheries
management, and marine ecosystem resilience.
""")

st.divider()

# ==================================================
# 2. RESEARCH INTERESTS
# ==================================================
st.header("Research Interests")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **Primary**
    - Agulhas Current variability  
    - Western boundary current dynamics  
    - Physical Oceanography 
    """)

with col2:
    st.markdown("""
    **Secondary**
    - Fisheries science  
    - Marine ecosystem resilience  
    - Climate change impacts  
    """)

with col3:
    st.markdown("""
    **Technical Skills**
    - Python, MATLAB, R""")

st.divider()

# ==================================================
# 3. PROFESSIONAL PREPARATION (EDUCATION)
# ==================================================
st.header("Professional Preparation (Education)")

st.markdown("""
**2023 - Bachelor of Science (Honours) in Ichthyology & Fisheries Science**
 
Rhodes University, South Africa  
Honours Thesis: *Predator-prey interactions at Tsitsikamma National Park Marine Protected Area*

**2021 - Advanced Diploma in Marine Science**  
Cape Peninsula University of Technology, South Africa**
""")

st.divider()

# ==================================================
# 4. APPOINTMENTS & POSITIONS
# ==================================================
st.header("Appointments & Positions")

st.markdown("""
**2024 - Present - Intern (Marine & Oceanographic Research)**  
Department of Forestry, Fisheries and the Environment (DFFE)  
- Research on annual and seasonal climatological variability of the Agulhas Current  
- Analysis of temperature, salinity, and density data using Python and MATLAB  
- Participation in national rocky shore, estuarine, and marine mammal monitoring programmes  

**2023 - Research Student**  
South African Institute for Aquatic Biodiversity (SAIAB) - 
- Conducted honours research on predator - prey interactions using BRUVS in a Marine Protected Area  
""")

st.divider()

# ==================================================
# 5. SELECTED RESEARCH PRODUCTS
# ==================================================
st.header("Selected Research Products")

st.markdown("Peer-reviewed publications (in preparation")

("Internship Research Project (Ongoing): Variability of the Agulhas Current along the ASCA transect")

st.divider()

# ==================================================
# 6. TRAINING & CERTIFICATIONS
# ==================================================
st.header("Synergistic Activities & Certifications")

st.markdown(
    "**Professional Registration**\n"
    "- SACNASP Candidate Natural Scientist (Aquatic Science)\n\n"
    "**Training & Short Courses**\n"
    "- Coastal Ocean Environment School (Western Indian Ocean): Physical & Chemical Oceanography\n"
    "- CROCCO Basic Modelling Course\n"
    "- CROCCO Air-Sea Interaction Advanced Course\n"
    "- Ocean Data Management (2025)\n"
    "- ArcGIS Pro - Basic Course\n\n"
    "**Field & Service Activities**\n"
    "- Rocky shore biodiversity monitoring\n"
    "- Estuarine health assessments (Orange River)\n"
    "- Cape fur seal pup growth monitoring\n"
    "- Humpback whale behavioural observations"
)

st.divider()


st.divider()

st.divider()




st.markdown(
    "<center>© Asiphe Tsokotsiyana | Marine & Ocean Science Researcher</center>",
    unsafe_allow_html=True
)
