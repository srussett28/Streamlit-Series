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
    image_path_title = "titledu.png"
    st.image( image_path_title, use_container_width=True)


    st.markdown("""
### Welcome to the Data Governance Hub!
This app provides a framework for understanding and implementing:
- **Data Governance**
- **Data Ethics**
- **Data Security**
- **Collaboration & Communication**

---

### Administrative Information
- **Who is this for?** Data Stewards Alike.
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

elif selected_section == "Data Governance":
    st.header("Data Governance")
    image_path_gov = "govdu.png"  
    st.image(image_path_gov, use_container_width=True)
    st.subheader("What is Data Governance?")
    st.markdown("""
    Data governance is the set of processes, policies, and frameworks that ensure the integrity, security, and availability of data in an organization.
    """)
    st.subheader("Key Principles")
    st.markdown("""
- **Accountability**: 
    The obligation to take responsibility for data-related actions and decisions, ensuring roles and processes are clearly defined and executed effectively. 
    Accountability fosters a culture of ownership, reduces errors, and enhances trust within teams and across organizations.

- **Transparency**: 
    The practice of openly sharing data policies, processes, and decisions to build trust and foster understanding among stakeholders. 
    Transparency reduces confusion, promotes collaboration, and builds confidence, especially in regulated or public-facing projects.

- **Data Quality**: 
    The accuracy, completeness, consistency, and reliability of data, ensuring it is fit for its intended purpose. 
    High-quality data enables better decision-making, supports accuracy, and prevents costly inefficiencies or compliance issues.

- **Compliance**: 
    Adherence to laws, regulations, standards, and organizational policies governing data use and protection. 
    Compliance safeguards organizations from penalties and ensures ethical, legal alignment with frameworks like GDPR, HIPAA, or ISO standards.

- **Stewardship**: 
    The responsible management and oversight of data assets, ensuring they are used ethically and effectively throughout their lifecycle. 
    Strong stewardship promotes data accuracy, accessibility, security, and long-term innovation.
""")
    
    # Framework
    st.subheader("Data Governance Framework")
    image_path_frame = "framedu.png"  
    st.image(image_path_frame, use_container_width=True)
    st.markdown("""
    - Definition and Importance
    - **Components**:
    - **Policies**: 
        High-level directives that define the organization's overarching approach to managing and governing data. 
        These include rules for data access, usage, retention, and compliance to ensure alignment with legal and ethical requirements. 
        Example: A policy might mandate that all personally identifiable information (PII) be encrypted during storage and transmission.
    
    - **Standards**: 
        Specific and measurable benchmarks that provide consistency across data-related operations. 
        Standards ensure uniformity in data formats, naming conventions, and metadata usage, fostering seamless integration and collaboration across teams. 
        Example: Standardizing data formats for customer records across systems to ensure compatibility and reduce duplication.

    - **Procedures**: 
        Step-by-step operational guidelines that describe how policies and standards are implemented. 
        Procedures ensure processes like data validation, backup, and sharing are repeatable, consistent, and auditable. 
        Example: A procedure for onboarding new data sources might include steps for profiling the data, assessing its quality, and cataloging it in a centralized repository.
    
    - **Example Frameworks**:
    - **DAMA-DMBOK**: 
        The Data Management Body of Knowledge (DMBOK) is a comprehensive guide that covers all aspects of data management, including governance, quality, security, and architecture. 
        It provides best practices and principles for building a robust data governance framework. 
        Learn more: [DAMA International](https://www.dama.org/content/body-knowledge)

    - **ISO 8000**: 
        This international standard focuses on data quality and interchange, providing guidelines for ensuring data accuracy, completeness, and consistency. 
        It is widely adopted by organizations aiming to maintain high-quality data across global operations. 
        Learn more: [ISO 8000 Information](https://www.iso.org/standard/50798.html)
    """)

    
    st.subheader("Roles and Responsibilities")
    st.markdown("""
- **Data Stewards**: 
    Data Stewards enforce data governance policies and ensure data accuracy, consistency, and security. 
    Their role is vital in maintaining the trustworthiness of organizational data and aligning it with compliance requirements. 
    Best practices include proactive communication with stakeholders, regular data audits, and advocating for ethical data practices.
    - **Includes**: Data Engineers, Data Scientists.

- **Data Owners**: 
    Data Owners are accountable for managing access to data and ensuring compliance with governance frameworks. 
    They play a crucial role in balancing data accessibility with security, enabling efficient workflows without compromising sensitive information. 
    Successful Data Owners establish clear access control policies, periodically review permissions, and collaborate with security teams to prevent breaches.
    - **Includes**: Analytics/ML Engineers, Governance Committee Members.

- **Data Users**: 
    Data Users leverage governed data for analysis, insights, and decision-making. 
    They are critical in translating raw data into actionable strategies that drive business success. 
    To excel, Data Users should prioritize understanding data governance policies, validate the quality of their data, and ensure ethical use of insights.
    - **Includes**: Data Analysts, Data Scientists.

- **Governance Committees**: 
    Governance Committees oversee the creation and enforcement of governance policies, ensuring alignment with organizational goals and regulatory standards. 
    Their importance lies in providing strategic direction and resolving conflicts related to data governance. 
    Best practices include engaging cross-functional stakeholders, conducting regular reviews, and maintaining transparency in decision-making.
    - **Includes**: Leaders from all roles, especially Data Owners.

- **Data Engineer (DE)**: 
    Data Engineers design, build, and maintain pipelines that ensure data is clean, accessible, and secure. 
    Their role is foundational for enabling reliable analytics and machine learning applications. 
    Best practices include documenting workflows, optimizing data pipeline performance, and staying updated with evolving data technologies.
    - **Falls Under**: Data Steward.

- **Data Scientist (DS)**: 
    Data Scientists develop models and extract insights from governed data to solve complex business problems. 
    They rely on high-quality, secure data to ensure their analyses and predictions are accurate and unbiased. 
    To succeed, they should adhere to governance policies, validate data quality before analysis, and communicate results clearly to stakeholders.
    - **Falls Under**: Data Steward, Data User.

- **Data Analyst (DA)**: 
    Data Analysts interpret data and create visualizations to inform strategic decisions. 
    They are essential for transforming data into actionable insights while ensuring compliance with governance standards. 
    Best practices include leveraging validated data sources, ensuring transparency in reporting, and aligning analyses with organizational objectives.
    - **Falls Under**: Data User.

- **Analytics/ML Engineer**: 
    Analytics and ML Engineers deploy machine learning models and integrate them into production systems. 
    They play a pivotal role in ensuring models operate at scale, remain secure, and deliver consistent value. 
    Success requires robust monitoring frameworks, adherence to ethical AI practices, and collaboration with data scientists and engineers.
    - **Falls Under**: Data Owner.
""")

    
    st.subheader("Data Lifecycle Management")
    image_path_cycle = "lcdu.png"  
    st.image(image_path_cycle, use_container_width=True)
    st.markdown("""
- **Data Creation and Capture**: 
    This phase involves generating and collecting data from various sources such as sensors, user inputs, applications, or automated systems. 
    Ensuring high-quality data at the point of creation is crucial for maintaining accuracy and consistency throughout its lifecycle. 
    Best practices include validating inputs, using standardized formats, and implementing automated checks to reduce errors.

- **Data Storage and Organization**: 
    Once data is created, it must be securely stored and organized for easy access and efficient management. 
    This involves selecting appropriate storage solutions (e.g., cloud, on-premise, hybrid) and structuring data using databases, data warehouses, or data lakes. 
    Best practices include encrypting sensitive data, implementing access controls, and optimizing storage for scalability and performance.

- **Data Usage and Analysis**: 
    In this phase, data is utilized for generating insights, creating reports, training machine learning models, or making business decisions. 
    Ensuring ethical and governed use of data is critical to maintaining trust and compliance. 
    Best practices include verifying data quality before use, documenting analysis methods, and safeguarding sensitive information during processing.

- **Data Archiving and Deletion**: 
    As data becomes outdated or redundant, it is either archived for long-term storage or securely deleted to free up resources and ensure compliance with retention policies. 
    Archiving involves moving less frequently accessed data to cost-effective storage solutions, while deletion ensures sensitive information is irretrievably destroyed. 
    Best practices include adhering to regulatory retention guidelines, monitoring access to archived data, and employing secure deletion methods to prevent breaches.
""")


    st.subheader("Policies and Compliance")
    st.markdown("""
- **Regulatory Requirements**: 
    Ensuring compliance with regulatory frameworks is essential to maintaining legal integrity, protecting consumer rights, and safeguarding data. 
    The following regulations have specific requirements for data protection:
    - **GDPR (General Data Protection Regulation)**:
        GDPR is a European Union regulation that focuses on data protection and privacy for all individuals within the EU. 
        It mandates how organizations collect, store, and process personal data, ensuring that individuals have control over their own data. 
        **Key Features**: 
            - Data subjects' rights (e.g., the right to access, the right to erasure, and the right to data portability).
            - Consent requirements for data processing.
            - Data breach notification within 72 hours.
            - Fines for non-compliance can reach up to 4% of annual global turnover or €20 million (whichever is greater).
        
    - **CCPA (California Consumer Privacy Act)**:
        CCPA is a state-level privacy law in California that gives residents the right to know, access, and delete personal data held by businesses. 
        It applies to companies that collect personal data of California residents, even if they are located outside California. 
        **Key Features**:
            - Right to know what personal information is being collected and sold.
            - Right to opt-out of the sale of personal data.
            - Right to request deletion of personal data.
            - Businesses are required to provide clear notices and disclosures to consumers regarding their data.
        
    - **HIPAA (Health Insurance Portability and Accountability Act)**:
        HIPAA is a U.S. regulation designed to ensure the protection of health information, particularly for healthcare providers, insurers, and related organizations. 
        It establishes guidelines for safeguarding protected health information (PHI) and electronic health records (EHRs). 
        **Key Features**: 
            - Requires organizations to implement strict access control and encryption measures.
            - Protects patient privacy, including consent for sharing medical data.
            - Mandates breach notification to affected individuals and the Department of Health and Human Services (HHS) within 60 days.
            - Penalties for non-compliance can include civil and criminal fines, with penalties up to $50,000 per violation.

- **Internal Policies**: 
    Internal policies ensure consistent data governance practices across the organization and help align data management with regulatory and ethical standards. 
    These policies outline how data should be collected, handled, stored, and shared within the organization. 
    Best practices include documenting policies clearly, conducting staff training, and reviewing policies regularly to adapt to new regulations and technologies.

- **Audits and Reporting**: 
    Regular audits are necessary to assess compliance with both internal policies and regulatory requirements. 
    Audits and reporting ensure that data governance practices are transparent and align with the organization’s compliance objectives. 
    Best practices include implementing automated audit processes, conducting regular vulnerability assessments, and creating detailed compliance reports to demonstrate adherence to regulatory requirements.
""")


    
    st.subheader("Data Quality Management")
    image_path_clean = "cleandu.png"  
    st.image(image_path_clean, use_container_width=True)
    st.markdown("""
- **Dimensions of Data Quality**: 
    Data quality is assessed based on key dimensions:
    - **Accuracy**: Ensures data is correct and error-free.
    - **Completeness**: Verifies that no critical data is missing.
    - **Consistency**: Confirms data is uniform across systems and sources.
    - **Timeliness**: Guarantees data is up-to-date and available when needed.
    Best practices include regular data validation, monitoring, and addressing discrepancies promptly.

- **Tools and Techniques**: 
    Organizations leverage various tools and methods to manage data quality:
    - **Data Profiling**: Analyzing data for patterns and anomalies.
    - **Data Cleansing**: Fixing or removing corrupted or inaccurate records.
    - **Automated Quality Checks**: Using tools like Talend, Informatica, or AWS Glue to streamline quality control.

- **Addressing Data Issues**: 
    Effective strategies for resolving data problems include:
    - Identifying root causes of inconsistencies through audits.
    - Establishing data quality ownership within teams.
    - Leveraging data stewards to maintain and improve data quality over time.
""")

    st.subheader("Technology and Tools for Data Governance")
    st.markdown("""
- **Data Governance Platforms**: 
    Comprehensive platforms like **Collibra**, **Informatica**, and **OvalEdge** provide centralized solutions for managing governance workflows, tracking data lineage, and ensuring compliance. 
    These platforms enable collaboration between data stewards, analysts, and business users, ensuring that governance policies are consistently applied. 
    Best practices include automating workflows for data access requests and tracking changes to data assets.

- **Metadata Management Tools**: 
    Tools like **Alation**, **Data.world**, and **Apache Atlas** help manage and document metadata, enabling efficient data discovery and lineage tracking. 
    Metadata management improves transparency by showing how data flows through systems, who has accessed it, and where it originated. 
    Organizations should integrate these tools with existing data catalogs and governance platforms for seamless operations.

- **Master Data Management (MDM) Systems**: 
    MDM tools like **Informatica MDM**, **IBM InfoSphere**, and **Reltio** ensure a single, consistent source of truth for core business data such as customer, product, or supplier information. 
    These systems improve decision-making by reducing duplication and ensuring accurate, consistent data across all systems. 
    Successful MDM implementation requires aligning data hierarchies with business needs and monitoring master data quality regularly.

- **Data Catalogs**: 
    Platforms like **Amundsen**, **Apache Atlas**, and **Google Data Catalog** create searchable inventories of data assets, helping users quickly locate and understand the data they need. 
    Data catalogs enhance productivity by providing rich context (e.g., data descriptions, usage stats, and lineage) and enabling self-service analytics. 
    Best practices include keeping catalogs up-to-date through automated metadata harvesting and ensuring governance policies are embedded into the catalog.
""")

    st.subheader("Metrics and KPIs")
    image_path_kpi = "kpidu.png"  
    st.image(image_path_kpi, use_container_width=True)
    st.markdown("""
- **Common Metrics**: 
    Metrics provide measurable indicators of data governance performance. Examples include:
    - **Data Quality Scores**: Metrics like accuracy, completeness, consistency, and timeliness percentages help assess the overall health of data assets.
    - **Data Usage Metrics**: Track who is accessing data, frequency of use, and compliance with access controls.
    - **Compliance Metrics**: Measure adherence to regulatory requirements (e.g., percentage of data assets meeting GDPR standards or audit completion rates).

- **Establishing Baselines**: 
    - Baselines are the starting point for evaluating improvements over time. Organizations should:
        - Collect historical data on quality and compliance metrics.
        - Use baselines to identify trends and set achievable targets.
        - Establish thresholds for acceptable data quality and compliance levels.

- **Reporting and Dashboards**: 
    - Effective reporting visualizes governance performance and highlights areas for improvement. Examples include:
        - **Dashboards**: Use tools like Power BI or Tableau to create real-time visualizations of key metrics.
        - **Automated Reports**: Schedule reports for compliance metrics or data quality issues, ensuring leadership stays informed.
        - **Stakeholder-Specific Views**: Tailor dashboards for executives, analysts, or stewards to ensure actionable insights for every role.
""")

    st.subheader("Challenges in Data Governance")
    st.markdown("""
- **Common Challenges**:
    - **Siloed Data**: Data stored in isolated systems or departments hinders governance and creates inefficiencies.
    - **Resistance to Change**: Employees may view governance as bureaucratic or burdensome, leading to low adoption.
    - **Resource Constraints**: Insufficient time, budget, or expertise can prevent effective governance implementation.
    - **Evolving Regulations**: Keeping up with constantly changing compliance requirements (e.g., GDPR updates or new local laws) can be overwhelming.

- **Solutions and Mitigation Strategies**:
    - **Breaking Silos**: Use data integration tools like ETL pipelines or cloud data lakes to unify data across systems. Foster cross-functional collaboration to align goals.
    - **Driving Adoption**: Educate employees on the benefits of governance, emphasizing efficiency and improved decision-making. Incentivize compliance through recognition programs.
    - **Addressing Resource Constraints**: Start small by focusing on high-priority areas (e.g., customer data) and scale efforts gradually. Leverage automation to maximize limited resources.
    - **Managing Regulatory Complexity**: Establish a dedicated compliance team or use platforms like Collibra to stay updated and adapt quickly.
""")

    st.subheader("Case Studies and Examples")
    image_path_kpi = "kpidu.png"  
    st.image(image_path_kpi, use_container_width=True)

# Tabs for Standard, Gold Standard, and What Not to Do
    tab1, tab2, tab3 = st.tabs(["Standard", "Gold Standard", "What Not to Do"])

# Standard Example
    with tab1:
     st.markdown("### **Standard: Google’s GDPR Compliance**")
     st.write("""
    **Scenario:**  
    When the General Data Protection Regulation (GDPR) was introduced in Europe, Google implemented policies and tools to ensure compliance. 
    They provided transparency by allowing users to view, download, and delete their data, meeting the basic requirements of GDPR.

    **Why It’s a Standard:**  
    Google achieved compliance by meeting regulatory requirements without going above and beyond to redefine data governance.

    **Key Takeaway:**  
    A standard governance approach focuses on ensuring compliance with laws and regulations, providing baseline protections for user data, 
    and implementing effective tracking and reporting mechanisms.
    """)

# Gold Standard Example
    with tab2:
     st.markdown("### **Gold Standard: Mastercard’s Data Governance Program**")
     st.write("""
    **Scenario:**  
    Mastercard created a robust data governance program, treating data as a strategic asset. 
    They implemented a Data Responsibility Imperative that governs the ethical use of data beyond compliance. 
    This includes advanced encryption, AI ethics committees, and leveraging data to enhance customer experiences without compromising privacy.

    **Why It’s a Gold Standard:**  
    Mastercard goes beyond compliance to build trust, prioritize ethical data use, and innovate responsibly. 
    Their governance approach is proactive, leveraging frameworks like data catalogs and automated metadata management to optimize governance at scale.

    **Key Takeaway:**  
    The gold standard integrates regulatory compliance, ethical responsibility, and innovative technologies 
    into a comprehensive strategy that benefits both the organization and its stakeholders.
    """)

# What Not to Do Example
    with tab3:
     st.markdown("### **What Not to Do: Facebook-Cambridge Analytica Scandal**")
     st.write("""
    **Scenario:**  
    In 2018, Facebook faced scrutiny after it was revealed that Cambridge Analytica improperly accessed and used the personal data of millions of users for political advertising. 
    Facebook's failure to detect and prevent this misuse exposed significant flaws in their data governance practices.

    **Why It’s a Cautionary Tale:**  
    This case highlights the risks of insufficient oversight, lack of user consent mechanisms, and weak controls for third-party data access.

    **Key Takeaway:**  
    Neglecting data governance can result in public backlash, regulatory penalties, and loss of trust. 
    Governance frameworks must ensure robust access controls, transparency, and proactive auditing.
    """)


    st.subheader("Best Practices")
    st.write("""
**1. For Standard Compliance:**  
   - Establish clear data privacy policies aligned with regulations.  
   - Implement tools for user consent, access, and data deletion.  
   - Regularly audit for compliance to avoid legal penalties.  

**2. For Achieving the Gold Standard:**  
   - Treat data as a strategic asset with a strong governance framework.  
   - Develop ethical guidelines for data use and create oversight committees.  
   - Leverage automation, AI, and advanced tools to scale governance effectively.  
   - Foster a culture of trust by being transparent with users about data use.  

**3. To Avoid Governance Pitfalls:**  
   - Regularly review and restrict third-party access to sensitive data.  
   - Ensure transparency in data collection and use policies.  
   - Proactively monitor for unauthorized use or breaches.  
   - Train employees on data governance and ethical data handling practices.  
""")


elif selected_section == "Ethics":
    st.header("Data Ethics")
    
    st.subheader("Understanding Data Ethics")
    st.markdown("""
    Data ethics addresses the responsible use of data in ways that respect privacy, autonomy, and societal values.
    """)
    st.subheader("Principles of Ethical Data Use")
    st.markdown("""
- **Fairness:** Data practices and algorithms should be designed to avoid bias and ensure equitable treatment across all demographics. Organizations must regularly audit systems to identify and mitigate unfair outcomes, promoting inclusion and impartiality.
  
- **Transparency:** Make data collection, processing, and algorithmic decision-making understandable to stakeholders. Clear documentation and open communication help build trust and allow users to make informed decisions about their data.

- **Privacy:** Safeguard personal and sensitive information by implementing robust security measures and adhering to data protection regulations. Privacy-centric design should empower users to control how their data is used.

- **Accountability:** Clearly define ownership of data and decision-making processes, ensuring all stakeholders are held to high standards. Establishing enforcement mechanisms and consequences for breaches helps maintain trust and integrity in the system.
""")


   
    st.subheader("Frameworks for Ethical Data Practices")
    st.markdown("""
- **Ethical AI Guidelines:**  
  Ethical AI guidelines such as the OECD Principles and EU Ethics Guidelines provide a foundation for responsible AI development and deployment. These frameworks emphasize fairness, transparency, and accountability in AI systems, ensuring they align with societal values. The OECD Principles focus on sustainable and inclusive growth, human-centric values, and accountability. The EU Ethics Guidelines add detailed principles like ensuring AI respects human rights and is designed for the common good. Together, they provide a roadmap for developing ethical AI across industries.

- **FAIR Principles:**  
  The FAIR principles—Findable, Accessible, Interoperable, and Reusable—are foundational for managing and sharing data responsibly. They focus on ensuring that data can be easily located, accessed with appropriate permissions, integrated across systems, and reused efficiently. FAIR encourages open metadata standards and interoperability, fostering collaboration and innovation. These principles are particularly relevant in fields like scientific research, where data sharing accelerates discovery. Organizations adhering to FAIR improve data quality, usability, and long-term value.

- **Responsible AI:**  
  Responsible AI emphasizes building AI systems that are reliable, safe, and explainable. Reliability ensures consistent performance under diverse conditions, while safety focuses on preventing harm to users and systems. Explainability ensures stakeholders understand how AI decisions are made, building trust and facilitating accountability. Responsible AI frameworks prioritize human oversight and ethical safeguards, ensuring that AI solutions align with moral and legal standards. They are essential for mitigating biases, errors, and unintended consequences in AI applications.

- **Ethical Design Thinking:**  
  Ethical design thinking integrates ethics into every stage of product and system development. This approach encourages teams to consider the societal impact of their solutions, focusing on inclusivity, fairness, and user well-being. By incorporating diverse perspectives during the ideation and testing phases, ethical design reduces biases and unintended harm. It emphasizes iterative feedback loops, allowing designers to refine solutions to better meet ethical standards. Ethical design thinking is not just about compliance but about fostering innovation that benefits all stakeholders.
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