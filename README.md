# Meme Generator
Pretty simple python app runed either by CLI or Flask Web Application.

My **meme** I mean a picture with some text place at a **random** position on the picture.


# How to run
##### Flask Web App
$ `cd path/to/project`
In this case the app.py is located in the root folder
$ `export FLASK_APP=hello.py`
$ `flask run`

##### Or run in by CLI
For direct help in the CLI:
$ `python meme.py -h`
For a custom meme:
$ `'python meme.py -p 'path/to/an/image -b 'Body of the text' -a 'Author Name'`

Or simply run `python meme.py` with no argument to get a randomly picture from  **data/photos** folder, with a random quote from one of the 4 different input files **docx, pdf, txt, csv**.

##### My experience
I had the task to implement the imported engine module, the meme generator engine and wire evertything together while learning python subprocces,  docx, panda, pillow, os and other modules. Work with images and drawing. Adding everything to the Flask appliction which needs knowledge in http protocols, requests's python module and Flask's requests. Overall, fun project. 


**Note: I don't know how to solve this, when pressing random or creating new picture, Ctrl + F5 have to be pressed to clear the cache**
