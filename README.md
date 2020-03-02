# Database-Assignment3

## How to Run
> source activate.sh
> flask run
> Play around with the website at http://127.0.0.1:5000/

Collaborated with Caleb.

The application should be written in Python3 using the Flask web framework.
You should use SQLite as the database
This is so you can develop completely independently of being able to connect to a GCE instance or Google's network.
Basic HTML responses are fine (and encouraged). No CSS, javascript, or framework required.

#### Required functionality
###### Views
- List all sailors
- List all boats
- Given a boat (via name), list sailors who have sailed it
- Given a sailor (via name), list boats the sailors have sailed on
- Given a date, list sailors who have sailed on that day
- Given a boat color list sailors who have sailed on a boat of that color
- List the boats by order of popularity (number of voyages) from most popular to least
###### Mutations
- Page to add a sailor
- Page to add a boat
- Page to add a voyage
#### Grading
- 50% for a working python flask application that can serve at least one route
- 10% for connecting to the sqlite database
- 4% for each view and mutation (there are 10 views/mutations so if you implement them all you get 40% here).
#### Extra credit
- Demonstrate your use of version control to the TA (5%)
- Demonstrate your unit tests to the TA (10% max, awarded by the TA according to how well you tested your code. Poor testing could get you just 1%, great testing could get you 10%. Ask the TAs in advance for advice on unit tests)

