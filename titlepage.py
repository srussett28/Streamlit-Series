import streamlit as st

st.title("Exploring the Data Universe: A Curious Weirdo’s Guide to Becoming a Data Swiss Army Knife")
image_path = "CuriousGuide.png"
st.image(image_path,  use_container_width=True)

st.subheader("By Someone Who’s Been There, (Sloan Russett)")
image_SBR = "SBR.jpg"
st.image(image_SBR,  use_container_width=True)

st.markdown("## The Lightbulb Moment")
st.write("""
I call myself a "data weirdo" because my journey into data has been anything but traditional. It all started with Excel, where I dived deep into VBA and macros to automate tasks and solve complex problems. But instead of graduating directly to SQL, I took a Business Analytics course at USC that introduced me to R. My early days in R were focused on regression analysis and building predictive models that provided actionable insights for users.
However, I didn’t start by learning the foundational structures of data or the x’s and o’s. I was thrown straight into the deep end, tackling applied problems from the start. Just as I was getting comfortable with R, I pivoted to Python—a shift that significantly expanded my toolkit and marked the start of my career as a consultant and solutions specialist.
In consulting, I wasn’t just coding or analyzing data—I was designing end-to-end solutions. My role demanded that I be a data engineer, architect, and data scientist all at once. Clients wanted to understand the algorithms, how their users would interact with them, and how these solutions would integrate into existing systems to drive optimization.
This unconventional learning path and multifaceted role shaped me into a versatile professional with a unique perspective on data. It’s why I don’t fit neatly into any one category and why this series reflects that bringing together insights from data analytics, data science, and engineering for anyone who feels like they don’t belong in just one box either.
""")


st.markdown("## What It Is")
st.write("""
This series is a guided tour through the key skills and concepts that make up the data universe. 
Each part focuses on a major area of data work. Mostly dealing with SQL, Python, cleaning, modeling, machine learning, and more—with explanations, examples, 
and practical applications. Think of it as a roadmap to becoming a versatile, data-savvy professional.
""")


st.subheader("Who It’s For")
image_You = "You.png"
st.image(image_You,  use_container_width=True)
st.write("""
This series is for:
- **Beginners** looking to break into the data field.
- **Professionals** who want to broaden their skill set across roles.
- **General enthusiasts** curious about what data professionals actually do.
Whether you’re a data analyst, scientist, or engineer—or a mix of all three—this series has something for you.
""")


st.title("Table of Contents")

toc = {
    "1. The Basics: Tools, prior knowledge, key terminology etc.": 
        "Introductory materials to get started. Link - [https://srussett28-streamlit-series-prereq2-nyxkg6.streamlit.app/](https://srussett28-streamlit-series-prereq2-nyxkg6.streamlit.app/)",
    "2. Everybody's favorite STATISTICCCCSSSSS": 
        "Understand the fundamentals of statistics for data analysis. Link - Under Construction",
    "3. SQL Commands for Data Professionals": 
        "Learn essential SQL commands for analysts, engineers, and scientists. Link - [https://srussett28-streamlit-series-streamlittest4-itgznn.streamlit.app/](https://srussett28-streamlit-series-streamlittest4-itgznn.streamlit.app/)",
    "4. Pertinent Python Libraries": 
        "Explore must-know Python libraries tailored to different data roles. Link - [https://srussett28-streamli-python-libraries-pt3pythonlibraries1-ysi6yx.streamlit.app/](https://srussett28-streamli-python-libraries-pt3pythonlibraries1-ysi6yx.streamlit.app/)",
    "5. Data Pipelines and Workflow Automate": 
        "Automate and orchestrate complex data workflows. Link - Under Construction",
    "6. Data Cleaning Techniques": 
        "Master the art of wrangling messy data into shape. Link - Under Construction",
    "7. Data Modeling": 
        "Dive into building statistical and machine learning models. Link - Under Construction",
    "8. Cloud Data Platforms": 
        "Leverage AWS, Azure, and GCP for scalable data solutions. Link - Under Construction",
    "9. Experimentation and A/B Testing": 
        "Learn to run and interpret experiments effectively. Link - Under Construction",
    "10. AI and Machine Learning": 
        "Discover the basics of AI/ML and their practical applications. Link - Under Construction",
    "11. Data Visualizations": 
        "Create stunning visualizations to tell compelling stories. Link - Under Construction",
    "12. Ethics, Governance, and Trust in Data": 
        "Understand the importance of responsible and ethical data use. Link - Under Construction"
}


# Render the TOC
for title, description in toc.items():
    st.markdown(f"### {title}\n{description}")







