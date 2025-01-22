cd "C:\Users\Sloan\Documents\Github\Sloan-Sports-ML-"
git status
git add .
git commit -m "Added dataframes for PGA stats and refactored merging process"
git push origin main


cd /c/Users/Sloan/Documents/Github/Sloan-Sports-ML-

cd /c/Users/Sloan/Documents/Github/Streamlit_Series
cd "/c/Users/Sloan/Documents/Github/Streamlit_Series/python_libraries_pt3"
cd "C:/Users/Sloan/Documents/Github/Streamlit_Series/Pipelines and Workflow pt4"
cd /c/Users/Sloan/Documents/Github/Streamlit_Series/EthicsGovTrust
streamlit run prereq.py
streamlit run sqlcmd.py

\Users\Sloan\Documents\Github\Streamlit_Series\EthicsGovTrust
C:\Users\Sloan\Documents\Github\Streamlit_Series\Python Libaries pt2  
C:\Users\Sloan\Documents\Github\Streamlit_Series\Data Cleaning Pt3
C:\Users\Sloan\Documents\Github\Streamlit_Series\Pipelines and Workflow pt4
C:\Users\Sloan\Documents\Github\Streamlit_Series\Data Modeling pt5
C:\Users\Sloan\Documents\Github\Streamlit_Series\Cloud Platforms pt6
C:\Users\Sloan\Documents\Github\Streamlit_Series\Experimentation & AB pt7
C:\Users\Sloan\Documents\Github\Streamlit_Series\AIML Pt8
C:\Users\Sloan\Documents\Github\Streamlit_Series\EthicsGovTrust pt9

"da2-gsrx5bibzbb4njvhl7t37wqyl4"
https://coding-blocks.github.io/DS-NOTES/1.2%20Introduction%20to%20Matplotlib.html
https://seaborn.pydata.org/tutorial/function_overview.html

# Remove rows where 'SG_Total' is NaN
overview_df = overview_df.dropna(subset=['SG_Total'])

# Verify the result
print("DataFrame Shape After Removal:", overview_df.shape)
print("Remaining Missing Data Summary:\n", overview_df.isnull().sum())
