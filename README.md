##MyFreq!
###Intro
MyFreq! is a website that performs simple freqency analysis on a user-supplied text document.
The website is build in python/Django. Please check the requiremnets.txt file for the needed packages. You can use virtualenv to set up the environment based on the requirements file.
###Solution
This web would repeatly store the user-supplied file in uploaded/temp. Then get all the contents through 'stemming'(https://pypi.python.org/pypi/stemming/1.0), which will return the 'source' of the word.(e.g "talk", "talked", "talking" ould all count as "talk"). And the website will shows the top 25 mostly frequently used word in the file.
###To do in future
For now, this website doesn't have any security function, and only supports .txt or other plain text file. So if work still goes on, I would complete these two functions.

Github: https://github.com/JinSun2014/MyFreq
