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

## UXD
### User stories
* As a guest/ public user, I want to be able to search for recipes for a particular meal.
* As a guest/ public user, I want to be able to view all recipes to see if something interests me.
* As a guest/ public user, I want to be able to view all recipes of a particular type or theme (e.g. Breakfast, Lunch, Starter, Main, Dessert)
* As a guest/ public user, I want to be able to create an account so that I can add my own recipes.
* As a guest/ public user, I want to be able to view all recipes for a specific user.
* As a registered user, I want to be able to log in to my account.
* As a registered user, I want to be able to log out of my account.
* As a registered user, I want to be able to add my own recipes.
* As a registered user, I want to be able to record the complexity of my recipe.
* As a registered user, I want to be able to detail how many servings my recipe makes.
* As a registered user, I want to be able to detail the prep time for my recipe.
* As a registered user, I want to be able to detail the cook time for my recipe.
* As a registered user, I want to be able to detail the type of meal my recipe is (e.g. Breakfast, Lunch, Starter, Main, Dessert).
* As a registered user, I want to be able to add the ingredients for my recipe.
* As a registered user, I want to be able to add the prepration intructions for my recipe.
* As a registered user, I want to be able to add an image of my meal.
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
* ![#f44336] (https://placehold.it/15/f44336/000000?text=+) `#f44336` - font colour

To keep with the cleanness and simplicity of the application, but to offer a clear contrast to the green branding, white and black font is also used to ensure clear and easy to read content across the site. Red is also used across the site to indicate errors, or items to be addressed.

## Technologies and Tools

## Features

## Future Features to implement

## Testing
### General
### Bugs Encoutered & Fixed

## Deployment

## Credits
### Content
### Images
### Acknowledgements
1. I took guidance from various sources on formatting & styling my web application

* [Stackoverflow] https://stackoverflow.com/questions/37127123/change-color-of-underline-input-and-label-in-materialize-css-framework for guidance on colours on form input fields.
* [Stackoverflow] https://stackoverflow.com/questions/35261021/change-color-of-checkbox-in-materialize-framework for guidance on styling of checkboxes.
* [Materializecss] https://materializecss.com/ and their various guides on usage of their frameworks (icons, buttons, forms, inputs, checkboxes etc.).
* [Tasty] https://tasty.co/ for general inspiration on styling.

2. I used the following to help overcome issues during the development of my application

* [Stackoverflow] https://stackoverflow.com/questions/10426190/how-to-clone-an-element-and-insert-it-multiple-times-in-one-go for guidance on how to insert and remove elements (e.g. ingredients & preparations).
* [mdbootstrap] https://mdbootstrap.com/support/jquery/dropdown-needs-2-clicks-to-activate/ for guidance on how to prevent a bug stopping form selctions not working in initial click.