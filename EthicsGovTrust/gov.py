import streamlit as st

# Sidebar navigation
st.sidebar.title("Navigation")
sections = [
    "Title Page",
    "Data Governance",
    "Ethics",
    "Data Security",
    "Collaboration & Communication"
]
selected_section = st.sidebar.radio("Go to:", sections)


if selected_section == "Title Page":
    st.title("Data Governance & Collaboration Hub")
    image_path_logic = "logdu.png"
    st.image("placeholder_image.jpg", caption="The Data Universe", use_column_width=True)


    st.markdown("""
### Welcome to the Data Governance Hub!
This app provides a framework for understanding and implementing:
- **Data Governance**
- **Data Ethics**
- **Data Security**
- **Collaboration & Communication**

---

### Administrative Information
- **Who is this for?** Data Stewards, Analysts, Engineers, Leaders.
- **Navigation:** Use the sidebar to explore each section.
- **Sources:** Based on ISO 27001, FAIR principles, and best practices.

---

### Quick Definitions
- **Data Governance:** Framework for managing data's availability, integrity, and security.
- **Data Ethics:** Guidelines for responsible data use.
- **Data Security:** Measures to protect sensitive data.
- **Collaboration:** Coordinated efforts to share and manage data.
- **Communication:** Transparent exchange of information.
""")
   
    st.markdown("""
### Roles in the Data Universe

#### Data Scientist
- **Why it matters:**
  - Models require unbiased, well-governed data to avoid perpetuating errors.
  - Ethical data use ensures predictions align with societal and organizational values.
  - Secure data protects sensitive training information.
  - Collaboration aligns insights with organizational goals.

#### Data Engineer
- **Why it matters:**
  - Governance ensures pipelines deliver high-quality, compliant data.
  - Ethical handling builds trust and prevents misuse.
  - Security is critical for protecting data in transit and at rest.
  - Collaboration ensures pipelines meet the needs of analysts, scientists, and stakeholders.

#### Data Analyst
- **Why it matters:**
  - Governance provides access to reliable datasets for accurate analysis.
  - Ethics ensures insights are unbiased and support responsible decisions.
  - Secure data prevents unauthorized access to sensitive findings.
  - Collaboration improves storytelling and communication across teams.

#### Analytics/Machine Learning Engineer
- **Why it matters:**
  - Governance ensures compliance when deploying models.
  - Ethics ensures fairness, explainability, and accountability in automation.
  - Security protects production environments and model outputs.
  - Collaboration enables seamless integration into workflows and business alignment.

---

These roles are interconnected, and this app provides a comprehensive understanding of the principles that support them.
""")   

 

# Data Governance Section
elif selected_section == "Data Governance":
    st.header("Data Governance")
    st.subheader("What is Data Governance?")
    st.markdown("""
    Data governance is the set of processes, policies, and frameworks that ensure the integrity, security, and availability of data in an organization.
    """)
    st.subheader("Key Principles")
    st.markdown("""
    - Accountability
    - Transparency
    - Data Quality
    - Compliance
    - Stewardship
    """)
    
    # Framework
    st.subheader("Data Governance Framework")
    st.markdown("""
    - Definition and Importance
    - Components:
      - Policies
      - Standards
      - Procedures
    - Example Frameworks: DAMA-DMBOK, ISO 8000
    """)

    # Roles and Responsibilities
    st.subheader("Roles and Responsibilities")
    st.markdown("""
    - Data Stewards
    - Data Owners
    - Data Users
    - Governance Committees
    """)

    # Data Lifecycle Management
    st.subheader("Data Lifecycle Management")
    st.markdown("""
    - Data Creation and Capture
    - Data Storage and Organization
    - Data Usage and Analysis
    - Data Archiving and Deletion
    """)

    # Policies and Compliance
    st.subheader("Policies and Compliance")
    st.markdown("""
    - Regulatory Requirements (GDPR, CCPA, HIPAA)
    - Internal Policies
    - Audits and Reporting
    """)

    # Data Quality Management
    st.subheader("Data Quality Management")
    st.markdown("""
    - Dimensions of Data Quality: Accuracy, Completeness, Consistency, Timeliness
    - Tools and Techniques
    - Addressing Data Issues
    """)

    # Technology and Tools
    st.subheader("Technology and Tools for Data Governance")
    st.markdown("""
    - Data Governance Platforms
    - Metadata Management Tools
    - Master Data Management (MDM) Systems
    - Data Catalogs
    """)

    # Metrics and KPIs
    st.subheader("Metrics and KPIs")
    st.markdown("""
    - Common Metrics
    - Establishing Baselines
    - Reporting and Dashboards
    """)

    # Challenges
    st.subheader("Challenges in Data Governance")
    st.markdown("""
    - Common Challenges
    - Solutions and Mitigation Strategies
    """)

    # Case Studies
    st.subheader("Case Studies and Best Practices")
    st.markdown("""
    - Real-World Examples
    - Best Practices
    """)

# Ethics Section
elif selected_section == "Ethics":
    st.header("Data Ethics")
    st.subheader("Understanding Data Ethics")
    st.markdown("""
    Data ethics addresses the responsible use of data in ways that respect privacy, autonomy, and societal values.
    """)
    st.subheader("Principles of Ethical Data Use")
    st.markdown("""
    - **Fairness:** Avoid bias and ensure equitable treatment.
    - **Transparency:** Make data practices and algorithms understandable.
    - **Privacy:** Protect personal and sensitive data.
    - **Accountability:** Define ownership and enforce consequences for breaches.
    """)

    # Frameworks for Ethical Practices
    st.subheader("Frameworks for Ethical Data Practices")
    st.markdown("""
    - Ethical AI Guidelines: OECD Principles, EU Ethics Guidelines.
    - FAIR Principles: Findable, Accessible, Interoperable, Reusable.
    - Responsible AI: Reliability, Safety, Explainability.
    - Ethical Design Thinking.
    """)

    # Bias and Fairness
    st.subheader("Bias and Fairness in Data")
    st.markdown("""
    - Types of Bias: Sampling, Algorithmic, Reporting.
    - Mitigating Bias: Diverse datasets, data audits.
    - Case Studies: Real-world examples (e.g., AI hiring tools).
    """)

    # Privacy and Consent
    st.subheader("Privacy and Consent")
    st.markdown("""
    - Importance of Consent: Informed consent for data collection.
    - Privacy Technologies: Differential privacy, federated learning.
    - Managing Sensitive Data: Identifying PII, secure handling.
    """)

    # Ethical Decision-Making
    st.subheader("Ethical Decision-Making in Data Use")
    st.markdown("""
    - Ethical Dilemmas: Balancing business goals and ethics.
    - Decision-Making Frameworks: Identify, Evaluate, Decide, Implement, Review.
    - Risk Assessment: Harm vs. benefit evaluation.
    """)

    # Accountability
    st.subheader("Accountability in Data Ethics")
    st.markdown("""
    - Role of Ethics Committees.
    - Establishing a Code of Ethics.
    - Monitoring and Reporting: Regular audits, incident reports.
    """)

    # Technology and Tools
    st.subheader("Technology and Tools for Ethical Practices")
    st.markdown("""
    - Bias Detection Tools: IBM AI Fairness 360, Google What-If Tool.
    - Privacy Tools: Anonymization software, encryption.
    - Ethical AI Frameworks and Libraries.
    """)

    # Education and Training
    st.subheader("Education and Training")
    st.markdown("""
    - Training for Data Professionals: Courses and certifications.
    - Organizational Training: Workshops and culture-building.
    """)

    # Metrics and KPIs
    st.subheader("Metrics and KPIs for Ethics")
    st.markdown("""
    - Common Metrics: Bias reduction, privacy incidents.
    - Dashboards for Ethical Oversight.
    """)

    # Challenges and Best Practices
    st.subheader("Challenges and Best Practices")
    st.markdown("""
    - Challenges: Ambiguity, balancing profitability and ethics.
    - Best Practices: Privacy by Design, continual evaluation.
    """)

    # Case Studies
    st.subheader("Case Studies in Data Ethics")
    st.markdown("""
    - Positive Examples: Ethical organizations.
    - Negative Examples: Lessons learned (e.g., Cambridge Analytica).
    """)

# Data Security Section
elif selected_section == "Data Security":
    st.header("Data Security")
    st.subheader("Why Data Security Matters")
    st.markdown("""
    Data security protects organizational and personal data from unauthorized access, breaches, or theft.
    """)
    st.subheader("Key Principles of Data Security")
    st.markdown("""
    - **Confidentiality:** Restrict data access to authorized users.
    - **Integrity:** Maintain data accuracy and consistency.
    - **Availability:** Ensure timely access to data when needed.
    - **Accountability:** Log and audit data access and usage.
    """)

    # Types of Data Security
    st.subheader("Types of Data Security")
    st.markdown("""
    - Physical Security: Protect data centers and devices.
    - Network Security: Use firewalls and IDS/IPS.
    - Endpoint Security: Secure individual devices.
    - Application Security: Protect software and APIs.
    - Cloud Security: Secure data stored in the cloud.
    """)

    # Regulations and Standards
    st.subheader("Regulations and Standards")
    st.markdown("""
    - Regulatory Frameworks: GDPR, HIPAA, CCPA.
    - Industry Standards: ISO 27001, NIST Cybersecurity Framework.
    - Compliance: SOC 2, PCI DSS, FedRAMP.
    """)

    # Data Encryption
    st.subheader("Data Encryption")
    st.markdown("""
    - Symmetric vs. Asymmetric Encryption.
    - Encryption in Transit: HTTPS, TLS.
    - Encryption at Rest: Secure stored data.
    - Key Management: Secure storage and rotation of encryption keys.
    """)

    # Access Control
    st.subheader("Access Control")
    st.markdown("""
    - Authentication: Multi-factor authentication (MFA).
    - Authorization: Role-based and attribute-based access control.
    - Least Privilege: Limit user permissions to the minimum necessary.
    - Identity and Access Management (IAM): Manage user identities and permissions.
    """)

    # Data Breaches
    st.subheader("Data Breaches")
    st.markdown("""
    - Common Causes: Phishing, weak passwords, insider threats.
    - Preventative Measures: Training, penetration testing.
    - Incident Response: Steps for detection, containment, and recovery.
    - Case Studies: High-profile breaches and lessons learned.
    """)

    # Monitoring and Auditing
    st.subheader("Monitoring and Auditing")
    st.markdown("""
    - Continuous Monitoring: Detect anomalies in real-time.
    - Logging and Audit Trails: Track data access and usage.
    - Vulnerability Scanning: Regular scans for weaknesses.
    - Incident Reporting: Structured processes for reporting issues.
    """)

    # Backup and Disaster Recovery
    st.subheader("Backup and Disaster Recovery")
    st.markdown("""
    - Backup Strategies: Full, incremental, and differential backups.
    - RTO and RPO: Recovery time and point objectives.
    - Disaster Recovery Plans: Testing and updating plans.
    - Cloud-Based Backup Solutions.
    """)

    # Emerging Threats and Mitigation
    st.subheader("Emerging Threats and Mitigation")
    st.markdown("""
    - Ransomware: Prevention and response.
    - Supply Chain Attacks: Secure third-party dependencies.
    - Zero-Day Exploits: Keep systems updated.
    - Insider Threats: Behavioral monitoring.
    """)

    # Technology and Tools
    st.subheader("Technology and Tools")
    st.markdown("""
    - SIEM Tools: Splunk, IBM QRadar.
    - EDR Tools: CrowdStrike, Carbon Black.
    - Cloud Security: AWS GuardDuty, Azure Security Center.
    - DLP Tools: Symantec DLP, Forcepoint.
    """)

    # Metrics and KPIs
    st.subheader("Metrics and KPIs for Data Security")
    st.markdown("""
    - Key Metrics: Incident count, time to response, patch percentage.
    - Security Dashboards: Visualize and report security posture.
    """)

    # Challenges and Best Practices
    st.subheader("Challenges and Best Practices")
    st.markdown("""
    - Challenges: Evolving threats, balancing security with usability.
    - Best Practices: Zero Trust Architecture, security automation.
    """)

    # Case Studies
    st.subheader("Case Studies in Data Security")
    st.markdown("""
    - Success Stories: Robust security programs.
    - Lessons from Breaches: Analysis and mitigation strategies.
    """)

# Collaboration & Communication Section
elif selected_section == "Collaboration & Communication":
    st.header("Collaboration & Communication")
    # Key Principles
    st.subheader("Key Principles of Collaboration and Communication")
    st.markdown("""
    - **Transparency:** Open sharing of data, insights, and processes.
    - **Accessibility:** Easy access to data and resources for relevant teams.
    - **Accountability:** Clear roles and responsibilities for collaboration.
    - **Alignment:** Synchronize efforts with organizational goals.
    """)

    # Tools and Technologies
    st.subheader("Collaboration Tools and Technologies")
    st.markdown("""
    - **Communication Platforms:** Slack, Microsoft Teams, Zoom.
    - **File Sharing:** Google Drive, SharePoint, Confluence.
    - **Project Management Tools:** Jira, Trello, Asana.
    - **Real-Time Collaboration:** Notion, Miro, collaborative notebooks.
    """)

    # Data Sharing and Governance
    st.subheader("Data Sharing and Governance in Collaboration")
    st.markdown("""
    - Role-based access controls for shared data.
    - Secure data sharing with encryption.
    - Alignment with governance policies.
    - Data versioning and documentation.
    """)

    # Collaborative Culture
    st.subheader("Fostering a Collaborative Culture")
    st.markdown("""
    - Encourage cross-functional teams.
    - Promote inclusive collaboration.
    - Open feedback mechanisms.
    - Celebrate collaborative successes.
    """)

    # Effective Communication
    st.subheader("Best Practices for Effective Communication")
    st.markdown("""
    - Use clear, jargon-free language.
    - Foster active listening.
    - Provide regular updates and stand-ups.
    - Use multi-channel communication for flexibility.
    """)

    # Overcoming Barriers
    st.subheader("Overcoming Barriers to Collaboration")
    st.markdown("""
    - Address time zone differences with asynchronous tools.
    - Standardize documentation for clarity.
    - Resolve conflicts with established protocols.
    - Build trust through transparency and accountability.
    """)

    # Metrics and KPIs
    st.subheader("Metrics and KPIs for Collaboration and Communication")
    st.markdown("""
    - Communication frequency (meetings, updates).
    - Task completion rates and delays.
    - Team engagement levels.
    - Collaboration dashboards for tracking progress.
    """)

    # Real-Time Collaboration
    st.subheader("Real-Time Collaboration in Data Projects")
    st.markdown("""
    - Collaborative data analysis with tools like Databricks.
    - Real-time dashboard updates (Power BI, Tableau).
    - Distributed collaboration with cloud systems.
    """)

    # Case Studies
    st.subheader("Case Studies and Success Stories")
    st.markdown("""
    - Examples of successful interdepartmental projects.
    - Lessons learned from collaborative challenges.
    """)

    # Training and Skill Development
    st.subheader("Training and Skill Development for Collaboration")
    st.markdown("""
    - Workshops on collaborative tools.
    - Communication skills training.
    - Team-building activities.
    - Leadership training for facilitating collaboration.
    """)

# Footer
st.sidebar.markdown("---")
st.sidebar.info("Built with Streamlit")