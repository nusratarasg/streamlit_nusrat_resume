import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from streamlit_timeline import timeline
import plotly.graph_objects as go
from prfdata import *
#from ds_steps import *



st.set_page_config(
    page_title="Nusrat Ara Riaz Resume",
    page_icon="👋",
    layout="wide"
)

#
# edu = [['Advanced Diploma - Health Informatics','Software Engineering','Centennial College, Toronto ON, Canada'],['MS Computer Science','Software Engineering','Preston University, Lahore Pakistan'],['BSc Math, Statistics, Physics','BS Science','Punjab University, Lahore Pakistan']]

# info = {'name':'Nusrat Ara Riaz', 'Brief':'Data Scientist with 2+ years of professional experience looking out to solve complex business problems using AI; Experienced in developing data-driven solutions for automating digitalization of health documents reducing manual efforts by 100% for lab reports & 50% for prescriptions; Love to learn new things. Right now : Streamlit !! ','photo':{'path':'abc.jpg','width':150}, 'Mobile':'8103795345','Email':'mehulgupta2016154@gmail.com','Medium':'https://medium.com/@mehulgupta_7991/about','City':'Nagda, Madhya Pradesh','Stackoverflow_flair':'''<a href="https://stackoverflow.com/users/8422170/mehul-gupta"><img src="https://stackoverflow.com/users/flair/8422170.png?theme=clean" width="250" height="70"  alt="profile for Mehul Gupta at Stack Overflow, Q&amp;A for professional and enthusiast programmers" title="profile for Mehul Gupta at Stack Overflow, Q&amp;A for professional and enthusiast programmers"></a>''','edu':pd.DataFrame(edu,columns=['Qualification','Stream','Institute']),'skills':['Python','Data Science','Machine Learning','Streamlit','Pandas','Matplotlib','Numpy','Data Wrangling','TensorFlow','Scikit-learn','RDBMS','ERD','SQL','HTML/CSS','C','Agile/SCRUM','FileMaker','UML','BPMN','Software Testing'],'achievements':['Web Interface Design Project','Database Project (an eCommerce Project)','Client-Side Website Development Project','Object Oriented Software Methodology Project (Online Catering System)','TARUN Project (Connecting People in a community for useful services) (Fall 2018) - FileMaker','Telehealth Project -- evaluation of mobile health apps','Business Plan Proposal -- based upon Strategyzer Business Model Canvas','Next Generation EMR (Electronic Medical Records)','MWC Volunteer Management System','MWC Senior Meals on Wheels system','MWC Free Medical Clinic System','OCRAT (Online Cancer Risk Assessment Tool)','Fine Naan with Expense Management','RUSMP (Road User Safety Modernization Program) for Ministry of Transportation']}

#'',


st.title('Summary')
st.write('#### Nusrat Ara Riaz')
# components.html(''' <p><b><i>Nusrat Ara Riaz</i></b></p> ''', height=50)

components.html('''
<h2 align="justify" style="font-weight:normal"> Motivated Data Scientist skilled in 1.  Data Analysis and Predictive Data Analysis (using ML algorithms), 2. Python data analysis libraries (Pandas, Numpy, Plotly, Matplotlib, etc.), 3. Streamlit (to Develop shareable web apps in minutes), 4. Claris FileMaker, 5. SQL & Data Modeling, 6. Agile Software Development, 7. Software Prototyping & StoryBoarding, 8. UML & BPMN, 9. Software Testing & Quality Assurance, 10. Business Apps Domain , 11. Health Informatics Domain </h2>
''',
height=160)
 
st.write('#### Coming soon: ')
st.write('##### YouTube Channel (FileMaker, Data Science using Python), Streamlit Apps !!')


# skill_col_size = 5
# embed_component= {'linkedin':"""<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
#         <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="nusratarasg" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://www.linkedin.com/in/nusrat-riaz-21744a85"></a></div>""", 'medium':"""<div style="overflow-y: scroll; height:500px;"> <div id="retainable-rss-embed" 
# data-rss="https://medium.com/feed/retainable,https://medium.com/feed/data-science-in-your-pocket"
# data-maxcols="3" 
# data-layout="grid"
# data-poststyle="inline" 
# data-readmore="Read the rest" 
# data-buttonclass="btn btn-primary" 
# data-offset="0"></div></div> <script src="https://www.twilik.com/assets/retainable/rss-embed/retainable-rss-embed.js"></script>"""}

# with st.sidebar:
#     components.html(embed_component['linkedin'], height=310)

url= 'https://www.linkedin.com/in/nusrat-riaz-21744a85'

st.sidebar.markdown("## [Linkdin Profile](%s)" % url)

resume="https://docs.google.com/document/d/1LNrWJQcSmP94qqB1Av8h3aIUQOxukj2spCY74o6pVls/edit?usp=sharing"
st.sidebar.markdown("## [Download Resume](%s)" % resume)
ml_apps="https://penguin-nusrat-streamlit.herokuapp.com/"
st.sidebar.markdown("## [Sample ML App](%s)" % ml_apps)

st.sidebar.markdown('### Wish to connect?')
st.sidebar.write('Email: nusratarasg@gmail.com')

#st.sidebar.write("check out this [link](https://www.linkedin.com/in/nusrat-riaz-21744a85")

# pdfFileObj = open('FileMaker Resume - Riaz Ahmed.pdf', 'rb')
# st.sidebar.download_button('Download Resume',pdfFileObj,file_name='FileMaker Resume - Riaz Ahmed.pdf',mime='pdf')
# txt = st.text_area('Text to analyze', value='It was the best of times')

#st.balloons()
#
col1, col2, col3 = st.columns([1,4,1])



with col1:
    pass



with col2:
    st.header("Data Science / Data Analysis Pyramid")
    st.image("pyramid.jpg")



with col3:
    pass
#
st.title('My Journey of Data Science - Timelines: ')
with open('timeline.json', "r") as f:
    data = f.read()
timeline(data, height=500)
#

# 
st.title('Technical Skills and Tools: ')
with st.expander("Click + to expand: ", expanded = False):
    components.html('''
    <h3 align="justify" style="font-weight:normal">
    <ol>
    <li>Data Analysis - Python, Pandas, Matplotlib, Numpy, etc.</li>
    <li>Machine Learning Algorithms <i>Scikit-Learn</i> and <i>TensorFlow</i></li>
    <li>Streamlit (to Develop shareable web apps in minutes)</li>  
    <li>FileMaker RAD Development(FileMaker Rel. 12 - 19) -- (7+ Years)</li>
    <li>Software Quality Analyst (Software Testing, <br>Software Quality Assurance) - 10+ Years</li>
    <li>Database Development (SQL, ERD) (10+ Years)</li>
    <li>Agile Software Development (SCRUM, <br>ICONIX, User Stories, Product Backlog, Sprint Backlog, Sprint execution)</li>
    <li>Object Oriented Software Engineering (UML, BPMN)</li>
    <li>UX Prototyping -- Axure RP, HTML/CSS, Tumult Hype</li>
    <li>Strategyzer Business Model Canvas</li>
    </ol>
    </h3>
    ''', height=255, scrolling=True)
# 
# Python Specific Skills
st.title('Python Programming Skills: ')
with st.expander("Click + to expand: ",expanded = False):
    components.html('''
    <h3 align="justify" style="font-weight:normal">
    <ol>
    <li>Vital Python 
        <ul>
            <li>Data Types</li>
            <li>Booleans and Conditionals</li>
            <li>Loops</li>
            
        </ul>
    </li>
    <li> Python Data Structures
        <ul>
            <li>List</li>
            <li>Matrix</li>
            <li>Tupules</li>
            <li>Dictionery</li>
            <li>Sets</li>
            <li>Strings</li>
        </ul>
    </li>
    <li> Python Programs 
        <ul>
            <li>Python Scripts and Modules </li>
            <li>Python Functions</li>
            <li>Variable Scope</li>
            <li>Lambda Functions</li>
            <li>Sets</li>
        </ul>
    </li>
    <li> Python – Classes and Methods
        <ul>
            <li>Define Class</li>
            <li>Class Methods</li>
            <li>Properties</li>
            <li>Inheritance</li>
        </ul>
    </li>
    <li> Python Libraries
        <ul>
            <li>Date & Times</li>
            <li>Pandas</li>
            <li>Numpy</li>
            <li>Matplotlib</li>
            <li><b><i>Streamlit</i></b></li>
        </ul>
    </li>
    <li> Advanced Topics
        <ul>
            <li>Regular Expressions</li>
            <li>Debugging</li>
            <li>Package Installation</li>
            <li>Source Management</li>
        </ul>
    </li>
    </ol>
    </h3>
    ''', height=255, scrolling=True)
# 
# Data Science Skills
st.title('Data Science / Analysis Skills: ')
with st.expander("Click + to expand: ",expanded = False):
    components.html('''
    <h3 align="justify" style="font-weight:normal">
    <ol>
    <li>Pandas DataFrame 
        <ul>
            <li>Import  data from different sources into pandas dataframe</li>
            <li>Explore data</li>
            <li>Grabbing subsets of data</li>
            <li>Adding and Removing Data</li>
            <li>Combine DataFrames | Merge, Join, Concat, & Append</li>
        </ul>
    </li>
    <li> Data Wrangling with Pandas
        <ul>
            <li>Cleaning Data</li>
            <li>Reshaping Data</li>
            <li>Handling duplicate, missing,or invalid data</li>
            <li>Aggregating Data by Group</li>
        </ul>
    </li>
    <li> EDA (Exploratory Data Analysis - Visualizations 
        <ul>
            <li>Matplotlib </li>
            <li>Seaborn</li>
            <li>Plotly</li>
            <li>Graphviz</li>
            li>Pydeck</li>
            <li>Bokeh</li>
            li>Map</li>
        </ul>
    </li>
    <li> Machine Learning with <i><b>Scikit-Learn</b></i> and <b><i>TensorFlow</i></b> 
        <ul>
            <li>Preprocessing data
            <ul>
                <li>Training and Testing Data Sets</li>
                <li>Scaling and Centring data</li>
                <li>Imputing</li>
                <li>Transformations</li>
            </ul>
            </li>
            <li>Build Machine Models
                <ul>
                <li>Linear Regression</li>
                <li>Logistic Regression</li>
                <li>Clustering</li>
                <li>Random Forests</li>
                </ul>
            </li>
        </ul>
    </li>
    <li> Evaluate  Model's Performance
        <ul>
            <li>Confusion Matrix</li>
            <li>Precision</li>
            <li>Accuracy</li>
            <li>Recall</li>
            <li>Specificity</li>
            <li>F1 score</li>
            <li>Precision-Recall or PR curve</li>
            <li>ROC (Receiver Operating Characteristics) curve</li>
            <li>PR vs ROC curve</li>
            <li>Cross-Validation</li>

        </ul>
    </li>
    <li> Predictions</li>
        <ul>
            <li> Predicting Stock Prices Using Pandas and Scikit-learn</li>
        </ul>
    
    
    </ol>
    </h3>
    ''', height=255, scrolling=True)
#
# st.write(info['name'])
# st.subheader('Skills & Tools ⚒️')
# def skill_tab():
#     rows,cols = len(info['skills'])//skill_col_size,skill_col_size
#     skills = iter(info['skills'])
#     if len(info['skills'])%skill_col_size!=0:
#         rows+=1
#     for x in range(rows):
#         columns = st.columns(skill_col_size, gap="small")
#         for index_ in range(skill_col_size):
#             try:
#                 columns[index_].button(next(skills))
#             except:
#                 break
# with st.spinner(text="Loading section..."):
#     skill_tab()



# st.subheader('Career snapshot')

st.subheader('Education 📖')
fig = go.Figure(data=[go.Table(
    header=dict(values=list(info['edu'].columns),
                fill_color='paleturquoise',
                align='center',height=65,font_size=25),
    cells=dict(values=info['edu'].transpose().values.tolist(),
               fill_color='lavender',
               align='left',height=40,font_size=17))])

fig.update_layout(width=850, height=600)
st.plotly_chart(fig)


st.subheader('Achievements 🥇')
achievement_list = ''.join(['<li>'+item+'</li>' for item in info['achievements']])
st.markdown('<ul>'+achievement_list+'</ul>',unsafe_allow_html=True)

st.subheader('Daily routine as Data Scientist')
#st.graphviz_chart(graph)

import graphviz as graphviz

# Create a graphlib graph object


graph = graphviz.Digraph()

graph.edge('Select a Data Set', 'Explore Data')
graph.edge('Select a Data Set', 'Visualize Data')
graph.edge('Explore Data', 'Perform Data Cleaning')
graph.edge('Perform Data Cleaning', 'Perform Data Wrangling')
graph.edge('Use ML Algorithms','Build Machine Model')
graph.edge('Perform Data Wrangling', 'Build Machine Model')
graph.edge('Build Machine Model', 'Train Model')
graph.edge('Train Model', 'Test Model')
graph.edge('Test Model', 'Tested Model')
graph.edge('Tested Model', 'End')
graph.edge('Tested Model', 'Deploy Model')
graph.edge('Deploy Model','As Local Web App')
graph.edge('Deploy Model', 'As Cloud Web App, e.g. Streamlit/Heroku/AWS')
#graph.view()
st.graphviz_chart(graph, use_container_width=False)
