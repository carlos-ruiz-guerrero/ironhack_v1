web scraping on infojobs job openings, data analysis, machine learning, data visualisation, sql queries 
we want to initially obtain information from infojobs, a top job search tool in Spain, where they post the finest jobs in the it industry, including remote positions
the intention is to initiall obtain the information via web scraping, i chose infojobs because of the way that it has to arrange the information, it clearly has separate fields related to location, job position name, SALARY, required experience, education level, etc. as opposed to linkedin
via web scraping we get a dataset with information regarding the position name, experience level, location and gross avg. annual salary
once we obtain all the information we will perform the different dataset operations, we will represent the information in graphs and also use tableau for data visualisation
sql queries will be implemented to retrieve specific information 
last part of the project consists of a streamlit ui where the user inputs the job name, experience level and location, and the application outputs the avg. yearly salary 

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

As of today, it become obvious the impossibility to retrieve the dataset via web scraping from infojobs.com, since the website has controls in place to prevent web scraping, for which they generate a captcha everytime an element within the container (each one of the job offerings) is accessed; this would require an special captcha validation system and due to budget constraints is not a feasible option, for which we consider: 

a) starting from an already provided .csv dataet from kaggle: https://www.kaggle.com/datasets/datamarket/ofertas-de-trabajo?resource=download
b) finding another website where there are no web scrapping restrictions: https://www.empleate.gob.es/empleo/#/trabajo?search=*&categoria=17&checkVisible=1&pag=0
