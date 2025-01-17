import streamlit as st

st.title("ETL: The Swiss Army Knife of Data")


st.sidebar.header(" Explore Your Role")
roles = ["Analyst", "Data Scientist", "Data Engineer", "Analytics/ML Engineer"]
selected_role = st.sidebar.radio("Choose your cosmic role:", roles)

# Introduction to ETL
st.markdown("""
Welcome to the ETL universe! Here, you'll explore how **Extract**, **Transform**, and **Load** fit into your role in the data universe. 
Each role uses the **Cosmic Swiss Army Knife** differently. Let's dive into the tools and techniques that make ETL your greatest ally.
""")

# Role-specific content
if selected_role == "Analyst":
    st.header(" ETL for Analysts")
    st.markdown("""
    As an **Analyst**, ETL ensures you have the right data, at the right time, in the right place to make decisions that drive impact.  
    """)
    
    st.subheader(" What ETL Means to You")
    st.markdown("""
    - **Extract**: Accessing datasets from files, APIs, or data warehouses.
    - **Transform**: Cleaning, formatting, and aggregating data for analysis.
    - **Load**: Preparing data for tools like Excel, Tableau, or Power BI.
    """)

    st.subheader("🔍 What to Look For")
    st.markdown("""
    - **Data Freshness and Accuracy**:
        Timely, accurate data is essential for making reliable decisions. As an analyst, you need confidence that the data reflects the most recent updates. 
        - **How to Check**: Ensure ETL pipelines are scheduled or real-time, and monitor for anomalies like duplicate rows or missing values.
        - **Why It's Important**: Outdated or incorrect data can mislead stakeholders, leading to poor decisions.

    - **Transformation Rules Aligning with Business Metrics**:
        Consistency in how metrics like revenue, profit, or churn are calculated is crucial. This alignment ensures everyone interprets the data the same way.
        - **How to Check**: Verify that the logic behind calculations aligns with business definitions. Work with data engineers or scientists to standardize these rules.
        - **Why It's Important**: Inconsistent metrics cause confusion and erode trust in the data.

    - **Data Availability in User-Friendly Formats**:
        Data should be easy to access and ready to use in your preferred tools like Excel, Tableau, or Power BI.
        - **How to Check**: Confirm that data is exported in formats you can work with (e.g., CSV, Excel). Validate that dashboards or reports pull data correctly.
        - **Why It's Important**: Accessible data reduces manual work, improves productivity, and encourages data-driven decision-making.
    """)


    st.subheader("Role in the Pipeline")
    st.markdown("""
    - **Collaborate with Data Engineers and Scientists to define transformation rules**:  
      Analysts often understand the business context better than technical teams. Your role is to ensure that the data is being transformed in ways that align with business needs and metrics.  
      - Example: If the goal is to track "active customers," collaborate to define criteria (e.g., last login within 30 days).  
      - Tip: Use clear documentation to avoid misunderstandings between teams.

    - **Validate data against expected outputs for accuracy**:  
      Analysts are the last line of defense to ensure data quality before it’s used in reporting or decision-making.  
      - Example: Check if totals in a transformed dataset match expected benchmarks, such as monthly revenue.  
      - Tip: Use exploratory tools like Excel, Power BI, or Python to compare results and identify anomalies.

    - **Report issues or anomalies back to the ETL team**:  
      Analysts are often the first to spot discrepancies or errors in the data. Communicating these issues effectively helps maintain pipeline integrity.  
      - Example: Report missing or duplicated records to Data Engineers for investigation.  
      - Tip: Provide specific examples and context when reporting issues to speed up troubleshooting.
    """)



elif selected_role == "Data Scientist":
    st.header(" ETL for Data Scientists")
    st.markdown("""
    As a **Data Scientist**, ETL fuels your machine learning models with feature-rich, clean datasets ready for training.  
    """)
    
    st.subheader(" What ETL Means to You")
    st.markdown("""
    - **Extract**: Pulling raw datasets for training and testing.
    - **Transform**: Feature engineering, scaling, and creating derived attributes.
    - **Load**: Saving data in model-ready formats like Parquet or CSV.
    """)

    st.subheader("What to Look For")
    st.markdown("""
    - **Completeness and Reliability of Raw Data**:
        The success of your models depends on the quality and scope of the input data. Missing, incomplete, or biased data can result in poor model performance.
        - **How to Ensure**: Check for missing values, duplicates, and sufficient representation of all categories or features.
        - **Why It's Important**: Incomplete datasets may cause bias or gaps in your predictions, impacting their reliability.

    - **Transformation Efficiency for Large-Scale Datasets**:
        Efficient transformations are critical when working with large datasets to reduce processing time and computational costs.
        - **How to Ensure**:
          1. Use vectorized operations (e.g., in pandas or NumPy) rather than loops.
          2. Use distributed computing tools like **Dask** or **PySpark** for scaling.
          3. Optimize storage formats (e.g., Parquet over CSV) for faster reads/writes.
        - **Why It's Important**: Slow transformations can delay your workflows, increase costs, and create bottlenecks in your pipeline.

    - **Feature Usability and Integrity**:
        Features are the backbone of your machine learning models. They must be relevant, correctly calculated, and aligned with the problem you are solving.
        - **How to Ensure**:
          1. Validate feature engineering logic (e.g., if `revenue = price × quantity`, ensure the calculation is correct).
          2. Use statistical summaries and visualizations to spot anomalies or inconsistencies.
          3. Check for feature distributions matching assumptions (e.g., normality for linear models).
        - **Why It's Important**: Poorly constructed or irrelevant features can degrade model performance, increase overfitting risk, and obscure insights.
    """)


elif selected_role == "Data Engineer":
    st.header("  ETL for Data Engineers")
    st.markdown("""
    As a **Data Engineer**, you’re the architect of the ETL pipeline, ensuring data flows efficiently and reliably from source to destination.  
    """)
    
    st.subheader("  What ETL Means to You")
    st.markdown("""
    - **Extract**: Building connectors to source data from APIs, databases, or files.
    - **Transform**: Implementing robust, scalable transformations.
    - **Load**: Optimizing data storage in warehouses or lakes.
    """)

    st.subheader(" What to Look For")
    st.markdown("""
    - **Scalability and Performance of the ETL Pipeline**:
        As data volumes grow, ETL pipelines must handle increasing loads efficiently.
        - **How to Ensure**:
          1. Use distributed frameworks like **Apache Spark** or **Dask** to process large datasets.
          2. Optimize queries in your transformations (e.g., index usage in SQL or partitioning in data lakes).
          3. Design pipelines with elasticity to scale resources dynamically.
        - **Why It's Important**: An unscalable pipeline leads to delays, high costs, and bottlenecks, making it unsuitable for modern data needs.

    - **Schema Consistency and Data Integrity**:
        Data schemas must remain consistent to avoid breaking downstream processes.
        - **How to Ensure**:
          1. Validate schemas during the extract and load phases using tools like **Great Expectations**.
          2. Implement version control for schema changes and ensure backward compatibility.
          3. Define constraints at the database or pipeline level to enforce data integrity (e.g., primary keys, foreign keys).
        - **Why It's Important**: Schema changes without proper management can result in failed jobs, inaccurate reports, and broken workflows.

    - **Automation and Error Handling Mechanisms**:
        Automated ETL processes reduce manual intervention and improve reliability.
        - **How to Ensure**:
          1. Use orchestration tools like **Apache Airflow** or **Prefect** to schedule and automate ETL tasks.
          2. Implement robust error handling with retry logic, alerts, and logging.
          3. Create a test environment to simulate pipeline failures and validate recovery mechanisms.
        - **Why It's Important**: Manual processes are prone to human error and delays. Automation ensures timely and reliable pipeline execution.
    """)

    st.subheader(" Basics and Best Practices")
    st.markdown("""
    - **Use Frameworks like Apache Airflow or dbt for Pipeline Orchestration**:
        These tools provide scheduling, dependency management, and monitoring for complex pipelines.
        - **Why It's Important**: They simplify the coordination of tasks, ensuring data flows smoothly between stages.

    - **Implement Idempotent Processes to Prevent Duplication During Failures**:
        Idempotency ensures that reprocessing the same data doesn't create duplicates or inconsistencies.
        - **How to Ensure**:
          1. Use unique identifiers (e.g., transaction IDs) to deduplicate data.
          2. Store checkpoints in your pipeline to track progress and avoid reprocessing the same records.
        - **Why It's Important**: Prevents issues like inflated metrics or wasted storage due to duplicate data.

    - **Monitor and Log Every Stage of the ETL Process**:
        Observability is key to diagnosing and resolving issues in pipelines.
        - **How to Ensure**:
          1. Use logging libraries (e.g., **loguru**, **Python logging**) to capture events and errors.
          2. Implement metrics and alerts with tools like **Prometheus**, **Grafana**, or **CloudWatch**.
          3. Visualize pipeline progress with Airflow dashboards or custom monitoring scripts.
        - **Why It's Important**: Visibility into pipeline health reduces downtime and speeds up debugging when failures occur.
    """)


elif selected_role == "Analytics/ML Engineer":
    st.header("  ETL for Analytics/ML Engineers")
    st.markdown("""
    As an **Analytics/ML Engineer**, you’re focused on integrating ETL pipelines with machine learning workflows and analytical dashboards.  
    """)

    st.subheader(" What ETL Means to You")
    st.markdown("""
    - **Extract**: Integrating data pipelines into ML training systems.
    - **Transform**: Preprocessing and validating data for real-time and batch ML workflows.
    - **Load**: Automating delivery of cleaned data to models or dashboards.
    """)

    st.subheader("🔍 What to Look For")
    st.markdown("""
    - **Reproducibility and Versioning of Datasets**:
        Ensuring that datasets used in ML experiments can be reproduced exactly is critical for debugging, auditing, and collaboration.
        - **How to Ensure**:
          1. Use tools like **Delta Lake** or **DVC** to track changes to datasets.
          2. Store metadata about dataset versions, such as creation date and transformation logic.
          3. Save raw and processed datasets separately for traceability.
        - **Why It's Important**: Reproducibility allows teams to retrace steps, replicate experiments, and maintain trust in the data pipeline.

    - **Compatibility with ML Frameworks (e.g., TensorFlow, PyTorch)**:
        Datasets need to be prepared in formats that ML frameworks can efficiently process.
        - **How to Ensure**:
          1. Use framework-compatible formats (e.g., **TFRecord** for TensorFlow or **NumPy arrays** for PyTorch).
          2. Standardize preprocessing steps to ensure features align with model input requirements.
          3. Validate data pipelines with small test sets before full-scale implementation.
        - **Why It's Important**: Properly formatted datasets minimize preprocessing overhead during training and improve model performance.

    - **Real-Time Processing Capabilities Where Needed**:
        Some ML applications require real-time data ingestion and processing (e.g., fraud detection or recommendation systems).
        - **How to Ensure**:
          1. Use streaming tools like **Apache Kafka** or **Spark Streaming** to process real-time data.
          2. Build pipelines with low-latency transformations and feature generation.
          3. Implement caching mechanisms for frequently accessed features (e.g., embeddings).
        - **Why It's Important**: Real-time capabilities ensure models deliver actionable insights without delay, critical for time-sensitive applications.
    """)

    st.subheader("🛠️ Basics and Best Practices")
    st.markdown("""
    - **Leverage Tools like MLflow for Tracking Data and Model Pipelines**:
        MLflow simplifies tracking experiments, datasets, and models, making pipelines more organized and reproducible.
        - **Why It's Important**: Provides a unified view of the ML lifecycle, from data versioning to model deployment.
        - **How to Ensure**:
          1. Use MLflow's tracking API to log datasets, hyperparameters, and results.
          2. Link each experiment to the dataset and model used.

    - **Ensure Pipelines Integrate with CI/CD Workflows for Automation**:
        Automating the deployment of data and models reduces manual effort and speeds up iterations.
        - **Why It's Important**: Enables rapid experimentation and consistent deployment across environments.
        - **How to Ensure**:
          1. Use tools like **GitHub Actions** or **Jenkins** to trigger ETL and ML workflows automatically.
          2. Test pipelines in staging environments before deploying to production.

    - **Focus on Monitoring and Alerting for Live ML Pipelines**:
        Monitoring ensures that deployed models and data pipelines continue to perform as expected.
        - **Why It's Important**: Detecting drift, anomalies, or pipeline failures early minimizes business impact.
        - **How to Ensure**:
          1. Implement monitoring tools like **Prometheus** or **Grafana** to track metrics (e.g., model accuracy, data freshness).
          2. Set up alerts for performance degradation or pipeline errors.
          3. Regularly retrain models based on updated data to maintain relevance.
    """)


# Footer
st.markdown("""
---
💡 **Tip**: No matter your role, understanding the full ETL process makes you a more effective data professional. Keep exploring the cosmos! 🚀
""")

import streamlit as st
import pandas as pd

st.title("ETL Sandbox: Swiss Army Knife of Data")


st.sidebar.header("Choose Your Role")
roles = ["Analyst", "Data Scientist", "Data Engineer", "Analytics/ML Engineer"]
selected_role = st.sidebar.radio("Select your role:", roles)


st.header(" The Data Magnet (Extract)")
uploaded_file = st.file_uploader("Upload your CSV file:", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Original Data")
    st.dataframe(df)

  
    st.header(" The Data Blender (Transform)")
    st.markdown("**Choose a transformation tool from the Swiss Army Knife!**")
    transform_option = st.selectbox(
        "Select a transformation:",
        ["Filter Rows", "Add a Column", "Group By"]
    )

    if transform_option == "Filter Rows":
        column = st.selectbox("Select a column to filter:", df.columns)
        unique_values = df[column].unique()
        filter_value = st.selectbox("Select a value to filter by:", unique_values)
        df_transformed = df[df[column] == filter_value]
        st.write("### Filtered Data")
        st.dataframe(df_transformed)

    elif transform_option == "Add a Column":
        col_name = st.text_input("Enter the new column name:")
        operation = st.selectbox("Select an operation:", ["Multiply", "Add", "Divide", "Subtract"])
        col1 = st.selectbox("Select the first column:", df.columns)
        col2 = st.selectbox("Select the second column:", df.columns)

        if operation == "Multiply":
            df[col_name] = df[col1] * df[col2]
        elif operation == "Add":
            df[col_name] = df[col1] + df[col2]
        elif operation == "Divide":
            df[col_name] = df[col1] / df[col2]
        elif operation == "Subtract":
            df[col_name] = df[col1] - df[col2]
        
        df_transformed = df
        st.write("### Data with New Column")
        st.dataframe(df_transformed)

    elif transform_option == "Group By":
        group_col = st.selectbox("Select a column to group by:", df.columns)
        agg_col = st.selectbox("Select a column to aggregate:", df.columns)
        agg_func = st.selectbox("Select an aggregation function:", ["Sum", "Mean", "Max", "Min"])

        if agg_func == "Sum":
            df_transformed = df.groupby(group_col)[agg_col].sum().reset_index()
        elif agg_func == "Mean":
            df_transformed = df.groupby(group_col)[agg_col].mean().reset_index()
        elif agg_func == "Max":
            df_transformed = df.groupby(group_col)[agg_col].max().reset_index()
        elif agg_func == "Min":
            df_transformed = df.groupby(group_col)[agg_col].min().reset_index()

        st.write("### Grouped Data")
        st.dataframe(df_transformed)

    # Load data
    st.header("🚀 The Data Catapult (Load)")
    st.markdown("**Launch your data to its destination!**")
    download_format = st.radio("Select a format to download:", ["CSV", "Excel", "Parquet"])

    if st.button("Download Transformed Data"):
        if download_format == "CSV":
            csv = df_transformed.to_csv(index=False).encode('utf-8')
            st.download_button("Download CSV", data=csv, file_name="transformed_data.csv", mime="text/csv")
        elif download_format == "Excel":
            excel = df_transformed.to_excel(index=False, engine='openpyxl')
            st.download_button("Download Excel", data=excel, file_name="transformed_data.xlsx")
        elif download_format == "Parquet":
            parquet = df_transformed.to_parquet(index=False)
            st.download_button("Download Parquet", data=parquet, file_name="transformed_data.parquet")


if selected_role:
    st.sidebar.subheader(f"How this helps you as a {selected_role}")
    if selected_role == "Analyst":
        st.sidebar.markdown("Simplifies data for quick reporting and analysis.")
    elif selected_role == "Data Scientist":
        st.sidebar.markdown("Creates feature-ready datasets for ML workflows.")
    elif selected_role == "Data Engineer":
        st.sidebar.markdown("Highlights scalable transformations for pipeline design.")
    elif selected_role == "Analytics/ML Engineer":
        st.sidebar.markdown("Ensures reproducible and automated pipelines for models.")


