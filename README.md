# milestone-project-3: Board Silly

## UX

### Project goals
To design and implement a well structured database, embedded in a fully functional full stack web app.

### User stories
User Story 1:
As a visitor, I want to be able to register for an account and log in and out so that my library and content are personal to me.

Acceptance Criteria:
- A new user can register with a username, email and password and is logged in automatically afterwards
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

### Features
User Authentication
- User registration with username and password
- Login and logout functionality
- Navigation updates dynamically based on     authentication state
- All protected pages redirect unauthenticated users to login

Game Catalogue
- Home page displaying all games as cards showing key information
- Search bar filtering games by title
- Category dropdown filter
- Combined search and filter working simultaneously
- No-results state with message

Game Detail Page
- Full game information display 
- Reviews section visible to all visitors
- Comments section visible to all visitors
- Empty state messages when no reviews or comments exist yet

Game Management
- Add game form with all relevant fields including cover image upload
- Edit game form pre-populated with existing data
- Delete game with confirmation step
- Ownership checks ensuring only the adding user can edit or delete
- Success and error messages for all actions

Personal Library
- Add any game to personal library from the game detail page
- Choose Owned or Wishlist status when adding
- Duplicate prevention with helpful messaging
- Library page showing all entries with status clearly displayed
- Remove game from library with confirmation step
- Empty state for library with prompt to browse

Reviews and Ratings
- Star rating submission (1–5) with written review body
- One review per user per game enforced
- Edit and delete own review
- Average rating calculated and displayed on game cards and detail page
- Login prompt shown to visitors in place of the review form

Comments and Review Replies
- Post a general comment on any game's detail page
- Reply directly to an individual review
- Comments and replies displayed in chronological order with username and date
- Edit and delete own comments and replies
- Login prompt shown to visitors in place of comment form
- Success messages for all comment and reply actions

Library Filtering
- Filter library entries by All, Owned or Wishlist status

User Feedback and Access Control
- Flash messages confirming every create, update and delete action
- Clear validation error messages on all forms

Custom 404 Page
- Branded 404 error page matching site design
- Clear link back to the home page

Deployment
- Application deployed to a cloud platform
- Environment variables used for all secret keys
- No secrets or commented out code in the repository

(W) Social and Community Features
- Follow and unfollow other users
- Activity feed showing content from followed users
- Public user profile pages
- User display name and bio editing
- Personalised game recommendations based on library contents

### Database Schema

![Database Schema](/README_images/db_schema.jpg)

By making the Comment column review_id nullable, we can use the null value to apply the comment on a game in general rather than a specific review.

I have created 5 database tables for the features that I want to implement. I am using one of Django's built in 'User' table.

### wireframes



### surface

For the project I want a clean design, dark greys with brighter accent colours(gold/amber) and warm rich colours(green/red) for tags and feedback messages. Final colours to be picked later on.


### Dependencies
default Dango dependencies:
asgiref==3.11.1
Django==6.0.3
sqlparse==0.5.5

For deploying on heroku:
gunicorn==25.3.0
packaging==26.0

Allows us to interact with the DB in Python:
psycopg==3.3.3

Allows Django to connect to our DB using a URL:
dj-database-url==3.1.2


### Deployment
I took steps to deploy at the earliest opportunity by just outputting a simple message as a string as our first basic html response.