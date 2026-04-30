# milestone-project-3: Board Silly

# [Deployed Site](https://board-silly-87262ba320b5.herokuapp.com/)

# [Current Palette](https://coolors.co/121212-1e1e1e-a0a0a0-e0e0e0-b8962e-d4af37-f2c94c-c5a75a)

# Contents:

- [UX](#ux)
  - [Strategy](#strategy)
    - [Project Goals](#project-goals)
    - [Business Goals](#business-goals)
    - [User Goals](#user-goals)
    - [User Personas](#user-personas)
  - [Scope](#scope)
    - [User Stories](#user-stories)
  - [Structure](#structure)
    - [Implemented Features](#implemented-features)
  - [Skeleton](#skeleton)
  - [Surface](#surface)
    - [Design Choices](#design-choices)
      - [Artwork](#artwork)
      - [Colour Theme](#colour-theme)
      - [Fonts](#fonts)
      - [Audio](#audio)
- [Accessibility](#accessibility)
- [Technologies Used](#technologies-used)
  - [Languages](#languages)
  - [Libraries](#libraries)
  - [Tools](#tools)
  - [Practices](#practices)
  - [Resources](#resources) 
- [Deployment](#deployment)
- [Steps to Deploy](#steps-to-deploy)
- [How to Run Locally](#how-to-run-locally)
- [Known Bugs and Fixes](#known-bugs-and-fixes)
- [Code Attribution](#code-attribution)
- [Testing](#testing)
  - [User Story Testing](#user-story-testing)
  - [Business Goal Testing](#business-goal-testing)
  - [Code Validation Testing](#code-validation-testing)
  - [Lighthouse Testing](#lighthouse-testing)
  - [Colour Testing](#colour-testing)
  - [Responsiveness Testing](#responsiveness-testing)
  - [Function Testing](#function-testing)

## UX
The Site will be a place where board game enthusiasts and casual board game players can discover new board games, keep a library of games, review and comment on games. With future scope to link social features, more personalisation in the form of recommendations and log play sessions user's have played with their friends. 

### Project Goals
To design and implement a well structured database, embedded in a fully functional full stack web app.

### Business Goals
- Give board game players one place to browse, evaluate and discover new titles 
- Enable users to organise their physical collection and wishlist in one place, reducing the need for spreadsheets or paper lists.
- Build a trusted catalogue of user reviews and ratings that helps others make informed purchasing and playing decisions.
- Lay the groundwork for future social features such as user profiles, followers and personalised recommendations.

### User Goals
- Browse, search and filter the catalogue to find board games that suit their group, budget or taste, supported by community reviews and ratings.
- Keep a personal library of owned games and a wishlist of future purchases, with the ability to filter and organise at a glance.
- Add missing games, write reviews with star ratings, and leave comments on game pages or individual reviews to share knowledge with others.
- Trust that their account and content are protected, receive clear feedback after every action, and know that only they can edit or delete what they have created.

### User Personas
Name: Sam C.
Age: 28
Occupation: Student
Role: Casual Collector
Motivation: Wants a simple way to keep track of his shelf and find games his friend group will enjoy.
Frustrations: Relies on memory or a scrappy notes app. Can't easily filter by player count or complexity.
Usage pattern: Visits occasionally, mainly to add a new game or browse before a game night.

Name: Rhiannon B.
Age: 35
Occupation: Software developer
Role: Enthusiast
Motivation: Reads reviews before every purchase and wants to contribute her own opinions to the community.
Frustrations: Existing sites feel cluttered. Hard to leave focused feedback on a specific game or reply to another user's take.
Usage pattern: Regular visitor — browses new additions, writes reviews after playing, checks comments.

Name: Marcus O.
Age: 42
Occupation: Teacher
Role: Casual Browser
Motivation: Looking for a family-friendly game. Wants honest, readable reviews without needing to sign up.
Frustrations: Overwhelmed by choice. Struggles to find games filtered by age range or complexity without trawling forums.
Usage pattern: Infrequent, task-focused visits. Unlikely to register unless the site gives him clear value first.

Name: Priya K.
Age: 31
Occupation: Librarian
Role: Contributor 
Motivation: Wants the catalogue to be complete and accurate — adds missing games and corrects her own entries.
Frustrations: Annoyed when data is missing or wrong with no way to fix it. Wants a straightforward add/edit flow.
Usage pattern: Moderate frequency — adds a game after buying it, edits entries when she spots errors.

## Scope
### User stories
User Story 1:
As a visitor, I want to be able to register for an account and log in and out so that my library and content are personal to me.

Acceptance Criteria:
- A new user can register with a username and password and is logged in automatically afterwards
- If a username or email is already taken, a helpful error message is shown
- Logging in with correct credentials redirects the user to the home page
- Logging in with incorrect credentials shows an error and does not grant access
- Logging out ends the session and redirects to the home page
- The navigation updates to reflect whether the user is logged in or out


User Story 2:
As a visitor, I want to browse all games and search or filter by title and category so that I can find what I am looking for quickly.

Acceptance Criteria:
- All games are visible on the home page as cards showing the key details
- Searching by title filters the results to matching games
- Filtering by category shows only games in that category
- Both search and filter can be used at the same time
- If nothing matches, a message is shown rather than an empty page

User Story 3:
As a visitor, I want to view the full details of a game including its stats, reviews and comments so that I can learn as much as possible about it before adding it to my library.

Acceptance Criteria:
- Clicking a game card takes the user to the detail page
- The detail page shows all game information including player count, play time, complexity and category
- Reviews and comments are visible on the detail page to all visitors
- If there are no reviews or comments yet, a message is shown encouraging users to be the first

User Story 4:
As a logged-in user, I want to be able to add new games to the catalogue and manage ones I have added so that the catalogue stays accurate and up to date.

Acceptance Criteria:
- Attempting to access the add game page without being logged in redirects to login
- Logged-in users can access an add game form with all the relevant fields
- A game can only be edited or deleted by the user who added it
- Trying to edit or delete someone else's game via the URL redirects with an error
- Successful add, edit and delete actions each show a confirmation message


User Story 5:
As a logged-in user, I want to add games to my personal library with a status of Owned or Wishlist, view my collection and remove games I no longer want tracked.

Acceptance Criteria:
- Logged-in users can add any game to their library from the game detail page
- When adding, the user can choose between Owned and Wishlist
- Adding a game that is already in the library shows a message rather than creating a duplicate
- The library page shows all the user's games with their status clearly displayed
- Games can be removed from the library with a confirmation step
- If the library is empty a message is shown with a prompt to start browsing

User Story 6:
As a logged-in user, I want to write a star rating and review for games I have played so that I can share my opinion with other users.

Acceptance Criteria:
- Logged-in users can submit a review with a rating between 1 and 5 and a written body
- Visitors who are not logged in see a prompt to log in rather than the review form
- A user can only have one review per game, with the option to edit or delete it afterwards
- Deleting a review updates the average rating shown on the game
- The average rating is displayed on both the game card and the detail page

User Story 7:
As a logged-in user, I want to leave a comment on a game's detail page or on a specific review so that I can share thoughts, ask questions or respond directly to what another user has said.

Acceptance Criteria:
- Logged-in users can post a comment on any game's detail page
- Comments appear in chronological order showing the username and date posted
- A user can edit or delete their own comments but not other users' comments
- Visitors can read comments but are prompted to log in to post one
- Successful comment actions show a confirmation message

User Story 8:
As a user, I want to receive clear feedback after every action I take and feel confident that my content is protected from other users.

Acceptance Criteria:
- Every create, update and delete action produces a relevant success message
- Form validation errors are clearly explained so the user knows what to fix
- Protected pages redirect unauthenticated users to the login page
- Users cannot edit or delete content belonging to others, even by manipulating the URL

User Story 9:
As a logged-in user, I want to filter my library by Owned or Wishlist so that I can focus on one part of my collection at a time.

Acceptance Criteria:
- The library page has filter options for All, Owned and Wishlist
- Selecting a filter shows only the matching entries
- If a filter returns no results a helpful message is shown

User Story 10:
As a user, I want to see a helpful branded page if I navigate somewhere that does not exist rather than a confusing generic error.

Acceptance Criteria:
- Any unknown URL shows a custom 404 page that matches the site's design
- The 404 page includes a clear link back to the home page
- The custom page is shown in production with Django DEBUG set to False

(**W**)User Story 11:
As a registered user, I want to follow other users and view public profiles so that I can discover games through people with similar tastes.

Acceptance Criteria:
- Users can follow and unfollow each other
- A feed shows recent activity from followed users
- Public profile pages display a user's library, reviews and stats
- Users can edit their own display name and bio

(**W**)User Story 12:
As a logged-in user, I want to receive game recommendations based on my library so that the experience feels richer and more personalised.

Acceptance Criteria:
- Recommendations are generated based on genres already in the user's library
- Recommendations can be dismissed and do not reappear

User Story 13:
As a developer, I want the finished application deployed to a cloud platform so that it is accessible to anyone with the link.

Acceptance Criteria:
- The deployed app works identically to the development version
- DEBUG is set to False in production
- No secret keys or passwords appear anywhere in the codebase or version history
- The live URL loads correctly with no broken links or missing static files  

User Story 14:
Log a Play Session:
As a logged-in user, I want to log a play session for a board game so that I can keep track of how often I play and who I played with.  

Acceptance Criteria:
- A logged-in user can log a play session from the game detail page
- The user can record the date played, number of players, duration in minutes, and an optional note
- Logged sessions appear on the user's library page under the relevant game
- A session can be deleted by the user who created it with a confirmation step
- If a game has no sessions logged a message is shown  

## Structure
### Implemented Features
User Authentication
- User registration with username and password
- Login and logout functionality
- Navigation updates dynamically based on authentication state
- All protected pages redirect unauthenticated users to login  
![Log In](/static/images/log-in.png)
![Log Out](/static/images/log-out.png)
![Sign up](/static/images/sign-up.png)
![Logged In Nav](/static/images/nav-two.png)
![Logged Out Nav](/static/images/nav-one.png)

Game Catalogue
- Home page displaying all games as cards showing key information
- Search bar filtering games by title
- Category dropdown filter
- Combined search and filter working simultaneously
- No-results state with message
![Game Library](/static/images/game-library.png)
![NoSearch Results](/static/images/nothing-matching-search.png)
![No Filter Results](/static/images/no-filter-match.png)

Game Detail Page
- Full game information display 
- Reviews section visible to all visitors
- Comments section visible to all visitors
- Empty state messages when no reviews or comments exist yet
![Game Detail Page](/static/images/game-detail.png)
![Review and Comment](/static/images/review-and-comment.png)

Game Management
- Add game form with all relevant fields including cover image upload
- Edit game form pre-populated with existing data
- Ownership checks ensuring only the adding user can edit or delete
- Message stating Pending Wait for Added Game to be Approved
- Success and error messages for all actions
![Add Game Form](/static/images/add-game.png)
![Edit Game Form](/static/images/edit-game.png)
![]

Personal Library
- Add any game to personal library from the game detail page
- Choose Owned or Wishlist status when adding
- Duplicate prevention with helpful messaging
- Library page showing all entries with status clearly displayed
- Remove game from library with confirmation step
- Empty state for library with prompt to browse
![Duplicate Library Entry Message](/static/images/game-library-duplicate-warning.png)
![Delete Library Entry Modal](/static/images/delete-library-entry.png)
![Library Entry](/static/images/library-entry.png)
![Empty Library Message](/static/images/empty-library.png)

Log Play Session
- Log How long the game took
- Log who played the game
- Log 1st, 2nd and third place
- Log any notes about how the session went 
- delete session modal
![Play Session](/static/images/session.png)
![Delete Session Modal](/static/images/delete-session.png)

Reviews and Ratings
- Star rating submission (1–5) with written review body
- One review per user per game enforced
- Edit and delete own review
- Average rating calculated and displayed on game cards and detail page
- Login prompt shown to visitors in place of the review form
- reviews awaiting approval have message and faded appearance
![Average Rating](/static/images/average-rating.png)
![Review Awaiting Approval](/static/images/review-and-comment-approval.png)
![delete Comment](/static/images/delete-comment.png)
![Delete Review](/static/images/delete-review.png)
![First to leave a comment](/static/images/comment-first.png)
![First to leave a review](/static/images/first-review-message.png)

Comments and Review Replies
- Reply directly to an individual review
- Comments and replies displayed in chronological order with username and date
- Edit and delete own comments and replies
- Login prompt shown to visitors in place of comment form
- Success messages for all comment and reply actions
![Comment Submit Message](/static/images/comment-submitted-message.png)
![Review Submit Message](/static/images/review-submitted-message.png)

Library Filtering
- Filter library entries by All, Owned or Wishlist status

User Feedback and Access Control
- Flash messages confirming every create, update and delete action
- Clear validation error messages on all forms

Custom 404 Page
- Branded 404 error page matching site design
- Clear link back to the home page
![User 404 Page](/static/images/custom-404-user.png)
![Guest 404 Page](/static/images/custom-404-user.png)

Deployment
- Application deployed to a cloud platform
- Environment variables used for all secret keys
- No secrets or commented out code in the repository

### Future Features
- Social and Community Features
  - Follow and unfollow other users
  - Activity feed showing content from followed users
  - Public user profile pages
  - User display name and bio editing
  - Personalised game recommendations based on library contents
- Live Search (AJAX)
- Log in with social media
- Stat Trackers with personal dashboard with play stats and graphs

## Skeleton
### Database Schema
This is the plan for the structure of my DataBase Tables. The tables changed very slightly during development in order to meet the needs of the project and remain agile.  
I have created 5 database tables for the features that I want to implement. I am using one of Django's built in 'User' table.  
  
![Database Schema](/README_images/db_schema.jpg)

### Wireframes
Desktop Wireframe Templates:  
![Add Game Desktop](/static/images/desktop__add_game_template_wireframe.webp)
![Base and Home Desktop](/static/images/desktop_base_and_home_template_wireframes.webp)  
![Game Detail Desktop](/static/images/desktop_game_detail_template_wireframe.webp)
![User Library Desktop](/static/images/desktop_userlibrary_template_wireframe.webp)  

Mobile Wireframe Templates:  
![Add Game Mobile](/static/images/mobile-user-library-template-wireframe.webp)
![Base and Home Mobile](/static/images/mobile_add_game_template_wireframe.webp)
![Game Detail Mobile](/static/images/mobile_base_and%20_home_template_wireframe.webp)
![User Library Mobile](/static/images/mobile_game_detail_template_wireframe.webp)  
  
The final design deviated slightly as the developement evolved and I learnt more to try and better improve UX throughout the project. The card redesign was a change made to help prioritse information and present it in a more digestable way. Changing the Genre clickable tags into a simple dropdown was a decision made to stick with convention for familiarity and ease of use for the user. 

## Surface
### Design Choices
For the project I want a clean design, dark greys with brighter accent colours(gold/amber). The look was insired by programs like Steam and Dark Mode profiles of other popular apps. This gold colour was made my CTA colour so whenever you will find reactivity or links in the project they will have this colour associated with them for cleear consistent UX.

The Hero Image used was taken by [Madeline Liu](https://unsplash.com/@madeline_sd) and provided by [Unsplash](https://unsplash.com/)
The box art images I uploaded to cloudinary myself were from [Board Game Geek](https://boardgame.geek.com/)   

### Colour Theme
These were the colours chosen for the colour pallette. I wanted to keep it quite simple 
![Colour pallette](/static/images/coloue-pallette.png)

### Fonts
I chose two fonts for the app. Firstly 'Metamorphus', I chose this as the title font as it has a medievil inspired, RPG feel to it, this was used for the app title and game titles. Secondly, Inter, this was chosen for its clarity and simplicity to compliment the more stylised font.

[Metamorphus](https://fonts.google.com/specimen/Metamorphous?preview.script=Latn)
[Inter](https://fonts.google.com/specimen/Inter)

### Design changes
slight changes made during developement:
- changed genre relatioinship from 1:N to N:N to allow games to have multiple genres
- made comment only on reviews not on games. Felt more natural flow. This removed the need for having a nullable field on the comment model.

## Technologies Used
### Dependencies
Core Framework:  
Django==6.0.3 - Main web framework
asgiref==3.11.1ASGI - support layer required by Django
sqlparse==0.5.5SQL - query formatting, required by Django  

Database:  
psycopg==3.3.3 - PostgreSQL database adapter
dj-database-url==3.1.2 - Parses database URLs from environment variables (e.g. for Heroku)  

Authentication:  
django-allauth==65.15.1 - User registration, login, and social authentication  

Forms & UI:
django-crispy-forms==2.6 - Renders Django forms with Bootstrap styling  
crispy-bootstrap5==2026.3 - Bootstrap 5 template pack for crispy-forms  
django-summernote==0.8.20.0 - Rich text / WYSIWYG editor for form fields   
bleach==6.3.0 - Sanitises HTML output from the rich text editor  
webencodings==0.5.1 - Character encoding support used by bleach  

Media & Static Files:  
cloudinary==1.44.2 - Cloudinary SDK for image upload and management
dj3-cloudinary-storage==0.0.6 - Django storage backend for Cloudinary
whitenoise==6.12.0 - Serves static files directly from Django in production  

Deployment:  
gunicorn==25.3.0 - WSGI HTTP server for running Django in production
python-dotenv==1.2.2 - Loads environment variables from a .env file  

HTTP & Networking:  
requests==2.33.1 - HTTP client library (used by Cloudinary SDK)
urllib3==2.6.3 - HTTP connection pooling, used by requests
certifi==2026.2.25 - Mozilla CA certificate bundle for HTTPS verification
charset-normalizer==3.4.7 - Character encoding detection, used by requests
idna==3.12 - Internationalised domain name support, used by requests  

Utilities:  
packaging==26.0 - Version parsing and comparison utilities
six==1.17.0 - Python 2/3 compatibility layer (legacy dependency)
typing_extensions==4.15.0 - Backported type hint support for older Python versions

### Languages
- HTML(Hyper Text Markup Language)
  - DTL(Django Template Language)
- CSS(Cascading Style Sheets)
- JavaScript
- Python 3.12
 
### Libraries and  Frameworks
- Bootstrap
- Django

### Tools
Colours - [coolers](https://coolors.co)
Wireframes - [draw.io](https://app.diagrams.net/)
Debugging & Specific Question Help - [Claude](https://claude.ai), [ChatGPT](https://chatgpt.com/)

### Practices
#### Defensive Programming/Error Handling 
Raise ValueError() for cloudinary url and secret key if not set.(settings.py)  

#### Pythonic Programming
Creating Docstrings for all the functions and classes

### Resources
Bootstrap Documentaion
CSS Documentation
HTML Documentation
Django Documentation

## Deployment
### Steps to Deploy
This web app was deployed through Heroku linked with GitHub.  
Steps taken to deploy:  
- Prepare sttings.py for production deployment
  - DEBUG > False
  - Removing Secret Keys
- Create Pocfile
- Add gunicorn
- Collect Static Files through terminal(`python3 manage.py collectstatic`)
- Push Deployment ready Commit to Github
- Create a Heroku app
- Set Environment Variables in Heroku Settings
- Link ot GitHub
- Deploy app from main branch

### How to Run Locally
To run this project localy make sure you have your virtual environment activated and the correct version of python runing. Then install dependencies using requirements.txt(pip3 install requirements.txt). After this has successfully completed, in the terminal, bash `python3 manage.py runserver`. Hold control/command and click on the link created to auto launch the app in your default browser.  

## Known Bugs and Fixes
- summernote broke the forms without dedicated templates, couldnt find fix so removed it.

- When deployed the text on the cencel register button in gold. I have addressed other links on the register card and it is this that is causing the problem. fix is to delete this style rule:  
``` CSS
.sign-up .card .card-body a {  
  color: var(--text-colour-gold);
}  
```
and instead of targeting and element I crate a class with some added specificity to turn the text gold and apply that class to the `<a>` I want effected.

- The Shadow on my Game Cards does not move with the translation on hover while the card and the border do. I assume this is something to do with what element the CSS class 'clickable' has been applied to in the card structure and pre existing classes that may be applied to the card structure already.

- Star Bar isn't working On Game Session Page. My guess would be this is because the Average rating context lives in the game detail view and not the play session view.

## Code Attribution
Claude wrote the Average Rating Star Bar lines of CSS as this was something I wasn't able to build myself running from lines 218 to 247 in static/css/styles.css.

## Testing
### User story testing
User stories were used t make sure all our targets have been met. The two User Story Acceptance Criteria that were not given a PASS status were part of the 'Won't Have' MoSCoW system. This was expected.  

User Story 1 - Register/Login:
Acceptance criteria: 
- A new user can register with a username and password and is logged in automatically afterwards
- If a username or email is already taken, a helpful error message is shown
- Logging in with correct credentials redirects the user to the home page
- Logging in with incorrect credentials shows an error and does not grant access
- Logging out ends the session and redirects to the home page
- The navigation updates to reflect whether the user is logged in or out  
Status: PASS

User Story 2 - Browse/Search Games:
Acceptance criteria: 
- All games are visible on the home page as cards showing the key details
- Searching by title filters the results to matching games
- Filtering by category shows only games in that category
- Both search and filter can be used at the same time
- If nothing matches, a message is shown rather than an empty page  
Status: PASS

User Story 3 - View Game Details:
Acceptance criteria: 
- Clicking a game card takes the user to the detail page
- The detail page shows all game information including player count, play time, complexity and category
- Reviews and comments are visible on the detail page to all visitors
- If there are no reviews or comments yet, a message is shown encouraging users to be the first  
Status: PASS

User Story 4 - Manage Games:
Acceptance criteria: 
- Attempting to access the add game page without being logged in redirects to login
- Logged-in users can access an add game form with all the relevant fields
- A game can only be edited or deleted by the user who added it
- Trying to edit or delete someone else's game via the URL redirects with an error
- Successful add, edit and delete actions each show a confirmation message  
Status: PASS

User Story 5 - Personal Library:
Acceptance criteria: 
- Logged-in users can add any game to their library from the game detail page
- When adding, the user can choose between Owned and Wishlist
- Adding a game that is already in the library shows a message rather than creating a duplicate
- The library page shows all the user's games with their status clearly displayed
- Games can be removed from the library with a confirmation step; If the library is empty a message is shown with a prompt to start browsing  
Status: PASS
 
User Story 6 - Reviews & Ratings:
Acceptance criteria: 
- Logged-in users can submit a review with a rating between 1 and 5 and a written body
- Visitors who are not logged in see a prompt to log in rather than the review form
- A user can only have one review per game, with the option to edit or delete it afterwards
- Deleting a review updates the average rating shown on the game
- The average rating is displayed on both the game card and the detail page  
Status: PASS 

User Story 7 - Comments:
Acceptance criteria: 
- Logged-in users can post a comment on any game's detail page
- Comments appear in chronological order showing the username and date posted
- A user can edit or delete their own comments but not other users' comments
- Visitors can read comments but are prompted to log in to post one
- Successful comment actions show a confirmation message  
Status: PASS

User Story 8 - Feedback & Security:
Acceptance criteria: 
- Every create, update and delete action produces a relevant success message
- Form validation errors are clearly explained so the user knows what to fix
- Protected pages redirect unauthenticated users to the login page
- Users cannot edit or delete content belonging to others, even by manipulating the URL   
Status: PASS

User Story 9 - Filter Library:
Acceptance criteria: 
- The library page has filter options for All, Owned and Wishlist
- Selecting a filter shows only the matching entries
- If a filter returns no results a helpful message is shown  
Status: PASS

User Story 10 - Custom 404 Page:
Acceptance criteria: 
- Any unknown URL shows a custom 404 page that matches the site's design
- The 404 page includes a clear link back to the home page
- The custom page is shown in production with DEBUG set to False  
Status: PASS 

User Story 11 - Social Features:
Acceptance criteria: 
- Users can follow and unfollow each other
- A feed shows recent activity from followed users
- Public profile pages display a user's library, reviews and stats
- Users can edit their own display name and bio  
Status:

User Story 12 - Recommendations:
Acceptance criteria: 
- Recommendations are generated based on genres already in the user's library
- Recommendations can be dismissed and do not reappear  
Status: TBC

User Story 13 - Deployment:
Acceptance criteria: 
- The deployed app works identically to the development version
- DEBUG is set to False in production
- No secret keys or passwords appear anywhere in the codebase or version history
- The live URL loads correctly with no broken links or missing static files  
Status: TBC

User Story 14 - Log Play Session:
Acceptance criteria: 
- A logged-in user can log a play session from the game detail page
- The user can record the date played, number of players, duration in minutes, and an optional note 
- Logged sessions appear on the user's library page under the relevant game
- A session can be deleted by the user who created it with a confirmation step
- If a game has no sessions logged a message is shown  
Status: PASS

### Code Validation testing
#### HTML Validation
HTML validated using https://validator.x3.org  
- base.html - PASS
- index.html - PASS
- game_detail.html - PASS
  - Action Required and Taken: Adjust the use of `<h>` elements so they do not skip any levels.
- add_game.html - PASS
- edit_game.html - PASS
- Library.html - PASS
  - Action Required and Taken: move an `<a>` element so it stops breaking nesting rules(which had broken the remove from library button) and delete stray closing div tag(`</div>`).  
- play_session.html - PASS
  - Action Required and Taken: Adjust the use of `<h>` elements so they don't skip any levels.  
- Sign up.html - PASS
- Log in.html - PASS
- Log Out.html - PASS
- 404_user.html - PASS
- 404_guest.html - PASS
'Bad Value' erros were raised as the validator didn't like the use of DTL(Django Template Language) however after manually reviewing these points I can discount them and look at the validation of the vanilla HTML surronding the DTL.  
Errors relating to the lack of DOCTYPE and `<head>` were raised on templates that expanded on base.html after reviewing these individually i can discount them and the templates where the errors where raised do in fact all extand the base.html where the DOCTYPE and <head> are located.  

#### CSS Validation
CSS validated using https://jigsaw.w3.org/css-validator/validator.
CSS document validates as CSS Level 3 + SVG.  
image 1 + 2

#### JS Validation 
JS Validated using Claude(Anthropic Ai).
Initially I used a different JS Validator however it brought back too many issues that weren't relevant to the project. e.g. wanting me to define things like 'console' and 'document'. I then switched to Claude and it was assessed to pass syntax validation with one note, make the toggle form approach consistent as I had used two seperte ways of acheiving this. One approach was more robust and eliminates an edge case where the first click on the toggle button woul dhave no affect. I have have gone for making everything in that light. e.g.  
Changing:  
```JavaScript
function toggleReviewForm() {
  const form = document.getElementById("reviewFormContainer");
  form.style.display = form.style.display === "none" ? "block" : "none";
}
```
Into:
```Javascript
function toggleReviewForm() {
  const form = document.getElementById("reviewFormContainer");
  if (form.style.display === "none" || form.style.display === "") {
    form.style.display = "block";
  } else {
    form.style.display = "none";
  }
}
```
#### Python Validation
I used the statis analysis in VS Code to check for syntax errors and these were my findings:
- board_silly
  - settings.py - PASS
  - urls.py - PASS
- game_list
  - admin - PASS
  - forms - PASS
  - models - PASS
    - Action Required and Taken: The 'Models' import was deleted as it was not being used
  - views - PASS
- library_session
  - admin - PASS
  - forms - PASS
  - models - PASS
  - views - PASS
- review_comment
  - admin - PASS
  - forms - PASS
  - models - PASS
  - views - PASS  


### Resposivenesss Testing
Responsiveness was handled mainly By a CSS Grid for the game cards. The resposiveness of the content of the cards was achieved using CSS Flex Properties.  

I have manualy tested the app down to a resolution of 320px and I am happy with it's performnce through the range of screen sizes

(W) Social and Community Features
- Follow and unfollow other users
- Activity feed showing content from followed users
- Public user profile pages
- User display name and bio editing
- Personalised game recommendations based on library contents

### Future Features
- Live Search (AJAX)

#### Games Initially included
This list of initialyy included games is designed to be a good start, but also to be expanded by Regular User's and the Super User:
- Catan
- Terraforming Mars
- Scythe
- Wingspan
- Splendor
- Cosmoctopus
- Diamant
- Carcasonne
- 7 Wonders
- 7 Wonders: Architect
- Plunder
- No Thanks
- Ticket to Ride
- Munchkin
- Apiary
- Twilight Imperium  
  
### Thanks
Thank you for taking the time to read through my project, this has been my favourite thing to make to date and is something I am going to introduce to my friends to see if they actualy want to use it.

Special thanks to Manu my assessor for his support during the course of this project.
