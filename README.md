# milestone-project-3: Board Silly

## UX

### Project goals
To design and implement a well structured database, embedded in a fully functional full stack web app.

### User stories
User Story 1:
As a visitor, I want to be able to register for an account and log in and out so that my library and content are personal to me.

Acceptance Criteria:

User Story 2:
As a visitor, I want to browse all games and search or filter by title and category so that I can find what I am looking for quickly.

Acceptance Criteria:


User Story 3:
As a visitor, I want to view the full details of a game including its stats, reviews and comments so that I can learn as much as possible about it before adding it to my library.

Acceptance Criteria:


User Story 4:
As a logged-in user, I want to be able to add new games to the catalogue and manage ones I have added so that the catalogue stays accurate and up to date.

Acceptance Criteria:


User Story 5:
As a logged-in user, I want to add games to my personal library with a status of Owned or Wishlist, view my collection and remove games I no longer want tracked.

Acceptance Criteria:


User Story 6:
As a logged-in user, I want to write a star rating and review for games I have played so that I can share my opinion with other users.

Acceptance Criteria:


User Story 7:
As a logged-in user, I want to leave a comment on a game's detail page or on a specific review so that I can share quick thoughts, ask questions or respond directly to what another user has said.

Acceptance Criteria:


User Story 8:
As a user, I want to receive clear feedback after every action I take and feel confident that my content is protected from other users.

Acceptance Criteria:


User Story 9:
As a logged-in user, I want to filter my library by Owned or Wishlist so that I can focus on one part of my collection at a time.

Acceptance Criteria:


User Story 10:
As a user, I want to see a helpful branded page if I navigate somewhere that does not exist rather than a confusing generic error.

Acceptance Criteria:


User Story 11:
As a registered user, I want to follow other users and view public profiles so that I can discover games through people with similar tastes.

Acceptance Criteria:


User Story 12:
As a logged-in user, I want to receive game recommendations based on my library so that the experience feels richer and more personalised.

Acceptance Criteria:

User Story 13:
As a developer, I want the finished application deployed to a cloud platform so that it is accessible to anyone with the link.

Acceptance Criteria:


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