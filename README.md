# Kurius-Hacks-CE

## Hackathon project by Kyle Java and Neala Mendoza

## Inspiration

Our team wanted to build a platform that would give back to the community, we had a couple ideas on how to approach this. One idea that we thought would be great is for people to view food drives that are going around them, personally it is hard to find out when/where food drives are happening. We also wanted to find a way for people to post there own food drives going on, for example if a school wanted to promote their local food drive coming up but have no way to advertise it. That is when we thought of "From Me To You", a website that not only shows upcoming food drives, but allows organizers to display and show their food drives coming up.

## What it does

"From Me To You" is a web application that users can use to view food drives as well as let others know about their own food drives upcoming. When a user enters our website, they will be greeted by the frontpage, and can see a table of upcoming food drives happening. In the table, user's can see the name of the event, address of the event, date of the event, a small description of what it is about, and who to contact. On the bottom of the page, user's or food drive organizer's will be able to display their own upcoming food drives which will then be added to the table.

## How I built it

The front-end of the website was built using HTML, CSS, Javascript, and Bootstrap. The back-end of the website was built using Flask and Python. We were able to store and preview events by adding them to a MongoDB cluster.

## Challenges I ran into

In the original plan we wanted to use React to Flask, it spent our team 3 hours trying to connect React and Flask, but in the end we were unable to do it so we just had to stick with just HTML and CSS. We also had trouble figuring out a way to add data to the cluster as well as preview the update at the same time.

## Accomplishments that I'm proud of

We are proud that we were able to get the MongoDB cluster to work, since our team has not had much experience with that particular database. We also were proud that we were able to build a nice and clean UI of our website.

## What I learned

We learned how to build elegant and easy to use forms in HTML, since our team hasn't worked with user input that much when it came to websites. We also learned how to make the website more dynamic and have data update on the webpage as soon as an event was added.

## What's next for From Me To You
We want to implement a way for user's to filter through events, either by date or location. We also want to implement a way for an event to be deleted from the database as soon the current date passes the event date. 
