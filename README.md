# Travel Guide / Currency Converter 🌎

![travel_Guide WebbApp](docs/screenshots/readme-travel_guide-banner.png)

<b>Visit the deployed site:</b> [travel_Guide](https://travel-guide.herokuapp.com/)

<b>Visit the repo here:</b> [Github PP3](https://github.com/KimBergstroem/PP3)

Do you know what currency are used in that country? Do you know how much your current currency are in that value?

The Currency Exchanger and Travel Guide is a , <b>Python-based 🐍</b> application that allows users to convert between different currencies and also engages them with a fun travel experience. The application aims to provide a convenient currency conversion tool while offering an enjoyable user experience through captivating design and travel-related questions.

&nbsp;

![GitHub Badge](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=fff&style=flat)
![Gitpod Badge](https://img.shields.io/badge/Gitpod-FFAE33?logo=gitpod&logoColor=fff&style=flat)
![Heroku Badge](https://img.shields.io/badge/Heroku-430098?logo=heroku&logoColor=fff&style=flat)

![Language uses](https://img.shields.io/github/languages/count/kimbergstroem/PP3)

![HTML5 Badge](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=fff&style=flat)
![CSS3 Badge](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=fff&style=flat)
![JSS Badge](https://img.shields.io/badge/JSS-F7DF1E?logo=jss&logoColor=000&style=flat)
![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=flat)
![Markdown Badge](https://img.shields.io/badge/Markdown-000?logo=markdown&logoColor=fff&style=flat)


--- 

## <span id="readme-top">**Table of content**</span>

- [User Story](#user-story🌎)
- [How to Use Travel Guide](#how-to-use-travel-guide🌎)
- [Program Flow](#program-flow🌎)
- [Data Model](#data-model🌎)
- [Technologies Used](#technologies-used🌎)
- [Features](#features🌎)
- [Testing](#testing🌎)
- [Deployment](#deployment🌎)
- [Credits](#credits🌎)

--- 

## **User story**🌎

### First Time Visitor Goals
* <b>As a first-time visitor</b>, I want to be greeted with a welcoming message and an engaging UX style,to set the tone for my experience.
* <b>As a first-time visitor</b>, I want to be presented with a menu of options to explore, such as choosing a destination country or accessing currency conversion information.
* <b>As a first-time visitor</b>, I want to select a destination country and see the currency used in that country, providing me with valuable information for my travels.
* <b>As a first-time visitor</b>, I want to have the option to view a list of currency codes for different countries to help me with currency exchange.

### Returning Visitor Goals
* <b>As a returning visitor</b>, I want to quickly access the travel guide without having to go through the initial welcome and name input process.
* <b>As a returning visitor</b>, I want to explore different options in the menu, such as choosing a new destination country or reviewing currency conversion details.
* <b>As a returning visitor</b>, I want to check the currency code for a specific country without having to navigate through the entire travel guide.
* <b>As a returning visitor</b>, I want to compare currency exchange rates and perform currency conversions for different countries I'm interested in.
* <b>As a returning visitor</b>, I want to have an enjoyable and visually appealing experience with captivating design and engaging travel-related questions.

--- 

## **How to use Travel Guide**🌎
The app will instantly display the converted amount based on current exchange rates. In addition to currency conversion, the app offers engaging travel-related questions to make your experience enjoyable. Explore destination recommendations, travel tips, for your trip planning. Enjoy the convenience of currency conversion and the excitement of discovering new travel insights with the travel_Guide app.

--- 

## **Program flow**🌎
The flowchart represents the logic of the <b>travel_Guide</b> application. The program starts by prompting the user to input their name and validates the input to ensure that the name is at least three letters long and contains only letters.

If the input is valid, a welcome message is shown briefly and then disappears. 
The terminal is cleared, and the program proceeds to display the main menu, offering four different options. Each option leads to a different path of choice by user:

1. <b>Country:</b>
This path prompts the user with different questions such as "Which content do you want to explore?" and "Which country are you interested in?". The user's inputs are processed using the Google Sheets API. If the inputs are valid string values, the information is saved and compared with existing data in the worksheet. This step ensures the correct currency is displayed for the selected country. The application provides the user with the accurate content, country, and currency information. Once all the necessary information is obtained, the user is prompted to either return to the main menu or perform another country search.

2. <b>Currency code:</b>
Choosing this path displays a library of all current currency codes automatically in the prompt. If the user is unfamiliar with the three-letter currency codes, they can select this option to view the codes. These codes are necessary for the currency exchange feature. After displaying the currency codes, the program automatically returns the user to the main menu.

3. <b>Currency Exchange:</b>
This path enables the user to input a currency and an amount to view the exchange rate. The currency exchange is facilitated by an API connected to the application, specifically the "Fixer API". This API provides daily updated rates between different currencies. The user is also presented with the result of the exchange, and if desired, they can choose to exchange another currency. Otherwise, the program asks whether the user wants to perform another currency exchange or return to the main menu.

4. <b>Exit:</b>
Finally, choosing option 4 displays the concluding message and exits the application. The terminal will be closed.



![flowchart](docs/screenshots/readme-flow_chart.png)

--- 

## **Data model**🌎
The program uses the <b>Google Sheets API</b> to access a Google Sheet that contains the content, country and currency data. The program then saves and compare the placeholders for the user inputs and presents the result information. The program uses input() function to get the user's choices and a series of validation functions to ensure that the user inputs are valid.

The <b>Fixer API</b> is utilized in this application to provide access to real-time and historical exchange rate data for currency conversion purposes. It enables the integration of currency exchange functionality.

Also, import <b>sys, time, os, requests, gspread</b> in this application. 
By importing these libraries and modules into the project, I gain access to their respective functionalities and can utilize them for various tasks, such as system interactions, time-related operations, HTTP requests, and Google Sheets integration.

--- 

## **Technologies used**🌎
### **Language**
- <b>Python 3</b>: primary programming language for the project
- <b>Html</b>, <b>css</b> and <b>javascript</b> is also used but only manipulated for better UI experience for user.

### **Programs used**
- [Figma](https://www.figma.com/) an online diagramming tool, was used to create flowcharts for the project
- [Canva](https://www.canva.com/) an all-in-one design tool that offers a user-friendly platform and a vast array of customizable templates to create professional-grade graphics and visual content
- [Gitpd](https://gitpod.io/) cloud-based IDE used for version control and writing code
- [Git](https://git-scm.com/) version control system used for managing and tracking changes to the project's codebase
- [Github](https://github.com/)  web-based hosting service used for version control and storing the project's code after being pushed from Gitpod
- [Heroku](https://www.heroku.com/home) cloud platform used for deploying and hosting the project's web application

--- 

## **Features**🌎
### **Existing features**
The travel_Guide application currently offers the following features:

- <b>Currency Conversion:</b> Users can convert between different currencies using the application. By selecting the source currency, target currency, and entering the desired amount, the app provides the converted value based on current exchange rates.
- <b>Engaging Travel Experience:</b> The app incorporates travel-related questions and trivia, enhancing the user's experience while using the application.
- <b>Destination Recommendations:</b> Users can explore destination recommendations within the app, aiding them in trip planning and discovery.
- <b>User-Friendly Design:</b> The application has an intuitive and captivating design, ensuring a pleasant and enjoyable user interface.

### **Future ideas**
Expanded Story Options: Provide more storylines or story options to allow users to select and engage with different narrative paths.

- <b>Personalization:</b> Offer the option for users to name their favorite teddy bear or customize certain aspects of the travel experience to add a personalized touch.
- <b>More Currency Options:</b> Increase the number of available currencies for conversion, ensuring a wider range of options for users.
- <b>Enhanced Story Interactions:</b> Develop interactive elements within the storylines, allowing users to make choices that have more significant impacts on the narrative.
- <b>Improved Validation and Error Handling:</b> Refine the validation and error handling mechanisms to provide more informative and user-friendly error messages in case of incorrect inputs or invalid data.

--- 

## **Validation**🌎
All string validation have the "<b>.capitalize()</b>" or "<b>.upper()</b>" function to prevent any big or small letter errors.

### **Name validation:**
- 3 or more letters inserted - OK for user name
- Only letters - OK for user name
- Correct name input - OK for user name
- Numbers instead of letters A-Z - OK, gives correct error message
- 2 lettters inserted - OK, gives correct error message

### **Main Meny validation:**
- Chocing 1-4 number: - OK, Takes user to the option entered
- Trying another number besides the "1-4" - OK, gives correct error message
- Trying to insert a string instead - OK, gives the correct error message
- Anything else inserted - OK, gives the correct error message

### **Currency code validation:**
- If putting the 3 letter code - OK, gives the user the option to exchange the currency and know that this currency code exist
- If putting interger instead of string value - OK, gives the correct error message
- If putting wrong 3 letters code - OK, gives the correct error message displaying that this code is not an existing currency code
- Anything else inserted - OK, gives the correct error message

### **All other input int/string validation:**
- blablablablabl


--- 

## **Testing**🌎

### Testing User Stories

**`First Time Visitors`**

| First Time User Goals | How this was achieved | Screenshot |
| --- | --- | --- |
| As a user, my objective is to discover the instructions on how to play the game in order to enhance my gameplay efficiency. | The game has a "rules" page popup which can be accessed by clicking on the "rules" button on the main page. | <details><summary>Screenshot of result</summary>![Result](docs/user-stories/userstories-rulespopup.png)</details> |
| As a user, I desire the ability to validate the correctness of my answers, thereby increasing my score. | When a user clicks on the answer buttons, a visual indication is provided by changing the color of the button. If the selected answer is correct, the button turns green; otherwise, it turns red. | <details><summary>Screenshot of result</summary>![Result](docs/user-stories/userstories-correctanswer.png)</details> |
| As a user, I would like to have visibility of the remaining time so that I can maintain a suitable pace during gameplay and avoid running out of time. | The user is provided with a countdown timer that is visible during their gameplay. The countdown timer also changes color depending on the urgency of time left. | <details><summary>Screenshot of result</summary>![Result](docs/user-stories/userstories-timer.png)</details> |
| As a user, I would like to view my final score at the end of the game in order to see my performance on the scoreboard and dashboard. | Upon completion of the game, the user is presented with their score along with a performance message that reflects their performance, varying based on how well or poorly they performed. | <details><summary>Screenshot of result</summary>![Result](docs/user-stories/userstories-score.png)</details> |
| As a user, I want to be able to cancel the game at any time during play if I do not want to continue. | Upon completion of the game, the user is presented with a quit icon displayed in the upper right corner of the quiz game. By clicking this icon, the user is taken back to the main menu, exiting and resetting the game. | <details><summary>Screenshot of result</summary>![Result](docs/user-stories/userstories-exitbutton.png)</details> |


**`Returning Visitors`**

| Returning User Goals | How this was achieved | Screenshot |
| --- | --- | --- |
| Review past scores | Returning users can access the dashboard that displays their previous quiz scores and username. They can view their improvement over time and compare their scores with other users. | <details><summary>Screenshot of result</summary>![Result](docs/user-stories/userstories-highscore.png)</details> |
| Engage in competitive challenge | The quiz game offers leaderboard functionality where returning users can compete with other players to achieve high scores. | <details><summary>Screenshot of result</summary>![Result](docs/user-stories/userstories-leaderboard.png)</details> |
| Play multiple times without limitations | Users, whether new or returning, have the freedom to play the quiz game multiple times. There are no restrictions on the number of attempts, allowing users to enjoy the game, improve their scores, and challenge themselves without limitations. | <details><summary>Screenshot of result</summary>![Result](docs/user-stories/userstories-playagain.png)</details> |

&nbsp;

Family and friends tested my game on their devices no issues were reported.

The scores below are the average results obtained from three users who attempted the following.
 
|Test|Result  |
|--|--|
|Obtain the welcome message try the name input validation |**100%**|
|In the main meny, try to select an option that is not in the meny, validation |**100%**  |
|In the convert exchange function, try to convert with different amount |**100%**|
|Try the validation on the currency converting |**100%**|
|Try the Enter blank space validation on all input |**100%**|

&nbsp;
### **Solved Bugs**
| Type   | Bug                                                                                                                                                                                                                                                                                                                                           | Solution                                                                                                                                                                                                                                                                                                                                                                    |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| run.py | Coming soon | Coming soon | 
| run.py | Coming soon | Coming soon |  
| run.py | Coming soon | Coming soon |                                                                                                                                                                

&nbsp;
### **Known Bugs**
| Type   | Bug                                                                                                                                                                                                                                                                                                                                           | Solution                                                                                                                                                                                                                                                                                                                                                                    |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| run.py | Coming soon | Coming soon | 
| run.py | Coming soon | Coming soon |  
| run.py | Coming soon | Coming soon |

&nbsp;

--- 

## **Deployment**🌎
To deploy this project, follow these steps:

1. Fork and clone this repository to your local machine.
2. Create a new Heroku app.
3. In the Heroku dashboard, navigate to the app's settings and set the buildpacks to Python and NodeJS in that order.
4. Connect your Heroku app to the repository by linking it to your forked copy of the repository.
5. Click on the "Deploy" button in the Heroku dashboard.

After following these steps, your app should be successfully deployed to Heroku. 

--- 

## **Credits**🌎

The inspiration for this project's development came from a range of online resources, including tutorials from Simplilearn and Stack Overflow. Additionally, references from websites like W3Schools and Code Institute's learning platform were utilized. 

- [Learn Learn Scratch Tutorials](https://www.youtube.com/watch?v=u4QmAIoo4i0) for their tutorial on how to include colors in python terminal.
- [Simplilearn](https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python) for their tutorial on list to string conversion in Python.
- [101Computing](https://www.101computing.net/number-only/) for their tutorial on try and except learning.
- [W3Schools](https://www.w3schools.com/python/ref_string_join.asp) for their tutorial on the `join()` method in Python.
- [Scaler](https://www.scaler.com/topics/capitalize-in-python/) for their tutorial on capitalizing strings in Python.
- [Stack Overflow](https://stackoverflow.com/questions/5904969/how-to-print-a-dictionarys-key) for how to display keys, values in formatted form.
- [Code Institute](https://codeinstitute.net/global/) for checking basic python programming tips and steps.
- [ItNext.io](https://itnext.io/overwrite-previously-printed-lines-4218a9563527) for learning line clearing and line removing with import time.
- [Gspread](https://docs.gspread.org/en/latest/) Library documentation - How to access cells and values in Google Sheets.
- [nkmk](https://note.nkmk.me/en/python-textwrap-wrap-fill-shorten/),  
- [Scaler](https://www.scaler.com/topics/how-to-clear-screen-in-python/) for their discussions on using the `textwrap` module and clearing the screen in Python.

###  **Acknowledgments**

I'd like to give recognition to the individuals who supported me in finishing this project:

* I would like to express my heartfelt appreciation to my family for their patience and assistance in identifying spelling mistakes and testing issues. Their support has been invaluable in improving the quality of this project.
I would also like to extend my gratitude to two testers who have made significant contributions: [Debbie B](https://github.com/DebbieBergstrom) and [Sandra B](https://github.com/SandraBergstrom). They have been instrumental in providing necessary feedback, identifying errors, and offering valuable tips. Their involvement has greatly contributed to the overall refinement of the project.

* [Jubril](https://github.com/Jubrillionaire), my Code Institute Mentor, for his exceptional guidance and expertise. His mentorship has been a source of inspiration and has greatly contributed to my growth as a developer.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

--- 
&nbsp;
