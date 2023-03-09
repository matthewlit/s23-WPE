# **CMPSC431W Spring 2023 Web Programming Exercise**

## About Me

>Matthew Kelleher - mtk5386@psu.edu

## About The Project

>A web programming exercise for CMPSC431W: Database Management Systems using python, HTML, Flask, and SQLite. Created a website for the Nittany University Hospital, where a hospital staff may enter and delete patient names in its database.

## Webpage Features

>- **Main Page:** Contains a drop down menu with “Add Patient Name” and “Remove Patient Name” as options and a “Go” button to go to the corresponding page. Controlled by `main` function in `app.py` and `main.html` in `templates`.
>
>- **Add Name Page:** Contains a form that takes as input the “First Name” and “Last Name” of the patient. The form can be submitted with the “Add” Button to insert a record into the database with the given first and last name. The “Go Back” button is used to redirect to the Main Webpage. The information of all the patients currently in the database are displayed under "History". Controlled by `name_add` and `add_name` functions in `app.py` and `add.html` in `templates`.
>
>- **Remove Name Page:** Contains a form that takes as input the “First Name” and “Last Name” of the patient. The form can be submitted with the “Delete” Button to remove a record into the database with the given first and last name. The “Go Back” button is used to redirect to the Main Webpage. The information of all the patients currently in the database are displayed under "History". Controlled by `name_remove` and `remove_name` functions in `app.py` and `remove.html` in `templates`.
>
>- **Bootstrap Modal:** When a user clicks to "Add" or "Delete" a patient from the database a prompt is displayed to "Confirm" the action to add/remove the patent to the database or "Cancel" the action to close the prompt. Controlled by `add.html` and `remove.html` in `templates`.
>
>- **Database:** Contains `users` table that contains a automatically generated `PID` and the `firstname` and `lastname` for each patient in the database. Stored in `database.db`.

## File Organization

>- **templates:** Folder containing HTML templates for the three webpages.
>
>- **app.py:** Python file to control the webpages and the database.
>
>- **database.db:** Database for the webpage containing patient data.

## How To Run

>1. Open Pycharm Professional
>
>2. In the top toolbar click `File` then `Open` and select the `Matthew_Kelleher_WPE` file from where you saved it
>
>3. Click on `app.py`
>
>4. In the top toolbar click `Run` and then `Run 'app.py'`
>
>5. The bottom terminal should open and read `Running on http://127.0.0.1:5000`, click on the link to open the webpage
