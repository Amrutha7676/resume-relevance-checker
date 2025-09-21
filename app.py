import streamlit as st
from modules.extractors import extract_text_from_file
from modules.relevance_checker import check_relevance

# ---- Page config ----
st.set_page_config(page_title="Resume Relevance Checker", layout="wide")

# ---- Inject CSS for styling ----
st.markdown("""
<style>
/* Blue file uploader buttons */
div.stFileUploader>div>div>label>div[data-baseweb] {
    background-color: #1E90FF;  /* DodgerBlue */
    color: white;
    font-weight: bold;
    border-radius: 5px;
    padding: 0.5em 1em;
}
div.stFileUploader>div>div>label>div[data-baseweb]:hover {
    background-color: #007ACC; /* Darker blue on hover */
}

/* Sidebar header style */
.stSidebar h2 {
    color: #ee0979;
}
</style>
""", unsafe_allow_html=True)

# ---- Main Gradient Title ----
st.markdown("""
<div style="background: linear-gradient(90deg, #ff6a00, #ee0979, #8e2de2);
            padding: 10px; border-radius:10px; text-align:center;">
    <h1 style="color:white; margin:0;">📄 Resume Relevance Checker</h1>
</div>
""", unsafe_allow_html=True)

# ---- Subtitle BELOW the title ----
st.markdown("""
<p style="text-align:center; font-size:16px; color:#555; margin-top:5px;">
A smart tool for placement teams to find the perfect candidates for job opportunities.
</p>
""", unsafe_allow_html=True)


# ---- Sidebar: Job Requirements ----
with st.sidebar:
    st.header("📂 Job Requirements Board")
    jd_file = st.file_uploader("Upload Job Description", type=["pdf", "docx", "txt"])
    jd_text = ""
    if jd_file:
        jd_text = extract_text_from_file(jd_file)
    else:
        jd_text = st.text_area("Or paste Job Description here:")

# ---- Function to clean and preserve paragraphs ----
def format_jd_text(jd_text):
    """
    Clean the JD text and combine lines into proper paragraphs.
    Returns a list of paragraphs.
    """
    lines = [line.strip() for line in jd_text.splitlines() if line.strip()]
    paragraphs = []
    current_paragraph = ""
    for line in lines:
        if line.endswith(('.', '?', '!', ';')):
            current_paragraph += " " + line
            paragraphs.append(current_paragraph.strip())
            current_paragraph = ""
        else:
            current_paragraph += " " + line
    if current_paragraph:
        paragraphs.append(current_paragraph.strip())
    return paragraphs

# ---- Right Dashboard ----
st.header("📝 Dashboard")

if jd_text:
    # Display processed job description
    paragraphs = format_jd_text(jd_text)
    st.subheader("📌 Processed Job Description")
    for para in paragraphs:
        st.markdown(para + "\n")

    # Resume upload section
    resume_files = st.file_uploader(
        "Upload Resumes", type=["pdf", "docx"], accept_multiple_files=True
    )

    if resume_files:
        st.subheader("📊 Relevance Scores")
        for resume_file in resume_files:
            resume_text = extract_text_from_file(resume_file)
            score = check_relevance(jd_text, resume_text)
            st.markdown(f"**{resume_file.name}:** {score}")
            # ---- Footer ----
st.markdown("""
<div style="text-align:center; padding:10px; margin-top:30px;
            border-top:1px solid #ccc; color: #555; font-size:14px;">
    Developed by <strong>Amrutha</strong> 💻
</div>
""", unsafe_allow_html=True)

