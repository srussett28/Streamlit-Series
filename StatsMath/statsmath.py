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
    image_path_ed = "StatsMath/mathdugit .png"  
    st.image(image_path_ed, use_container_width=True)

    tabs = st.tabs(["Descriptive", "Prescriptive", "Predictive", "Diagnostic", "Other"])

    if selected_role == "Data Analyst":
        with tabs[0]:
            st.header("Descriptive Statistics for Data Analysts")
            image_path_an = "StatsMath/analystdu .png"  
            st.image(image_path_an, use_container_width=True)
            st.markdown("## Mean, Median, Mode")
            st.markdown("**Concept:**")
            st.write("- **Mean:** The average value of a dataset, calculated by summing all values and dividing by the total count.")
            st.write("- **Median:** The middle value when a dataset is ordered; splits the dataset into two equal halves.")
            st.write("- **Mode:** The most frequently occurring value(s) in a dataset.")

            st.markdown("**Calculations:**")
            st.write("- **Mean Formula:** \( \\text{Mean} = \\frac{\\sum x_i}{n} \), where \( x_i \) are data points and \( n \) is the total count.")
            st.write("- **Median:** Order the dataset and pick the middle value (or average of two middle values if even).")
            st.write("- **Mode:** Identify the value(s) with the highest frequency.")

            st.markdown("**When to Use:**")
            st.write("- Use **Mean** for datasets without significant outliers.")
            st.write("- Use **Median** when there are extreme outliers or skewed data.")
            st.write("- Use **Mode** for categorical or discrete data to identify the most common category/value.")

            st.markdown("**When Not to Use:**")
            st.write("- Avoid **Mean** if the dataset contains extreme outliers that distort the average.")
            st.write("- **Mode** may not be informative for continuous datasets with unique values.")

            st.markdown("**Additional Information:**")
            st.write("- Mean and Median are measures of central tendency, but they respond differently to skewness and outliers.")
            st.write("- Median is preferred for ordinal data or when analyzing income, house prices, etc.")

            

            # Range, Variance, Standard Deviation
            st.markdown("## Range, Variance, Standard Deviation")
            st.markdown("**Concept:**")
            st.write("- **Range:** The difference between the maximum and minimum values in a dataset.")
            st.write("- **Variance:** A measure of how far data points are spread out from the mean, quantifying variability.")
            st.write("- **Standard Deviation:** The square root of variance; provides variability in the same unit as the data.")

            st.markdown("**Calculations:**")
            st.write("- **Range Formula:** \( \\text{Range} = \\text{Max Value} - \\text{Min Value} \)")
            st.write("- **Variance Formula:** \( \\text{Variance} = \\frac{\\sum (x_i - \\mu)^2}{n} \), where \( \\mu \) is the mean.")
            st.write("- **Standard Deviation Formula:** \( \\sigma = \\sqrt{\\text{Variance}} \)")

            st.markdown("**When to Use:**")
            st.write("- Use **Range** for quick variability checks in small datasets.")
            st.write("- Use **Variance** and **Standard Deviation** for larger datasets to understand variability more precisely.")

            st.markdown("**When Not to Use:**")
            st.write("- **Range** is not ideal for large datasets as it only considers extreme values.")
            st.write("- Avoid using **Standard Deviation** without context; large or small values depend on the dataset scale.")

            st.markdown("**Additional Information:**")
            st.write("- Variance and Standard Deviation are commonly used for quantitative datasets.")
            st.write("- Standard Deviation is preferred in inferential statistics and hypothesis testing.")

            ---

            # IQR: Quartile, Percentile, Box Plot
            st.markdown("## IQR, Quartiles, Percentiles, and Box Plots")
            st.markdown("**Concept:**")
            st.write("- **Quartiles:** Divide a dataset into four equal parts (Q1, Q2/Median, Q3).")
            st.write("- **Percentile:** Indicates the value below which a given percentage of observations fall.")
            st.write("- **IQR (Interquartile Range):** Measures the spread between Q1 and Q3, capturing the middle 50% of the data.")
            st.write("- **Box Plot:** A graphical representation showing the distribution of a dataset using quartiles and outliers.")

            st.markdown("**Calculations:**")
            st.write("- **IQR Formula:** \( \\text{IQR} = Q3 - Q1 \)")
            st.write("- **Percentile Formula:** Identify the \( P \)-th value by sorting data and finding the rank: \( R = \\frac{P}{100} \\times (n + 1) \).")
            st.write("- **Box Plot Elements:** Drawn using Q1, Median (Q2), Q3, and outliers detected using 1.5 × IQR rule.")

            st.markdown("**When to Use:**")
            st.write("- Use **IQR** to identify outliers and describe data spread resistant to extreme values.")
            st.write("- Use **Percentiles** for comparisons, such as test scores or benchmarks.")
            st.write("- Use **Box Plots** to visualize distribution and spot outliers.")

            st.markdown("**When Not to Use:**")
            st.write("- Avoid relying solely on **IQR** if the dataset has multiple peaks or complex distributions.")
            st.write("- Percentiles may not be meaningful for categorical data.")

            st.markdown("**Additional Information:**")
            st.write("- Box Plots are especially useful for comparing multiple datasets side by side.")
            st.write("- IQR is robust against skewed data, unlike variance or standard deviation.")

            ---

            # Correlation and Covariance
            st.markdown("## Correlation and Covariance")
            st.markdown("**Concept:**")
            st.write("- **Correlation:** Measures the strength and direction of a linear relationship between two variables.")
            st.write("- **Covariance:** Measures how two variables vary together, but without standardizing the scale.")

            st.markdown("**Calculations:**")
            st.write("- **Correlation Formula:** \( \\text{Correlation} (r) = \\frac{\\text{Covariance}(X, Y)}{\\sigma_X \\sigma_Y} \)")
            st.write("- **Covariance Formula:** \( \\text{Cov}(X, Y) = \\frac{\\sum (X_i - \\bar{X})(Y_i - \\bar{Y})}{n} \)")

            st.markdown("**When to Use:**")
            st.write("- Use **Correlation** for understanding relationships between variables (e.g., height and weight).")
            st.write("- Use **Covariance** to measure directional relationships but not strength.")

            st.markdown("**When Not to Use:**")
            st.write("- Avoid interpreting **Covariance** as strength; its value is scale-dependent.")
            st.write("- Avoid using **Correlation** for non-linear relationships or heavily skewed data.")

            st.markdown("**Additional Information:**")
            st.write("- Correlation ranges from -1 (perfect negative) to 1 (perfect positive).")
            st.write("- Covariance is harder to interpret directly but forms the basis of correlation.")
        
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

