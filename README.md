# Flask Forms with Images

## Objective: 
In this lab, you will learn about incorporating user image uploads to directories with firebase and displaying them... by adding to your very own meet channel!  

By the end of this lab, you will have a profile with images your users uploaded.  

> Before we start, make sure to fork the repo, and clone the code to your machine.


## Instructions:

In this lab, we'll be creating our very own meet profile with your users uploading the images!  
We have provided you with some frontend and backend code already, so make sure to clone the repo!  

1. Create and set up a new Firebase project:
    1. Go to https://console.firebase.google.com/
    2. Create a new project and name it whatever you'd like.
    3. Go to Realtime Database and create a database.
    4. Go to rules and change false to true.

2. Connect the Firebase project to your Flask app:
    1. In your Firebase project:
        - Go to project setting and create a web app.
        - Copy the firebaseconfig lines.
    2. In the app.py file:
        - Create a dictionary called config and paste the copied lines (make sure to fix the syntax errors).
        - Intialize the firebase using pyrebase.
        - Intialize db using the firebase object.

3. In `add_post.html`, you have a form that contains an input called caption and a submit button:
    - **Add** the required line to the form tag to be able to accept images.
    - **Add** an input that you can upload images to.
        
Now, after you're done with setting up the profile info, let's display our posts!  

3. In `main.py` theres a variable called `posts`, it's a dictionary that has image links as *Keys*, and post captions as *Values*!
    - Pass `posts` to `index.html`, and display each post correctly!
    - *Hint: hmmm.. how can we **loop** through these posts and show them on the page?*
    - *Feel free* to change the dictionary keys and values to create your own Instagram profile!


##### That's so cool! You have just created your first advanced flask application!
##### Call an Instructor/TA to check your completed tasks
 

If you have extra time, continue to the **Bonus Problems** *below*.  
If not, make sure you commit and push your code.


<img src="https://miro.medium.com/max/1200/1*SzN6u2U98S4RyhWo_WyaHQ.png" width="400">




## Bonus Problems: 
1. Fill in the **Social Media** icons with accessible links!
    - Make sure to **pass** the links variables and linking them correctly in `index.html`.
    
2. If you add too many posts, it'll start getting clunky and messy... try to fix it!
    - *Hint: maybe something like, say, every 3 posts on a row? or something like that.*

##### Great job on completing the bonus problems section!  
###### make sure you commit and push your code.


