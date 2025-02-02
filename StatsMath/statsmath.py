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
    image_path_ed = "mathdu.png"  
    st.image(image_path_ed, use_container_width=True)

    tabs = st.tabs(["Descriptive", "Prescriptive", "Predictive", "Diagnostic", "Other"])

    if selected_role == "Data Analyst":
        with tabs[0]:
            st.header("Descriptive Statistics for Data Analysts")
            st.markdown("## Mean, Median, Mode")
            st.markdown("**Concept:**")
            st.write("- **Mean:** The average value of a dataset, calculated by summing all values and dividing by the total count.")
            st.write("- **Median:** The middle value when a dataset is ordered; splits the dataset into two equal halves.")
            st.write("- **Mode:** The most frequently occurring value(s) in a dataset.")

            st.markdown("**Calculations:**")
            st.latex(r"\text{Mean} = \frac{\sum_{i=1}^{n} x_i}{n}")
            st.latex(r"\text{Median} = \text{Middle value of sorted data}")
            st.latex(r"\text{Mode} = \text{Most frequently occurring value(s)}")

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
            st.latex(r"\text{Range} = \text{Max Value} - \text{Min Value}")
            st.latex(r"\text{Variance} = \frac{\sum_{i=1}^{n} (x_i - \mu)^2}{n}")
            st.latex(r"\sigma = \sqrt{\text{Variance}}")
            
            st.markdown("**When to Use:**")
            st.write("- Use **Range** for quick variability checks in small datasets.")
            st.write("- Use **Variance** and **Standard Deviation** for larger datasets to understand variability more precisely.")

            st.markdown("**When Not to Use:**")
            st.write("- **Range** is not ideal for large datasets as it only considers extreme values.")
            st.write("- Avoid using **Standard Deviation** without context; large or small values depend on the dataset scale.")

            st.markdown("**Additional Information:**")
            st.write("- Variance and Standard Deviation are commonly used for quantitative datasets.")
            st.write("- Standard Deviation is preferred in inferential statistics and hypothesis testing.")

        

            # IQR: Quartile, Percentile, Box Plot
            st.markdown("## IQR, Quartiles, Percentiles, and Box Plots")
            st.markdown("**Concept:**")
            st.write("- **Quartiles:** Divide a dataset into four equal parts (Q1, Q2/Median, Q3).")
            st.write("- **Percentile:** Indicates the value below which a given percentage of observations fall.")
            st.write("- **IQR (Interquartile Range):** Measures the spread between Q1 and Q3, capturing the middle 50% of the data.")
            st.write("- **Box Plot:** A graphical representation showing the distribution of a dataset using quartiles and outliers.")

            st.markdown("**Calculations:**")
            st.latex(r"\text{IQR} = Q3 - Q1")
            st.latex(r"R = \frac{P}{100} \times (n + 1)")

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

            # Correlation and Covariance
            st.markdown("## Correlation and Covariance")
            st.markdown("**Concept:**")
            st.write("- **Correlation:** Measures the strength and direction of a linear relationship between two variables.")
            st.write("- **Covariance:** Measures how two variables vary together, but without standardizing the scale.")

            st.markdown("**Calculations:**")
            st.latex(r"r = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}")
            st.latex(r"\text{Cov}(X, Y) = \frac{\sum_{i=1}^{n} (X_i - \bar{X})(Y_i - \bar{Y})}{n}")

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
            st.markdown("**Concept**")
            st.write(
    "A/B Testing is a randomized controlled experiment used to compare two versions (A and B) of a variable "
    "to determine which performs better. It is commonly used in marketing, UX design, and product optimization."
)

            st.markdown("**Calculations**")
            st.latex(r"\text{Conversion Rate} = \frac{\text{Conversions}}{\text{Total Visitors}} \times 100")
            st.latex(r"\text{Lift} = \frac{\text{Conversion Rate of B} - \text{Conversion Rate of A}}{\text{Conversion Rate of A}}")


            st.markdown("**When to Use**")
            st.write(
    "- When testing changes to websites, ads, or products before full rollout."
    "\n- When optimizing conversion rates or engagement."
    "\n- When a controlled experiment is possible."
)

            st.markdown("**When Not to Use**")
            st.write(
    "- When sample sizes are too small to achieve statistical power."
    "\n- When external factors (e.g., seasonality, market shifts) could skew results."
    "\n- When testing multiple variables at once (consider multivariate testing instead)."
)

            st.markdown("**Additional Info**")
            st.write(
    "- Common statistical tests: **Chi-Square Test**, **T-Test**, **Z-Test**."
    "\n- Requires **random assignment** of users into groups to reduce bias."
    "\n- The **False Discovery Rate (FDR)** should be controlled to avoid misleading conclusions."
)

# Sampling Techniques Section
            st.header("🎲 Sampling Techniques: Probability and Non-Probability Sampling")
            st.markdown("**Concept**")
            st.write(
    "Sampling is the process of selecting a subset of data from a larger population to make inferences about the whole."
    "\n- **Probability Sampling**: Every member of the population has a known, nonzero chance of being selected."
    "\n- **Non-Probability Sampling**: Selection is based on convenience or judgment rather than randomization."
)

            st.markdown("**Calculations**")
            st.latex(r"\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}")
            st.latex(r"s = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1}}")
            st.latex(r"\text{Margin of Error} = Z \times \frac{\sigma}{\sqrt{n}}")


            st.markdown("**When to Use**")
            st.write(
    "**Probability Sampling** (e.g., Simple Random, Stratified, Cluster, Systematic)"
    "\n- When unbiased representation is required."
    "\n- When statistical inference is needed."
    "\n\n**Non-Probability Sampling** (e.g., Convenience, Judgmental, Snowball, Quota)"
    "\n- When random selection is impractical or expensive."
    "\n- When exploratory research is conducted."
)

            st.markdown("**When Not to Use**")
            st.write(
    "**Probability Sampling**"
    "\n- When cost or time constraints make it infeasible."
    "\n- When the population list is unavailable."
    "\n\n**Non-Probability Sampling**"
    "\n- When results need to be generalizable to the whole population."
    "\n- When avoiding bias is critical."
)

            st.markdown("**Additional Info**")
            st.write(
    "- **Law of Large Numbers**: Larger samples tend to produce more accurate estimates."
    "\n- **Central Limit Theorem (CLT)**: The distribution of sample means approaches normality as the sample size increases."
    "\n- Sample size should be calculated using **power analysis** for sufficient reliability."
)
        with tabs[2]:
            st.header("Predictive Statistics for Data Analysts")
            st.subheader("Empirical and Theoretical Probability")
            st.write("Probability helps in predicting the likelihood of different outcomes in uncertain situations. There are two main types:")
            st.write("1. **Empirical Probability**: This is based on actual experiments or observations. It calculates the probability of an event occurring by looking at past data.")
            st.write("2. **Theoretical Probability**: This is based on expected outcomes under ideal conditions, assuming all outcomes are equally likely.")
            
            st.write("### Formulae")
            st.latex(r"P(E) = \frac{\text{Number of times E occurs}}{\text{Total trials}}")
            st.latex(r"P(E) = \frac{\text{Favorable outcomes}}{\text{Total possible outcomes}}")
            
            st.write("### When to Use")
            st.write("- Use empirical probability when working with real-world data, like customer purchase history or sports statistics.")
            st.write("- Use theoretical probability for controlled experiments, such as determining the odds of rolling a specific number on a fair die.")
            
            st.write("### Limitations")
            st.write("- Empirical probability is only as accurate as the amount of data collected; small datasets can lead to misleading results.")
            st.write("- Theoretical probability assumes ideal conditions, which may not reflect real-world randomness.")
            
            st.subheader("Trend Analysis")
            st.write("Trend analysis is used to identify patterns in data over time, helping to make informed business and economic decisions.")
            st.write("Common methods include:")
            st.write("- **Moving Averages**: Helps smooth fluctuations and identify long-term trends.")
            st.latex(r"SMA_t = \frac{X_{t} + X_{t-1} + ... + X_{t-n+1}}{n}")
            st.write("- **Linear Regression**: Identifies trends by fitting a straight line through data points.")
            
            st.write("### When to Use")
            st.write("- Use moving averages to detect trends in financial markets or sales forecasting.")
            st.write("- Use regression analysis to make predictions about future performance based on historical data.")
            
            st.write("### Limitations")
            st.write("- Trends do not always continue; unexpected events can disrupt patterns.")
            st.write("- Over-reliance on past data assumes that future conditions will remain similar.")
        
        with tabs[3]:
            st.header("Diagnostic Statistics for Data Analysts")
            st.subheader("Set Theory: Union, Intersection, Complement")
            st.write("Set theory is a fundamental concept in probability and data analysis. It defines how groups of items relate to each other.")
            st.write("- **Union (A ∪ B)**: Contains all elements from both sets A and B.")
            st.write("- **Intersection (A ∩ B)**: Contains only the elements common to both sets A and B.")
            st.write("- **Complement (A')**: Contains all elements that are in the universal set but not in A.")
            
            st.write("### Formula")
            st.latex(r"P(A \cup B) = P(A) + P(B) - P(A \cap B)")
            st.latex(r"P(A \cap B) = P(A) \cdot P(B)")
            
            st.write("### Applications")
            st.write("- Used in database queries, search engines, and probability calculations.")
            st.write("- Helps in understanding logical relationships between datasets.")
            
            st.subheader("Skewness and Kurtosis")
            st.write("These two concepts measure the shape of a dataset's distribution.")
            st.write("- **Skewness** tells whether data is symmetrically distributed or shifted to one side.")
            st.write("- **Kurtosis** measures whether data has extreme outliers and how concentrated values are around the mean.")
            
            st.write("### Formula")
            st.latex(r"g_1 = \frac{\sum (x - \bar{x})^3}{n \cdot s^3}")
            st.latex(r"g_2 = \frac{\sum (x - \bar{x})^4}{n \cdot s^4}")
            
            st.write("### Applications")
            st.write("- Skewness helps in detecting bias in data distributions.")
            st.write("- Kurtosis helps in determining whether a dataset has heavy tails and outliers.")
        
        with tabs[4]:
            st.header("Other Topics for Data Analysts")
            st.subheader("Feature Engineering")
            st.write("Feature engineering involves modifying raw data to improve model performance.")
            
            st.subheader("Box-Cox Transformation")
            st.write("The Box-Cox transformation is a statistical technique used to stabilize variance and make data more normally distributed.")
            st.write("This is particularly useful when dealing with skewed data, as many statistical models assume normality.")
            st.write("The transformation is defined as:")
            st.latex(r"Y_{new} = \frac{Y^{\lambda} - 1}{\lambda} \text{ for } \lambda \neq 0")
            st.write("Where:")
            st.write("- \( Y_{new} \) is the transformed data.")
            st.write("- \( Y \) is the original data.")
            st.write("- \( \lambda \) is the transformation parameter.")
            st.write("- When \( \lambda = 0 \), a logarithmic transformation is applied.")
            
            st.write("### When to Use:")
            st.write("- When data is highly skewed and violates normality assumptions.")
            st.write("- When variance increases with the mean, making traditional models ineffective.")
            
            st.write("### Limitations:")
            st.write("- The choice of \( \lambda \) is crucial and often determined using maximum likelihood estimation.")
            st.write("- The transformation is only applicable to positive data.")
            
            st.subheader("Z-Score and Scaling")
            st.write("Z-score normalization (also called standardization) is used to scale data so that it has a mean of 0 and a standard deviation of 1.")
            st.write("This makes it easier to compare variables measured on different scales.")
            st.write("The formula is:")
            st.latex(r"Z = \frac{X - \mu}{\sigma}")
            st.write("Where:")
            st.write("- \( X \) is the original value.")
            st.write("- \( \mu \) is the mean of the dataset.")
            st.write("- \( \sigma \) is the standard deviation of the dataset.")
            
            st.write("### When to Use:")
            st.write("- When variables in a dataset have different units and need to be compared.")
            st.write("- Before applying machine learning models that rely on distance calculations (e.g., k-means clustering, k-nearest neighbors).")
            
            st.write("### Limitations:")
            st.write("- Z-score scaling assumes a normal distribution, which may not be the case for all datasets.")
            st.write("- Can be sensitive to outliers, as they can greatly affect the mean and standard deviation.")
            
            st.subheader("Model Validation")
            st.write("Model validation is essential to ensure that a statistical or machine learning model is reliable and generalizes well to new data.")
            
            st.subheader("Confidence Intervals")
            st.write("A confidence interval provides a range of values within which we expect a population parameter (such as the mean) to lie with a certain level of confidence.")
            st.write("The formula for a confidence interval for the mean (when population standard deviation is known) is:")
            st.latex(r"CI = \bar{X} \pm Z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}")
            st.write("Where:")
            st.write("- \( \bar{X} \) is the sample mean.")
            st.write("- \( Z_{\alpha/2} \) is the critical value from the Z-table for the desired confidence level (e.g., 1.96 for 95% confidence).")
            st.write("- \( \sigma \) is the population standard deviation.")
            st.write("- \( n \) is the sample size.")
            
            st.write("### When to Use:")
            st.write("- When estimating population parameters from sample data.")
            st.write("- When assessing the reliability of statistical estimates.")
            
            st.write("### Limitations:")
            st.write("- A larger confidence level (e.g., 99%) results in a wider interval, making estimates less precise.")
            st.write("- Confidence intervals assume random sampling and may be biased if data is not representative.")
            
            st.subheader("Prediction Intervals")
            st.write("A prediction interval estimates a range within which **a new individual observation** is likely to fall.")
            st.write("Unlike confidence intervals, which estimate population parameters, prediction intervals account for individual variability and are generally wider.")
            st.write("The formula is similar to a confidence interval but includes variability in new observations:")
            st.latex(r"PI = \bar{X} \pm t_{\alpha/2} \cdot S \cdot \sqrt{1 + \frac{1}{n}}")
            st.write("Where \( S \) is the sample standard deviation and \( t_{\alpha/2} \) is the critical t-value.")
            
            st.write("### When to Use:")
            st.write("- When forecasting future values rather than estimating parameters.")
            st.write("- When making individual-level predictions in regression models.")
            
            st.write("### Limitations:")
            st.write("- Prediction intervals are always wider than confidence intervals due to additional uncertainty in individual predictions.")
            st.write("- Assumes that new observations come from the same distribution as the training data.")
            
            st.subheader("Automation and Deployment")
            st.write("Automating data workflows improves efficiency and consistency in analytical processes.")
            st.write("- **Automated ETL Pipelines**: Data extraction, transformation, and loading into a database can be scheduled and automated.")
            st.write("- **Model Deployment**: Statistical and machine learning models can be packaged and deployed as APIs for real-time inference.")
            st.write("- **Monitoring & Retraining**: Once deployed, models need periodic monitoring and retraining to maintain accuracy.")
            
            st.write("### When to Use:")
            st.write("- When handling large-scale data pipelines that require consistency.")
            st.write("- When deploying models for real-time applications like recommendation systems or fraud detection.")
            
            st.write("### Limitations:")
            st.write("- Requires careful monitoring to avoid data drift and model degradation over time.")
            st.write("- Initial setup can be complex and resource-intensive.")
            


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

