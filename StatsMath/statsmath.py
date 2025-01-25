import streamlit as st
from streamlit_option_menu import option_menu

def main():
    st.set_page_config(page_title="Statistics and Math for Roles", layout="wide")

    # Sidebar Navigation for Roles
    with st.sidebar:
        selected_role = option_menu(
            "Select Role",
            ["Data Analyst", "Data Scientist", "Data Engineer", "Analytics/ML Engineer"],
            icons=["clipboard-data", "graph-up", "server", "robot"],
            menu_icon="cast",
            default_index=0
        )

    # Main Content
    st.title(f"{selected_role}: Statistics and Math")

    if selected_role == "Data Analyst":
        st.header("Welcome, Data Analyst!")
        st.write("As a Data Analyst, you focus on descriptive and diagnostic statistics.")
        st.markdown("### Key Topics:")
        st.markdown("- Descriptive Statistics (Mean, Median, Mode, etc.)")
        st.markdown("- Sampling Techniques")
        st.markdown("- Data Visualization Techniques (Box plots, Histograms)")

    elif selected_role == "Data Scientist":
        st.header("Welcome, Data Scientist!")
        st.write("As a Data Scientist, you work extensively with predictive and inferential statistics.")
        st.markdown("### Key Topics:")
        st.markdown("- Probability Distributions (Normal, Binomial, Poisson)")
        st.markdown("- Hypothesis Testing")
        st.markdown("- Machine Learning Basics")

    elif selected_role == "Data Engineer":
        st.header("Welcome, Data Engineer!")
        st.write("As a Data Engineer, your focus is on the data pipeline and ensuring data quality.")
        st.markdown("### Key Topics:")
        st.markdown("- Data Cleaning and Transformation")
        st.markdown("- Sampling Techniques and Data Integrity")
        st.markdown("- Data Storage and Retrieval Systems")

    elif selected_role == "Analytics/ML Engineer":
        st.header("Welcome, Analytics/ML Engineer!")
        st.write("As an Analytics/ML Engineer, you work on deploying and optimizing models.")
        st.markdown("### Key Topics:")
        st.markdown("- Statistical Power and Model Validation")
        st.markdown("- Confidence Intervals and Prediction Intervals")
        st.markdown("- A/B Testing and Optimization Techniques")

if __name__ == "__main__":
    main()
