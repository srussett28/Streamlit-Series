import streamlit as st

def main():
    st.sidebar.title("Navigation")
    selected_option = st.sidebar.radio(
        "Choose a section:",
        ["Title Page", "Tools Needed", "Relevant Books", "Websites", "GitHub Repositories", "Relevant Figures", "Other Resources"]
    )

    if selected_option == "Title Page":
        st.title("Welcome to the Prerequisite Guide")
        intro_image = "started2.png"  # Path to your introductory image
        st.image(intro_image, use_container_width=True)
        st.write(
            """
            This guide will walk you through the tools, resources, and knowledge you need to succeed in this series. 
            Use the navigation on the left to explore different sections!
            """
        )
        st.markdown("---")

    elif selected_option == "Tools Needed":
        st.header("Tools Needed")
        image_toolbox = "toolbox.png"
        st.image(image_toolbox, use_container_width=True)
        st.write("To follow this series, you'll need/nice to have the following tools:")
        tools = [
            "**Python (latest version recommended)** - A versatile programming language that forms the backbone of this series. Essential for running Streamlit apps. [Download](https://www.python.org)",
            "**Streamlit** - A Python library for building interactive web apps. Install via `pip install streamlit`",
            "**Jupyter Notebook or JupyterLab** - Ideal for exploratory data analysis. Install via `pip install notebook`",
            "**VS Code or your preferred IDE** - A powerful and lightweight code editor. [Download](https://code.visualstudio.com)",
            "**Git for version control** - Helps you track changes in your code. [Download](https://git-scm.com)",
            "**SQL Editor (e.g., DBeaver or TablePlus)** - Tools for managing and querying databases. [DBeaver](https://dbeaver.io) | [TablePlus](https://tableplus.com)",
            "**PostgreSQL (optional SQL database)** - A robust open-source SQL database. [Download](https://www.postgresql.org)"
        ]

        for tool in tools:
            st.markdown(f"- {tool}")

        st.header("Additional Git and VS Code Tips")
        image_git = "vscgit.png"
        st.image(image_git, use_container_width=True)
        st.write("To make the most of this series, here are some tips for using Git and VS Code effectively:")

        st.subheader("Git Basics")
        git_commands = [
            "`git init` - Initialize a new Git repository.",
            "`git clone [URL]` - Clone an existing repository.",
            "`git add [file]` - Stage changes for the next commit.",
            "`git commit -m \"message\"` - Commit changes with a message.",
            "`git push` - Push changes to the remote repository.",
            "`git pull` - Fetch and merge changes from the remote repository."
        ]
        for cmd in git_commands:
            st.markdown(f"- {cmd}")

        st.subheader("VS Code and Git Bash")
        st.write("VS Code can be used effectively with Git Bash for terminal programming:")
        st.markdown("1. Configure Git Bash as your default terminal in VS Code.")
        st.markdown("2. Use Git Bash for running Python scripts (`python script.py`) and Git commands.")
        st.markdown("3. Leverage VS Code's built-in Git tools for seamless version control.")    

        st.subheader("VS Code and Extensions")
        extensions = [
            "**GitLens** - Provides powerful Git capabilities.",
            "**Python Extension** - Enables linting, debugging, and IntelliSense for Python development.",
            "**Docker Extension** - Simplifies Docker container management directly in VS Code.",
            "**Prettier** - A code formatter to ensure consistent code style.",
            "**Copilot** - AI-powered coding assistant by GitHub."
        ]
        for ext in extensions:
            st.markdown(f"- {ext}")

        st.markdown("---")

    elif selected_option == "Relevant Books":
        st.header("Relevant Books")
        image_book = "bookcase.png"
        st.image(image_book, caption="Might as well take out stock in O'Reily", use_container_width=True)
        st.write("Expand your knowledge with these resources:")
        books = [
            "'Data Science for Business' by Foster Provost and Tom Fawcett",
            "'Information Dashboard Design' by Stephen Few",
            "'Python for Data Analysis' by Wes McKinney",
            "'Naked Statistics' by Charles Wheelan",
            "'All of Statistics: A Concise Course in Statistical Inference' by Larry Wasserman",
            "'Mathematics for Machine Learning' by Marc Peter Deisenroth, A. Aldo Faisal, and Cheng Soon Ong",
            "'Storytelling with Data' by Cole Nussbaumer Knaflic",
            "'Fundamentals of Data Engineering by Joe Reis and Matt Housley",
            "'Designing Data-Intensive Applications' by Martin Kleppmann",
            "'Introduction to Machine Learning with Python' by Andreas C. Müller and Sarah Guido",
            "'Designing Machine Learning Systems' by Chip Huyen",
            "'The Elements of Statistical Learning: Data Mining, Inference, and Prediction' by Trevor Hastie, Robert Tibshirani, and Jerome Friedman",
            "'AI Engineering: Building Applications with Foundation Models' by Chip Huyen",
            "'Bulletproof Problem Solving' by Charles Conn and Robert McLean",
            "'Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow' by Aurélien Géron",
            "'Streaming Systems' by Tyler Akidau, Slava Chernyak, and Reuven Lax",
            "'Applied Predictive Modeling' by Max Kuhn and Kjell Johnson",
            "'Machine Learning Yearning' by Andrew Ng (free online)",
            "'Data Governance: The Definitive Guide; by Evren Eryurek, Uri Gilad, Jessi Ashdown, and Anita Kibunguchy",
            "'Non-Invasive Data Governance: The Path of Least Resistance and Greatest Success' by Robert S. Seiner",
        ]
        for book in books:
            st.markdown(f"- {book}")

        st.markdown("---")

    elif selected_option == "Relevant Figures":
        st.header("Relevant Figures to Follow")
        image_crew = "crew.png"
        st.image(image_crew, caption="Everybody Accounted for?", use_container_width=True)
        st.write("Stay updated by following these industry leaders:")
        figures = [
            "Andrew Ng (@AndrewYNg) - AI/ML expert, https://www.linkedin.com/in/andrewyng/ , https://www.deeplearning.ai/",
            "Yan LeCun (@ylecun) - Chief AI Scientist at Facebook, https://www.linkedin.com/in/yann-lecun/ ",
            "Swami Sivasubramanian (@SwamiSivasubram) - VP of AWS AI, https://www.linkedin.com/in/swaminathansivasubramanian/ ",
            "Nirmal Budhathoki (@nirmalbudhathoki) - SR Data Scientist @ Microsoft, https://www.linkedin.com/in/nirmal-budhathoki/ " ,
            "Zach Wilson (@_zachwilson) - Data Engineer/Found dataexpert.io, https://www.linkedin.com/in/eczachly/ , https://www.dataexpert.io/",
            "Dawn Choo (@dawnchoong) - Data Scientist, https://www.linkedin.com/in/data-dawn/ " ,
            "Chip Huyen (@chipro) - AI Engineer/Author, https://www.linkedin.com/in/chiphuyen/ " ,
            "Matt Dancho (@mdancho84) - Data Scientist, https://www.linkedin.com/in/mattdancho/ , business-science.io ",
            "Venkata Naga Sai Kumar Bysani (@venkatbysani) - Data Scientist Blue Cross Blue Shield, https://www.linkedin.com/in/saibysani18/ ",
            "Meri Nova (@MeriNova) - AI/ML Engineer, https://www.clicked.com/browse-experiences?distinct_id=merinovacampaign " ,
            "Brad Yerbro (@BradYerbro) - AI/ML Engineer Lockheed Martin, https://www.linkedin.com/in/brad-yerbro/ " ,
            "Rami Krispin (@RamiKrispin) -  SM Data Scientist Apple, https://www.linkedin.com/in/ramikrispin/ " ,
            "Karun Thankachan (@karun_thankachan) - Sr.Data Scientist Walmart , https://www.linkedin.com/in/karunt/ " ,
            "Oun Muhammad (@OunMuhammad) - Sr. Data Analyst Target , https://www.linkedin.com/in/ounmuhammad/ " ,
            "Kelly Adams (@kellyadams) - Data Analyst Golden Heart Games , https://www.linkedin.com/in/kellyjianadams/  " ,
            "Chris French (@chris_french) - Data Analyst , https://www.linkedin.com/in/chris-french-data/ , https://www.datafrenchy.com/  " ,
            "Deepak Goyal (@DeepakGoyal) - Data Engineer https://www.linkedin.com/in/deepak-goyal-93805a17/ , https://adeus.azurelib.com/ ", 
            "Andreas Kretz (@AndreasKretz) - Data Engineer , https://www.linkedin.com/in/andreas-kretz/  , https://learndataengineering.com/?utm_source=linkedin.com&utm_medium=ak_profile",
            "Jess Ramos (@jessramos) - Sr. Data Analyst Crunchbase , https://www.linkedin.com/in/jessramosmsba/  , https://linktr.ee/jessramosdata ",
            "Timur Bikmukhametov (@timurbikm) - Principle Data Scientist , https://www.linkedin.com/in/timurbikmukhametov/ " ,
            "Mark Eltsefon (@MarkEltsefon) - Staff Data Scientist Meta, https://www.linkedin.com/in/mark-eltsefon/ " ,
            "Ethan Mollick (@emollick) - Associate Professor Wharton School, https://www.linkedin.com/in/ethanmollick/ " ,
            "David Langer (@davidlanger) - Data Scientist, https://www.linkedin.com/in/davelanger/ " ,
            "Matt Houssley (@matt_housley) - CTO Ternary Data, https://www.linkedin.com/in/housleymatthew/ " ,
            "Joe Reis (@joe_reis) - Data Engineer/Instructor, https://www.linkedin.com/in/joereis/ " ,
            "Tiffany Teasley (@tiffanyteasley) - Data Scientist Lexis Nexis, https://www.linkedin.com/in/tiffany-teasley/ " ,
            "Carly Taylor (@carly_taylor) - Data Engineer, https://www.linkedin.com/in/carly-taylor-data/" , 
            
        ]
        for figure in figures:
            st.markdown(f"- {figure}")

        st.markdown("---")

    elif selected_option == "Websites":
        st.header("Websites")
        st.write("Here’s an expanded list of valuable websites:")
        websites = [
            "**[Kaggle](https://www.kaggle.com)**  \nA platform offering datasets, competitions, and learning resources for data science and machine learning. It’s perfect for honing skills and exploring real-world datasets.",
            "**[Towards Data Science](https://towardsdatascience.com)**  \nA Medium publication covering Python, machine learning, and AI tutorials. Learn from expert-shared case studies and industry trends.",
            "**[Stack Overflow](https://stackoverflow.com)**  \nThe go-to community Q&A platform for coding and troubleshooting. Ideal for resolving programming challenges.",
            "**[DataCamp](https://www.datacamp.com)**  \nInteractive online courses in data science and analytics. Get hands-on experience with real-world projects.",
            "**[ChatGPT](https://chat.openai.com)**  \nAI-powered assistant for brainstorming, debugging, and learning new concepts. A versatile tool for all experience levels.",
            "**[GitHub](https://github.com)**  \nA platform for hosting and collaborating on code repositories. Access open-source tools, projects, and libraries for your needs.",
            "**[Coursera](https://www.coursera.org)**  \nAn online learning platform offering courses from top universities and companies. Explore data science, AI, and ML courses at your pace.",
            "**[DeepLearning.ai](https://www.deeplearning.ai)**  \nFounded by Andrew Ng, this platform offers specialized courses in deep learning, AI, and ML. Learn from leading experts and real-world case studies.",
            "**[Discord](https://discord.com)**  \nA communication platform where you can join data science, machine learning, and programming communities. Great for networking, discussing projects, and getting help in real-time."
            "**[MIT OpenCourseWare](https://ocw.mit.edu)**  \nFree educational resources from MIT’s actual courses. Explore foundational and advanced topics in data science, AI, and computer science at no cost."
        ]
        for site in websites:
            st.markdown(f"- {site}")

        st.markdown("---")

    elif selected_option == "GitHub Repositories":
        st.header("GitHub Repositories by most stars")
        st.write("Explore these categorized repositories:")
        repos = {
            "Data Science": [
        {"name": "PythonDataScienceHandbook", "url": "https://github.com/jakevdp/PythonDataScienceHandbook", "description": "Companion repository for the Python Data Science Handbook by Jake VanderPlas."},
        {"name": "data-science", "url": "https://github.com/ossu/data-science", "description": "This is a path for those of you who want to complete the Data Science undergraduate curriculum on your own time, for free, with courses from the best universities in the world."},
        {"name": "data-science-ipython-notebooks", "url": "https://github.com/donnemartin/data-science-ipython-notebooks", "description": "Curated repository topics spanning foundational tools, deep learning frameworks, statistical inference, and big data technologies."},
        {"name": "Data-Science-For-Beginners", "url": "https://github.com/microsoft/Data-Science-For-Beginners", "description": "Azure Cloud Advocates at Microsoft offer a 10-week, 20-lesson curriculum all about Data Science."},
        {"name": "DataSciencePython", "url": "https://github.com/ujjwalkarn/DataSciencePython", "description": "Curated list of Python tutorials for Data Science, NLP, and Machine Learning."},
    ],
    "Data Engineer": [
        {"name": "data-engineering-zoomcamp", "url": "https://github.com/DataTalksClub/data-engineering-zoomcamp", "description": "Data Engineering Self Paced Zoomcamp."},
        {"name": "data-engineer-handbook", "url": "https://github.com/DataExpert-io/data-engineer-handbook", "description": "Resources to become an amazing data engineer!"},
        {"name": "data-engineer-roadmap", "url": "https://github.com/datastacktv/data-engineer-roadmap", "description": "Complete picture of the modern data engineering landscape and study guide for aspiring data engineers."},
        {"name": "awesome-data-engineering", "url": "https://github.com/igorbarinov/awesome-data-engineering", "description": "Curated list of awesome things related to Data Engineering."},
        {"name": "data-engineering-practice", "url": "https://github.com/danielbeach/data-engineering-practice", "description": "Data Engineering Practice Problems."},
    ],
    "Machine Learning/AI": [
        {"name": "awesome-machine-learning", "url": "https://github.com/josephmisiti/awesome-machine-learning", "description": "Curated list of awesome machine learning frameworks, libraries, and software (by language)."},
        {"name": "azureml-examples", "url": "https://github.com/Azure/azureml-examples", "description": "Examples and tutorials for Azure Machine Learning services."},
        {"name": "machine_learning_examples", "url": "https://github.com/lazyprogrammer/machine_learning_examples", "description": "Collection of machine learning examples and tutorials."},
        {"name": "homemade-machine-learning", "url": "https://github.com/trekhleb/homemade-machine-learning", "description": "Examples of popular machine learning algorithms implemented in Python with explanations."},
        {"name": "machine-learning-for-trading", "url": "https://github.com/stefan-jansen/machine-learning-for-trading", "description": "Exploring how ML can add value to algorithmic trading strategies."},
    ]
        }
        for category, repo_list in repos.items():
            with st.expander(category):
                for repo in repo_list:
                    st.markdown(f"- [{repo['name']}]({repo['url']})")

        st.markdown("---")

    elif selected_option == "Other Resources":
        image_other = "other.png"
        st.image(image_other, use_container_width=True)
        st.header("Other Resources")
        resources = [
        {
            "name": "[Google Colab](https://colab.research.google.com)",
            "description": (
                "A free cloud-based notebook environment that supports Python and is "
                "great for running machine learning experiments without the need for "
                "local setup. It includes pre-installed popular libraries and allows "
                "for GPU/TPU acceleration."
            )
        },
        {
            "name": "[Anaconda](https://www.anaconda.com)",
            "description": (
                "A Python/R distribution specifically designed for data science. It "
                "comes with a suite of pre-installed libraries and tools, including "
                "Jupyter Notebook, making it easier to manage environments and dependencies."
            )
        },
        {
            "name": "[DataCamp Projects](https://www.datacamp.com/projects)",
            "description": (
                "A collection of guided, hands-on projects designed to apply data science "
                "and analysis concepts in real-world scenarios. Great for building practical experience."
            )
        },
        {
            "name": "[IBM Watson Studio](https://www.ibm.com/cloud/watson-studio)",
            "description": (
                "A collaborative environment for data scientists, developers, and analysts to work on AI, "
                "ML, and deep learning projects. It includes tools for building and deploying models at scale."
            )
        },
        {
            "name": "[OpenAI Playground](https://platform.openai.com/playground)",
            "description": (
                "An interactive environment for exploring GPT-based APIs. Perfect for prototyping and "
                "testing AI solutions using large language models. A great way to familiarize yourself with API capabilities."
            )
        }
    ]
        
        for resource in resources:
            st.markdown(f"### {resource['name']}")
            st.write(resource["description"])
            st.markdown("---")

if __name__ == "__main__":
    main()
