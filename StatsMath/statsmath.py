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

 # Main Content
    st.title(f"{selected_role}: Statistics and Math")

    tabs = st.tabs(["Descriptive", "Prescriptive", "Predictive", "Diagnostic", "Other"])

    if selected_role == "Data Analyst":
        with tabs[0]:
            st.header("Descriptive Statistics for Data Analysts")
            st.markdown("- Mean, Median, Mode, Range, Variance, Standard Deviation")
            st.markdown("- IQR: Quartile, Percentile, Box Plot")
            st.markdown("- Correlation and Covariance")
        with tabs[1]:
            st.header("Prescriptive Statistics for Data Analysts")
            st.markdown("- A/B Testing")
            st.markdown("- Sampling Techniques: Probability and Non-Probability Sampling")
        with tabs[2]:
            st.header("Predictive Statistics for Data Analysts")
            st.markdown("- Empirical and Theoretical Probability")
            st.markdown("- Trend Analysis")
        with tabs[3]:
            st.header("Diagnostic Statistics for Data Analysts")
            st.markdown("- Set Theory: Union, Intersection, Complement")
            st.markdown("- Skewness and Kurtosis")
        with tabs[4]:
            st.header("Other Topics for Data Analysts")
            st.markdown("- Feature Engineering:")
            st.markdown("  - Box-Cox Transformation")
            st.markdown("  - Z-Score and Scaling")
            st.markdown("- Model Validation:")
            st.markdown("  - Confidence and Prediction Intervals")
            st.markdown("- Automation and Deployment:")
            st.markdown("  - Automating Workflows and Pipelines")

    elif selected_role == "Data Scientist":
        with tabs[0]:
            st.header("Descriptive Statistics for Data Scientists")
            st.markdown("- Descriptive Measures of Central Tendency and Spread")
            st.markdown("- Visualizations: Histograms, QQ Plots")
        with tabs[1]:
            st.header("Prescriptive Statistics for Data Scientists")
            st.markdown("- Hypothesis Testing: P-Values, Confidence Intervals, Tailed Tests")
            st.markdown("- Statistical Power and Significance Testing")
        with tabs[2]:
            st.header("Predictive Statistics for Data Scientists")
            st.markdown("- Probability and Statistical Distributions:")
            st.markdown("  - Normal, Binomial, Poisson, Exponential, Geometric Distributions")
            st.markdown("  - Central Limit Theorem")
        with tabs[3]:
            st.header("Diagnostic Statistics for Data Scientists")
            st.markdown("- Bayesian Analysis")
            st.markdown("- Conditional Probability, Law of Total Probability")
        with tabs[4]:
            st.header("Other Topics for Data Scientists")
            st.markdown("- Feature Engineering:")
            st.markdown("  - Box-Cox Transformation")
            st.markdown("  - Z-Score and Scaling")
            st.markdown("- Model Validation:")
            st.markdown("  - Statistical Power and Influencing Factors")
            st.markdown("  - Confidence and Prediction Intervals")
            st.markdown("  - A/B Testing and Optimization Techniques")
            st.markdown("- Automation and Deployment:")
            st.markdown("  - Leveraging Statistical Insights for Model Improvements")

    elif selected_role == "Data Engineer":
        with tabs[0]:
            st.header("Descriptive Statistics for Data Engineers")
            st.markdown("- Data Sampling and Integrity")
            st.markdown("- Aggregation Techniques")
        with tabs[1]:
            st.header("Prescriptive Statistics for Data Engineers")
            st.markdown("- Workflow Automation")
            st.markdown("- Setting ETL Pipelines for Statistical Data")
        with tabs[2]:
            st.header("Predictive Statistics for Data Engineers")
            st.markdown("- Probability Modeling for Data Pipelines")
            st.markdown("- Trend Forecasting Techniques")
        with tabs[3]:
            st.header("Diagnostic Statistics for Data Engineers")
            st.markdown("- Ensuring Data Quality with Statistical Metrics")
            st.markdown("- Data Validation Techniques")
        with tabs[4]:
            st.header("Other Topics for Data Engineers")
            st.markdown("- Probability and Statistical Distributions:")
            st.markdown("  - Normal, Binomial, Poisson, Exponential, Geometric Distributions")
            st.markdown("  - Central Limit Theorem")
            st.markdown("- Automation and Deployment:")
            st.markdown("  - Automating Workflows and Pipelines")

    elif selected_role == "Analytics/ML Engineer":
        with tabs[0]:
            st.header("Descriptive Statistics for Analytics/ML Engineers")
            st.markdown("- Feature Scaling and Transformation (Z-Score, Box-Cox)")
            st.markdown("- Analyzing Model Inputs")
        with tabs[1]:
            st.header("Prescriptive Statistics for Analytics/ML Engineers")
            st.markdown("- A/B Testing for Model Validation")
            st.markdown("- Optimization Techniques for Model Tuning")
        with tabs[2]:
            st.header("Predictive Statistics for Analytics/ML Engineers")
            st.markdown("- Predictive Models: Regression, Classification")
            st.markdown("- Confidence and Prediction Intervals")
        with tabs[3]:
            st.header("Diagnostic Statistics for Analytics/ML Engineers")
            st.markdown("- Model Diagnostics and Error Analysis")
            st.markdown("- Statistical Power and Validation")
        with tabs[4]:
            st.header("Other Topics for Analytics/ML Engineers")
            st.markdown("- Probability and Statistical Distributions:")
            st.markdown("  - Normal, Binomial, Poisson, Exponential, Geometric Distributions")
            st.markdown("  - Central Limit Theorem")
            st.markdown("- Feature Engineering:")
            st.markdown("  - Box-Cox Transformation")
            st.markdown("  - Z-Score and Scaling")
            st.markdown("- Model Validation:")
            st.markdown("  - Statistical Power and Influencing Factors")
            st.markdown("- Automation and Deployment:")
            st.markdown("  - Leveraging Statistical Insights for Model Improvements")

if __name__ == "__main__":
    main()

