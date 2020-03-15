# Meme Generator
Pretty simple python app runed either by CLI or Flask Web Application.

My **meme** I mean a picture with some text place at a **random** position on the picture.


# How to run
##### Flask Web App
**Simply run the app.py file!**
$ `python app.py`

##### Or run in by CLI
For direct help in the CLI:
$ `python meme.py -h`
For a custom meme:
$ `'python meme.py -p 'path/to/an/image -b 'Body of the text' -a 'Author Name'`

Or simply run `python meme.py` with no argument to get a randomly picture from  **data/photos** folder, with a random quote from one of the 4 different input files **docx, pdf, txt, csv**.

##### My experience
I had the task to implement the imported engine module, the meme generator engine and wire evertything together while learning python subprocces,  docx, panda, pillow, os and other modules. Work with images and drawing. Adding everything to the Flask appliction which needs knowledge in http protocols, requests's python module and Flask's requests. Overall, fun project. 


# Use of files
- Utils.Loging.py: Simple loging class, prints colored text for visibility in the terminal
- UtilsMeme.MemeEngine: Contains the MemeGenerator class wich has one method make_meme which takes 3 parameters, the path to the image, the Quote object and the optional size of the result image, the methode place randomly the quote on the picture.
- UtilsQuote.Models: A fils to hold all the models, in this case, I have only a very simple one, the Quote with 2 fields, body and author
- UtilsQuote.QuoteEngine: A class which contains all the importers for csv, txt, docx and pdf, all called by one class Importer by need.
- meme.py is the file which handles and can be used to generate a meme via CLI
- app.py is the Flask Web Application, html can be found in /templates


**Note: I don't know how to solve this, when pressing random or creating new picture, Ctrl + F5 have to be pressed to clear the cache**
