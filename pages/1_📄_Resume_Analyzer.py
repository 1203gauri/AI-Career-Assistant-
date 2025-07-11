# import streamlit as st
# from utils import pdf_extractor, nlp_utils
# import os
# import datetime

# # Config
# st.set_page_config(page_title="📄 Resume Analyzer", page_icon="📄", layout="wide")

# st.title("📄 Resume Analyzer")

# st.markdown(
#     """
#     Upload your resume (PDF) and select a target job role.  
#     The app analyzes your resume against key skills required for that role and gives you feedback.
#     """
# )

# # Target roles with example keywords
# role_keywords = {   
#     "Data Scientist": ["python", "machine learning", "statistics", "pandas", "tensorflow", "scikit-learn", "deep learning"],
#     "Machine Learning Engineer": ["python", "tensorflow", "pytorch", "mlops", "model deployment", "feature engineering"],
#     "Software Engineer": ["java", "c++", "design patterns", "algorithms", "data structures", "git", "oop"],
#     "Frontend Developer": ["html", "css", "javascript", "react", "vue", "angular", "responsive design", "webpack"],
#     "Backend Developer": ["node.js", "django", "flask", "sql", "nosql", "api development", "microservices"],
#     "Full Stack Developer": ["html", "css", "javascript", "react", "node.js", "api", "sql", "devops"],
#     "DevOps Engineer": ["ci/cd", "docker", "kubernetes", "aws", "terraform", "jenkins", "ansible", "monitoring"],
#     "Cloud Engineer": ["aws", "azure", "gcp", "cloud architecture", "serverless", "cloudformation", "iac"],
#     "Flutter Developer": ["dart", "flutter", "state management", "bloc", "provider", "ui/ux", "firebase"],
#     "Mobile App Developer": ["swift", "kotlin", "flutter", "react native", "android studio", "xcode", "ui/ux"],
#     "Cybersecurity Analyst": ["penetration testing", "network security", "vulnerability assessment", "firewalls", "siem", "encryption", "incident response"],
#     "Blockchain Developer": ["solidity", "ethereum", "smart contracts", "web3.js", "decentralized applications", "nfts"],
#     "Data Engineer": ["etl", "spark", "hadoop", "big data", "airflow", "sql", "data pipelines"],
#     "AI Engineer": ["neural networks", "deep learning", "tensorflow", "pytorch", "nlp", "computer vision", "model optimization"],
#     "UI/UX Designer": ["figma", "adobe xd", "wireframes", "prototyping", "user research", "usability testing"],
#     "QA Engineer": ["manual testing", "automation testing", "selenium", "jmeter", "cypress", "test cases", "bug tracking"],
#     "Product Manager": ["roadmap", "stakeholder management", "agile", "scrum", "user stories", "analytics", "market research"],
#     "Business Analyst": ["requirements gathering", "sql", "data analysis", "stakeholder communication", "process improvement", "documentation"],
#     "Embedded Systems Engineer": ["c", "c++", "microcontrollers", "rtos", "fpga", "hardware interfacing"],
#     "Game Developer": ["unity", "unreal engine", "c#", "game physics", "3d modeling", "animation", "ai in games"],
 
# }

# # Upload resume
# uploaded_file = st.file_uploader("📄 Upload your Resume (PDF only)", type=["pdf"])

# # Select role
# role = st.selectbox("🎯 Select Target Role", options=list(role_keywords.keys()))

# if uploaded_file and role:
#     if st.button("🚀 Analyze Resume"):
#         with st.spinner("Analyzing your resume..."):

#             # Extract text
#             text = pdf_extractor.extract_text_from_pdf(uploaded_file)

#             # Match keywords
#             matched, missing, score = nlp_utils.match_keywords(text, role_keywords[role])

#             st.success(f"✅ Analysis complete! Your resume matches **{score}%** for the role: **{role}**")

#             col1, col2 = st.columns(2)
#             with col1:
#                 st.markdown("### 🎯 Matched Keywords")
#                 st.write(", ".join(matched) if matched else "No matches found.")
#             with col2:
#                 st.markdown("### 🔍 Missing Keywords")
#                 st.write(", ".join(missing) if missing else "None 🎉")

#             # Save report
#             save_dir = "saved_data/feedback_logs"
#             os.makedirs(save_dir, exist_ok=True)
#             timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
#             save_path = os.path.join(save_dir, f"{role}_{timestamp}.txt")

#             with open(save_path, "w") as f:
#                 f.write(f"Role: {role}\nMatch Score: {score}%\n")
#                 f.write(f"Matched: {', '.join(matched)}\n")
#                 f.write(f"Missing: {', '.join(missing)}\n")

#             st.info(f"📁 Report saved to `{save_path}`")

# else:
#     st.info("⬆️ Please upload your resume and select a role to start analysis.")





# import streamlit as st
# from utils import pdf_extractor, nlp_utils
# import os
# import datetime

# st.set_page_config(page_title="📄 Resume Analyzer", page_icon="📄", layout="wide")

# st.markdown("""
# <style>
# .section {
#     background-color: #f9f9f9;
#     padding: 30px;
#     border-radius: 12px;
#     box-shadow: 0 2px 6px rgba(0,0,0,0.1);
# }
# .keywords {
#     display: flex;
#     flex-wrap: wrap;
#     gap: 6px;
#     margin-top: 10px;
# }
# .keyword {
#     background: #e0f7fa;
#     color: #00796b;
#     padding: 6px 10px;
#     border-radius: 6px;
#     font-size: 0.85rem;
# }
# .keyword.missing {
#     background: #ffebee;
#     color: #c62828;
# }
# </style>
# """, unsafe_allow_html=True)

# st.title("📄 Resume Analyzer")

# st.markdown(
#     """
#     <p style="font-size: 1.1rem; color: #555;">
#     Upload your <b>resume (PDF)</b> and choose a <b>target job role</b>.  
#     Get actionable insights on how your resume aligns with your dream job!
#     </p>
#     """, unsafe_allow_html=True
# )

# with st.container():
#     col1, col2, col3 = st.columns([1, 2, 1])
#     with col2:
#         uploaded_file = st.file_uploader("📄 Upload your Resume", type=["pdf"], label_visibility="collapsed")

# role_keywords = {
    # "Data Scientist": ["python", "machine learning", "statistics", "pandas", "tensorflow", "scikit-learn", "deep learning"],
    # "Machine Learning Engineer": ["python", "tensorflow", "pytorch", "mlops", "model deployment", "feature engineering"],
    # "Software Engineer": ["java", "c++", "design patterns", "algorithms", "data structures", "git", "oop"],
    # "Frontend Developer": ["html", "css", "javascript", "react", "vue", "angular", "responsive design", "webpack"],
    # "Backend Developer": ["node.js", "django", "flask", "sql", "nosql", "api development", "microservices"],
    # "Full Stack Developer": ["html", "css", "javascript", "react", "node.js", "api", "sql", "devops"],
    # "DevOps Engineer": ["ci/cd", "docker", "kubernetes", "aws", "terraform", "jenkins", "ansible", "monitoring"],
    # "Cloud Engineer": ["aws", "azure", "gcp", "cloud architecture", "serverless", "cloudformation", "iac"],
    # "Flutter Developer": ["dart", "flutter", "state management", "bloc", "provider", "ui/ux", "firebase"],
    # "Mobile App Developer": ["swift", "kotlin", "flutter", "react native", "android studio", "xcode", "ui/ux"],
    # "Cybersecurity Analyst": ["penetration testing", "network security", "vulnerability assessment", "firewalls", "siem", "encryption", "incident response"],
    # "Blockchain Developer": ["solidity", "ethereum", "smart contracts", "web3.js", "decentralized applications", "nfts"],
    # "Data Engineer": ["etl", "spark", "hadoop", "big data", "airflow", "sql", "data pipelines"],
    # "AI Engineer": ["neural networks", "deep learning", "tensorflow", "pytorch", "nlp", "computer vision", "model optimization"],
    # "UI/UX Designer": ["figma", "adobe xd", "wireframes", "prototyping", "user research", "usability testing"],
    # "QA Engineer": ["manual testing", "automation testing", "selenium", "jmeter", "cypress", "test cases", "bug tracking"],
    # "Product Manager": ["roadmap", "stakeholder management", "agile", "scrum", "user stories", "analytics", "market research"],
    # "Business Analyst": ["requirements gathering", "sql", "data analysis", "stakeholder communication", "process improvement", "documentation"],
    # "Embedded Systems Engineer": ["c", "c++", "microcontrollers", "rtos", "fpga", "hardware interfacing"],
    # "Game Developer": ["unity", "unreal engine", "c#", "game physics", "3d modeling", "animation", "ai in games"],
# }

# with st.container():
#     col1, col2, col3 = st.columns([1, 2, 1])
#     with col2:
#         role = st.selectbox("🎯 Select Target Role", options=list(role_keywords.keys()), index=0)

# if uploaded_file and role:
#     col1, col2, col3 = st.columns([1, 2, 1])
#     with col2:
#         if st.button("🚀 Analyze Resume", use_container_width=True):
#             with st.spinner("Analyzing your resume..."):
#                 text = pdf_extractor.extract_text_from_pdf(uploaded_file)
#                 matched, missing, score = nlp_utils.match_keywords(text, role_keywords[role])

#                 st.markdown(f"""
#                 <div class="section">
#                     <h4>✅ Analysis Complete</h4>
#                     <p>Your resume matches <b>{score}%</b> of the required skills for <b>{role}</b>.</p>
#                 """, unsafe_allow_html=True)

#                 st.progress(score)

#                 st.markdown("""
#                     <div style="margin-top:20px;">
#                         <h5>🎯 Matched Keywords</h5>
#                         <div class="keywords">
#                 """, unsafe_allow_html=True)

#                 if matched:
#                     st.markdown("".join([f'<span class="keyword">{kw}</span>' for kw in matched]), unsafe_allow_html=True)
#                 else:
#                     st.markdown("*No matches found.*")

#                 st.markdown("""
#                         </div>
#                         <h5 style="margin-top:20px;">🔍 Missing Keywords</h5>
#                         <div class="keywords">
#                 """, unsafe_allow_html=True)

#                 if missing:
#                     st.markdown("".join([f'<span class="keyword missing">{kw}</span>' for kw in missing]), unsafe_allow_html=True)
#                 else:
#                     st.markdown("🎉 *None!*")

#                 st.markdown("</div></div>", unsafe_allow_html=True)

#                 save_dir = "saved_data/feedback_logs"
#                 os.makedirs(save_dir, exist_ok=True)
#                 timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
#                 save_path = os.path.join(save_dir, f"{role}_{timestamp}.txt")

#                 with open(save_path, "w") as f:
#                     f.write(f"Role: {role}\nMatch Score: {score}%\n")
#                     f.write(f"Matched: {', '.join(matched)}\n")
#                     f.write(f"Missing: {', '.join(missing)}\n")

#                 st.info(f"📁 Report saved to `{save_path}`")
# else:
#     st.info("⬆️ Please upload your resume and select a role to start analysis.")


import streamlit as st
from utils import pdf_extractor, nlp_utils
import os
import datetime
from streamlit_extras.colored_header import colored_header
from streamlit_extras.badges import badge

# Config
st.set_page_config(page_title="📄 Resume Analyzer", page_icon="📄", layout="wide")

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2920/2920349.png", width=100)
    st.title("Resume Analyzer")
    st.markdown("🚀 Unlock your career potential by aligning your resume with your dream role!")
    st.markdown("---")
    # Fix: use a supported badge type or replace with markdown
    st.markdown("Made with ❤️ by Gauri")

colored_header("📄 Resume Analyzer Dashboard", description="Analyze your resume against your target job role and get actionable insights.", color_name="blue-70")

with st.container():
    st.markdown("""
        <style>
        .highlight-card {
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .score-badge {
            font-size: 24px;
            color: white;
            background-color: #4caf50;
            padding: 5px 15px;
            border-radius: 50px;
        }
        </style>
        """, unsafe_allow_html=True)

# Target roles with example keywords
role_keywords = {   
        "Data Scientist": ["python", "machine learning", "statistics", "pandas", "tensorflow", "scikit-learn", "deep learning"],
    "Machine Learning Engineer": ["python", "tensorflow", "pytorch", "mlops", "model deployment", "feature engineering"],
    "Software Engineer": ["java", "c++", "design patterns", "algorithms", "data structures", "git", "oop"],
    "Frontend Developer": ["html", "css", "javascript", "react", "vue", "angular", "responsive design", "webpack"],
    "Backend Developer": ["node.js", "django", "flask", "sql", "nosql", "api development", "microservices"],
    "Full Stack Developer": ["html", "css", "javascript", "react", "node.js", "api", "sql", "devops"],
    "DevOps Engineer": ["ci/cd", "docker", "kubernetes", "aws", "terraform", "jenkins", "ansible", "monitoring"],
    "Cloud Engineer": ["aws", "azure", "gcp", "cloud architecture", "serverless", "cloudformation", "iac"],
    "Flutter Developer": ["dart", "flutter", "state management", "bloc", "provider", "ui/ux", "firebase"],
    "Mobile App Developer": ["swift", "kotlin", "flutter", "react native", "android studio", "xcode", "ui/ux"],
    "Cybersecurity Analyst": ["penetration testing", "network security", "vulnerability assessment", "firewalls", "siem", "encryption", "incident response"],
    "Blockchain Developer": ["solidity", "ethereum", "smart contracts", "web3.js", "decentralized applications", "nfts"],
    "Data Engineer": ["etl", "spark", "hadoop", "big data", "airflow", "sql", "data pipelines"],
    "AI Engineer": ["neural networks", "deep learning", "tensorflow", "pytorch", "nlp", "computer vision", "model optimization"],
    "UI/UX Designer": ["figma", "adobe xd", "wireframes", "prototyping", "user research", "usability testing"],
    "QA Engineer": ["manual testing", "automation testing", "selenium", "jmeter", "cypress", "test cases", "bug tracking"],
    "Product Manager": ["roadmap", "stakeholder management", "agile", "scrum", "user stories", "analytics", "market research"],
    "Business Analyst": ["requirements gathering", "sql", "data analysis", "stakeholder communication", "process improvement", "documentation"],
    "Embedded Systems Engineer": ["c", "c++", "microcontrollers", "rtos", "fpga", "hardware interfacing"],
    "Game Developer": ["unity", "unreal engine", "c#", "game physics", "3d modeling", "animation", "ai in games"],
}

uploaded_file = st.file_uploader("📤 Upload your Resume (PDF only)", type=["pdf"])
role = st.selectbox("🎯 Choose Your Target Role", options=list(role_keywords.keys()))

if uploaded_file and role:
    if st.button("🔍 Analyze Resume", use_container_width=True):
        with st.spinner("⏳ Analyzing your resume... Please wait."):

            text = pdf_extractor.extract_text_from_pdf(uploaded_file)
            matched, missing, score = nlp_utils.match_keywords(text, role_keywords[role])

            st.markdown(f"""
                <div class='highlight-card'>
                    <h3>✅ Analysis Complete!</h3>
                    <p>Your resume matches <span class='score-badge'>{score}%</span> for the role: <strong>{role}</strong></p>
                </div>
            """, unsafe_allow_html=True)

            st.markdown("---")

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### 🎯 <span style='color:#4caf50;'>Matched Keywords</span>", unsafe_allow_html=True)
                st.success(", ".join(matched) if matched else "No matches found.")
            with col2:
                st.markdown("### 🔍 <span style='color:#f44336;'>Missing Keywords</span>", unsafe_allow_html=True)
                st.error(", ".join(missing) if missing else "None 🎉")

            save_dir = "saved_data/feedback_logs"
            os.makedirs(save_dir, exist_ok=True)
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            save_path = os.path.join(save_dir, f"{role}_{timestamp}.txt")

            with open(save_path, "w") as f:
                f.write(f"Role: {role}\nMatch Score: {score}%\n")
                f.write(f"Matched: {', '.join(matched)}\n")
                f.write(f"Missing: {', '.join(missing)}\n")

            st.info(f"📁 Report saved to `{save_path}`")
else:
    st.info("⬆️ Please upload your resume and select a role to start analysis.")
