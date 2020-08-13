# CI-MilestoneProjectThree
## Table of Contents
1. [Overview](#overview)
2. [Live Site](#live-site)
3. [User Experience & Design](#uxd)

    - [Wireframes](#skeleton)
4. [Technologies and Tools](#technologies-and-tools)
5. [Features](#features)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Credits](#credits)


## Overview
The inspiration behind this web application, **Foodology**, was to create a go-to place for *foodies* and other like-minded people to explore the vast cultural differences 
across the culinary world, and share recipe ideas and find new favourite meals with fresh, natural ingredients - That's the big picture - who needs fast food?

We also want to encourage friends and family to share their passion with each other and do so through the medium of cooking, and that can also be acheived here.

Food is a a subject that can connect strangers from all corners of the planet, and at Foodology, we wanted to create a fun and simple to use application to visitors to
view all recipes that have been created and shared by the wonderful food community, as well as allow these guests to create an account and share their own experiences.

* Fed up of the same evening meal routine? No problem.
* Want to prepare a special meal for loved ones? Look no further.
* Struggling for ideas for this week's shopping trip? We've got you covered.

We want our brand to spread far and wide and to encourage the world to give thier taste buds the love that they deserve.

## Live site

The deployed site can be found at [Foodology](https://foodology.herokuapp.com/).

## UXD
### User stories
* As a guest/ public user, I want to be able to search for recipes for a particular meal.
* As a guest/ public user, I want to be able to view all recipes to see if something interests me.
* As a guest/ public user, I want to be able to view all recipes of a particular type or theme
* As a guest/ public user, I want to be able to view all recipes for a specific user.
* As a guest/ public user, I want to be able to create an account so that I can add my own recipes.
* As a registered user, I want to be able to log in to my account.
* As a registered user, I want to be able to log out of my account.
* As a registered user, I want to be able to add my own recipes.
* As a registered user, I want to be able to edit the details of my own recipes.
* As a registered user, I want to be able to delete my own recipes.
* As a registered user, I want to be able to view my own recipes.
* As a registered user, I want to be able to control whether other people can view my recipes.

### Strategy
The key design principle of this site, is to have minimal text (excluding recipe details), and be very visual. 
Visitors have come to search for recipe ideas, or find inspiration and don't want to be distracted by large bodies of text.
Therefore we want to keep the application as sleek as possible and only display information that is applicable to the recipes as user is looking at.
The application therefore needs to be very intuitive, and have simple to use navigation for the guests/users to be able to search for others' recipes or add, edit and delete their own recipes  

### Scope
The scope is to cater for a variety of vistors wanting to find and add a wide variety of recipes.
We therefore want to cater for this audience by allowing users to.
* Create an account and log in.
* Add recipes
    - The type of meal a user is adding.
    - The complexity of the recipe being cooked. 
    - How long it will take to prepare and cook the meal.
    - Add an image of the end product.
    - Add the ingredients required to prepare the recipe.
    - Add instructions on how to cook the recipe.
* View your own recipes.
* Edit or delete your own recipes.
* View other recipes, or search on a particular criteria.

### Structure
It was decided that the Flask framework could be adopted for this application.

This enables the use of template inheritance, and routing, to create an efficient and interactive application with a consistent look and feel throughout.

This allows for multiple blocks of content to be built and maintained, and ultimately utilised dependant on the users interaction with the application.

As defined the scope, we can create block content for:

* Application home/ landing
* Registration 
* Login
* Creating new recipes
* Updating or deleting existing recipes
* Viewing recipes
* Searching for recipes

### Skeleton
<details>
<summary>Base template wireframes</summary>
<p align="center">
    <img height="400" src="https://github.com/lewisclark4/CI-MilestoneProjectThree/blob/master/wireframes/base.png" alt="Base template wireframe">
</p>
</details>

<details>
<summary>Home wireframes</summary>
<p align="center">
    <img height="400" src="https://github.com/lewisclark4/CI-MilestoneProjectThree/blob/master/wireframes/home.png" alt="Home template wireframe">
</p>
</details>

<details>
<summary>Register wireframes</summary>
<p align="center">
    <img height="400" src="https://github.com/lewisclark4/CI-MilestoneProjectThree/blob/master/wireframes/register.png" alt="Register template wireframe">
</p>
</details>

<details>
<summary>Login wireframes</summary>
<p align="center">
    <img height="400" src="https://github.com/lewisclark4/CI-MilestoneProjectThree/blob/master/wireframes/login.png" alt="Login template wireframe">
</p>
</details>

<details>
<summary>View all recipes wireframes</summary>
<p align="center">
    <img height="400" src="https://github.com/lewisclark4/CI-MilestoneProjectThree/blob/master/wireframes/all-recipes-my-recipes.png" alt="View all recipes template wireframe">
</p>
</details>

<details>
<summary>View a recipe wireframes</summary>
<p align="center">
    <img height="400" src="https://github.com/lewisclark4/CI-MilestoneProjectThree/blob/master/wireframes/view-recipes.png" alt="View a recipe template wireframe">
</p>
</details>

<details>
<summary>Add, edit or delete recipe wireframes</summary>
<p align="center">
    <img height="400" src="https://github.com/lewisclark4/CI-MilestoneProjectThree/blob/master/wireframes/add-edit-recipe.png" alt="Add, edit or delete template wireframe">
</p>
</details>

<details>
<summary>Schema overview</summary>
<p align="center">
    <img height="400" src="https://github.com/lewisclark4/CI-MilestoneProjectThree/blob/master/wireframes/schema.png" alt="Add, edit or delete template wireframe">
</p>
</details>

### Surface
#### Font
In-keeping with the clean, modern & simplistic design for the application, the font 'Raleway' was chosen as the primary font for this site.

Raleway is described as an elegant sans-serif typeface.

Raleway is a symbolic representation of the fresh and natural cooking culture that we are trying to inspire.

A standard Sans-serif font is used as a back-up font, should there be any issues with loading the Raleway font.

#### Colour Scheme 

Also in-line with our 'fresh' & 'natural' objective, the colour green was chosen as the brand colours.

The colour green is often reference within health and nature environments and therefore we wanted to enhance these feelings and emotions when the application is being used.

* ![#4caf50](https://placehold.it/15/4caf50/000000?text=+) `#4caf50` - Primary colour
* ![#2e7d32](https://placehold.it/15/2e7d32/000000?text=+) `#2e7d32` - Secondary colour

These are the main branding colours used across the application.

The primary green is a bright fresh green and is aesthetically pleasing.

The secondary green is a deeper darker green and offers a solid contrast, while not deviating from brand colours. 

* ![#fff](https://placehold.it/15/fff/000000?text=+) `#fff` - font colour
* ![#000](https://placehold.it/15/000/000000?text=+) `#000` - font colour
* ![#f44336](https://placehold.it/15/f44336/000000?text=+) `#f44336` - font colour

To keep with the cleanness and simplicity of the application, but to offer a clear contrast to the green branding, white and black font is also used to ensure clear and easy to read content across the site. Red is also used across the site to indicate errors, or items to be addressed.

[Back to Top](#overview)

## Technologies and Tools

The following is a list of tools and technologies used to create the web application
* [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    - Used as the main language for the templates
* [CSS3](https://www.w3.org/Style/CSS/current-work.en.html)
    - Used for styling the webpage
* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
    - Used mostly for DOM manipulation upon user interaction
* [Python](https://www.python.org/)
    - Used for backend data manipulation
* [Materialize](https://materializecss.com/)
    - Used as the main frontend framework
* [Google fonts](https://fonts.google.com/)
    - Used for website fonts
* [Font Awesome](https://fontawesome.com/)
    - To utilise the icon set alongside materialize
* [jQuery](https://jquery.com/)
    - Used to initialize some of the materialize components.
* [Flask](https://palletsprojects.com/p/flask/)
    - Used as the main framework for my application
* [Jinja2 ](https://pypi.org/project/Jinja2/)
    - Used as the main language for the flask templates
* [Pymongo](https://docs.mongodb.com/drivers/pymongo)
    - Used to enable the application to communicate with the mongoDB database
* [MongoDB](https://www.mongodb.com/cloud/atlas)
    - Used as my database host
* [GitHub](https://github.com/)
    - Used to store my project source code
* [Gitpod](https://www.gitpod.io/)
    - Used as my IDE
* [Heroku](https://www.heroku.com/)
    - Used to host the website

### Other Tools

* [Cacoo](https://cacoo.com/)
    - Used to build my Wireframes
* [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools)
    - Used to check site responsiveness, and also help identify and fix bugs
* [W3C Markup Validation Service](https://validator.w3.org/)
    - Used to validate HTML
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
    - Used to validate css
* [JSHint](https://jshint.com/)
    - Used to validate JavaScript
* [PEP8 Online](http://pep8online.com/)
    - Used to validate Python

[Back to Top](#overview)

## Features
### Navigation Bar
The navbar (collapsable on smaller devices) can be used to navigate to different areas of the site depending on user interaction.

The navbar is fixed so that it can be selected by the user at all times for improved UX/ site navigation.

The links in the nabbar are highlighted when hovered over, to give feedback to the user that they can interact with these links.

The website logo & brand also acts as a link back to the home page, as is standard expectation for users.

The links displayed to the users change depending on whether the visitor is a registered user and in session.

This removes the unnecesary links to login or register, and displays links to view or add their personal recipes, as well as log out if required. 

### Footer
The Footer has been kept very clean and simple, and just displays social media icons/ links. 

Similar to the nav links, these social media links also have some simple styling applied to give feedback to a user when they are hovered over.

### Registration
This form is only available to users who are not in session. If a user is in session, they will be prompted to log out before they are able to register a new user.

There is a registration function to enable a user to create an account for the application. This is a basic function that requires a user to create a username and password.

There is validation to prevent a username being created multiple times, and there is also validation for a user to reenter their password to help ensure that it has been typed correctly.

Feedback is given to the user if there are any issues with the data being submitted.

Passwords are hashed using bcrypt to keep the sensitive data encoded.

There is a link to the log-in page if a user has already registered.

### Log in
This form is only available to users who are not in session.

The sign in page is slightly simpler than the registration, and users enter their username and password.

The password is hashed and then compared to the stored, hashed password in the database.

Feedback is given to the user if there are any issues with the data being submitted.

There is a link to the register page if a user needs to create an account.

There is also a log in form in the index.html which is loaded when a user first lands on the site.

### Add Recipe
**C**RUD **C**reate or 'add' a new recipe.

This function is only available to a user that is logged in and in session, else they will be prompted to log-in.

Here you can add all the details of your recipe:

* Recipe Name
* A URL to an image of the recipe/meal
* Cuisine type
* Difficulty level
* Prep time
* Cooking time
* Number of servings
* Any known allergens (a user can select multiple items from a defined list)
* A list of ingredients (a user can add multiple records for each ingredient)
* A list of instructions/ preparations to make the recipe/ meal (a user can add multiple records for each step of the process)

Javascript is used to display picklists, and also insert or remove ingredient & preparation elements dependant on user interaction with the form.

There are multiple validations in this form, some validations are to prompt the user to complete an input field, and some validations relate to the formatting of those input fields.

A user can then submit the form which posts the data to the database.

### Search recipes
This function is available to all users on the recipes/ index page.

This allows a user to enter a search for a key word (e.g. a recipe name, an ingredient or a username), and any applicable results will be returned.

If there are no results returned, then a message is presented to the user to advise to try another search.

### View Recipe
C**R**UD -  **R**ead or 'view' recipes, either public or private.

This is available to all users to select a recipe from the public or private recipe pages, and be able to view the details of that recipe, and the image that has been provided.

### Edit Recipe
CR**U**D **U**pdate or 'edit' a recipe.

This function is only available to the user that created the recipe, and the user has to be in session to be able to update the recipe, else they are displayed a message to advise they are not authorised to make changes to the recipe.

This is very similar to the add recipe feature, but the page will display the details previously saved by the user.

The user is then able to amend, add or remove items from the form.

Appropriate validations are still in place to ensure the form is completed correctly.

### Delete Recipe
CRU**D** Delete or 'remove' a user's own recipes.

This function is only available to the user that created the recipe, and the user has to be in session to be able to update the recipe, else they are displayed a message to advise they are not able to delete the recipe

This function does not fully delete the recipe from the database when requested by a user, it sets a boolean field called 'soft_delete' to True.

This in turn prevents the recipe being displayed as either a public or private recipe.

A user is prompted to confirm they wish to delete the recipe, and is able to cancel at this stage.

However, this function does allow the 'admin' user to delete a recipe from the database completely.

## Future Features to implement
* Add a feature to enable a user to upload personal images directly, rather than need to specify a URL.
* Add a favourites feature to enable users to mark a recipe as their favourite and have easy visibility of these recipes.
* Add an up-vote/ like function to allow users to like others recipes.
* Add a comments function to allow users to interact or ask questions about recipes.
* Add a shopping list feature, to enable a user to create a shopping list using ingredients from a recipe they would like to make.
* Add further information about a recipe (e.g. calories, macronutrient breakdown & any other nutritional information)

[Back to Top](#overview)

## Testing
### General code validation
* HTML validation with [W3C Markup Validation Service](https://validator.w3.org/). While there are some 'errors' as this validator does not interpret Jinja, this allowed me to identify instances where I had missed closing tags etc.
* CSS validation with [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/). My code is fully compliant and there are no errors.
* Javascript validation with [JSHint](https://jshint.com/). My code is fully compliant. There are some warnings about the undefined $ variable being used, given the use of jQuery in my script.js file.
* Python validation with [PEP8 Online](http://pep8online.com/). My code is fully compliant, and there are no errors.

### Browser & Device Compatibility

| **Browser**      | **Device** | **Compatibility**                                            | **Version**            |
| :--------------- | :--------- | :----------------------------------------------------------- | :--------------------- |
| Google Chrome    | PC         | Excellent - Fully compatible                                 | Version 83.0.4103.116  |
| Microsoft Edge   | PC         | Excellent - Fully compatible                                 | Version 84.0.522.59    |
| IE 11            | PC         | Poor - Some styling issues. Add Recipe page unusuable        | Version 11.0.9600.19750|
| Google Chrome    | Mobile     | Excellent - Fully compatible                                 | Version 84.0.4147.125  |
| Firefox          | Mobile     | Excellent - Fully compatible                                 | Version 68.11.0        |
| Microsoft Edge   | Mobile     | Excellent - Fully compatible                                 | Version 45.07.4.505    |
| Mi Browser       | Mobile     | Excellent - Fully compatible                                 | Version 12.4.4-g       |
| Safari           | iPad       | Excellent - Fully compatible                                 | Version 12.4.8         |

### Google Lighthouse

I used Google Lighthouse in the chrome browser to help improve performance & improve Accessibility by flagging missing alt tags for images etc.

| **Device** | **Performance** | **Accessibility** | **Best Practices** | **SEO** |
| :----------| :---------      | :-----------------| :----------------- | :------ |
| Desktop    | 90              | 86                | 86                 | 100     |
| Mobile     | 94              | 86                | 86                 | 100     |

To improve performance, Lighthouse suggests improvements such as resizing images, but as this is user driven across the site, this will not be possible.

To improve accessibility, Lighthouse suggests increaing the contrast ration of background and foreground colours, but I felt the contrast was sufficient and wanted to retain brand colours.

To Improve best practice, Lighthouse suggests using HTTPS. This would require an SSL certficate for my site. Lighthouse also notes the use of jQuery libraries with known vulnerabilities.

### Functional testing
- [x] Test nav links redirect users as appropriate.
- [x] Test all other links redirect users as appropriate.
- [x] Test errors by typing in incorrect page redirects.
- [x] Test access to my recipes, or add and edit recipes without being logged in and confirm I am unable.
- [x] Test access to login and register pages when logged in and confirm I am unable.
- [x] Test search function returns desired results.
- [x] Test social links open new tab as appropriate.
- [x] Test user registration validation - if username exists in DB
- [x] Test user registration validation - if password reentered correctly
- [x] Test user registration - record created in DB with hashed password
- [x] Test user login validation - if username exists in DB
- [x] Test user login validation - if hashed password matches DB record.
- [x] Test user login - user logged in/ session created when correct details added.
- [x] Test create recipe forms and form validations.
- [x] Test add / remove ingredients & preparation records
- [x] Test public vs private recipe toggle.
- [x] Test edit recipe records
- [x] Test soft delete recipe
- [x] Test hard delete recipe 
- [x] Test log out


### Bugs Encountered & Fixed

[Back to Top](#overview)

## Deployment

[Back to Top](#overview)

## Credits
### Content
Recipe ideas we all taken from [BBC Good Food](https://www.bbcgoodfood.com/), although ingredients & recipe details were not carried over verbatim.

All images have been source from the [Pixabay](https://pixabay.com/) images library, and are all free for use, sharing or modification.

### Images
### Acknowledgements
1. I took guidance from various sources on formatting & styling my web application

* [Stackoverflow](https://stackoverflow.com/questions/37127123/change-color-of-underline-input-and-label-in-materialize-css-framework) for guidance on colours on form input fields.
* [Stackoverflow](https://stackoverflow.com/questions/35261021/change-color-of-checkbox-in-materialize-framework) for guidance on styling of checkboxes.
* [Materializecss](https://materializecss.com/) and their various guides on usage of their frameworks (icons, buttons, forms, inputs, checkboxes, modals etc.).
* [Tasty](https://tasty.co/) for general inspiration on styling.

2. I used the following to help overcome issues, bugs and hurdles during the development of my application

* [Stackoverflow](https://stackoverflow.com/questions/10426190/how-to-clone-an-element-and-insert-it-multiple-times-in-one-go) for guidance on how to insert and remove elements (e.g. ingredients & preparations).
* [mdbootstrap](https://mdbootstrap.com/support/jquery/dropdown-needs-2-clicks-to-activate/) for guidance on how to prevent a bug stopping form selctions not working in initial click.
* [Stackoverflow](https://stackoverflow.com/questions/31859903/get-the-value-of-a-checkbox-in-flask) for guidance on passing a value to MongoDB from the checkbox in my add recipe form.
* [Stackoverflow](https://stackoverflow.com/questions/9681601/how-can-i-count-the-number-of-elements-with-same-class) for guidance on how to count the number of classes in a page to allow me to use this in my jquery to add/ remove ingredients & preparations.
* [w3schools](https://www.w3schools.com/tags/att_input_pattern.asp) for guidance on validating the values of text in input fields (allowed me to restrict input in the recipe images to .png & .jpg files).
* [Stackoverflow](https://stackoverflow.com/questions/48679305/want-to-update-only-value-element-of-specific-key-on-mongodb) for guidance on use of the 'Set' operator to update only the soft_delete field when a user deletes a recipe.
* [MongoDB](https://docs.mongodb.com/manual/text-search/) for guidance on creating my search function.
* [Stackoverflow](https://stackoverflow.com/questions/16073865/search-by-objectid-in-mongodb-with-pymongo) for guidance on storing object IDs in my database tables and then calling data back from them.

3. General acknowledgements

* [Pretty Printed Youtube](https://www.youtube.com/channel/UC-QDfvrRIDB6F0bIO4I4HkQ) I have been watching various videos on this channel on use of python and flask to help supplement my learning from Code Institute.

[Back to Top](#overview)