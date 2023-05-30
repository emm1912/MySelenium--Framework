# MySeleniumAutomation-Framework V1.0 23-MAY-2023
###### Note. In branch "experiments" you will find that the html-report maker is working, you will find some new methods, one more automation example and now you can select which browser you want to use from the cli.
Well in the search of having a broader view in the the world of software development, a very good friend of mine recommended me to investigate about software automation and more 
precisely to search about "Selenium" and "Postman" (this last one, as I have also been using django lately to make some simple API's applications), so after researching
and reading a lot of info/documentation I came to the conclusion that I needed to build a selenium Framework, first and foremost to simplify the automation of test's.
So here is my Selenium Framework, I built it with the help of several sources (official documentation, videos, guides).

So dear reader, feel free to check it out and modify it if necessary.

## Description

First of all you need to clone the project to your local machine. Once there you will find the "requirements.txt" to create your virtual environment and install the needed
modules for this framework to work. For this project I used PyCharm as IDE, but dear reader you are welcome to use any IDE that fit your needs.

Next, the structure of the project:


<code>
├── configurations
│   └── config.ini
├── geckodriver.log
├── logs
│   └── automation.log
├── main.py
├── pageObjects
│   ├── base_element.py
│   ├── base_page.py
│   ├── geckodriver.log
│   ├── __init__.py
│   ├── locator.py
│   ├── LoginPage.py
│   └── __pycache__
├── README.md
├── reports
├── requirements.txt
├── screenshots
│   └── test_homepageTitle.png
├── testcases
│   ├── conftest.py
│   ├── geckodriver.log
│   ├── LoginDataDrivenTest.py
│   ├── __pycache__
│   ├── pytest.ini
│   └── test_login.py
├── testdata
│   └── Book1.xlsx
└── utilites
    ├── chromedriver.exe
    ├── customlogger.py
    ├── __init__.py
    ├── __pycache__
    ├── readProperities.py
    └── XLUtils.py
</code>


### Folder description

#### Configurations:
Here you can modify the .ini file where you can store user's, password's and some other usefull data necessary to run the test's, some scripts use this data to do their
work.
#### Log: 
The folder where the custom logger saves the messages we wrote in our code.
#### PageObjects: 
Here you will find scripts with the written method's that help us automate faster and easier.


* base_page.py		Here you will find the methods that can help us navigate a web page.
Like `forward` `back` `scrolldown` also the `go` method to tell the driver go fetch the url we want etc. More about this later....


* base_element.py		Here you will find the methods that help us fetch objects from the webpage, also send text and click things.
Like `find` `input_text` `click` also the `text`. More info keep reading.


* locator.py			Here is a single method, that facilitate the input of the arguments that the base_element methods need (nothing fancy just a namedtuple).


* LoginPage.py		And lucky last one, this one describes the login webpage "https://admin-demo.nopcommerce.com/" thata we are (in this example) using as a 
test playground.


#### Screenshots: 
This is the folder where the screenshots are saved (in png format).

#### Testcases: 
Here you can find the test's that we wrote and a "conftest.py" script that help us setup the webdriver.

#### Testdata: 
Here you will find the xlsx used to do ddt (the Book1.xlsx archive has some "users" and "passwords" to be test in the login page).

#### Utilites: 
Here are the scripts that have the necessary code to make work the custom logger, the readconfig method (to load the data from the .ini document) and the xlsx document
reader.

###### Note. There might be some other files inside this folders, but the most important info is the one here described.

## How to use? -> Here is an intro on how to use this framework <- 

Inside the "pageObjects" folder you will find the script "LoginPage.py", this script describes some actions we want to do in our playground login page, so you will
have to do some similar script for your particular case, then you create the "test_example.py" using this method's to perform the test (as you probably already know).

The idea of the method's within the "base_page.py" script is to let us do actions that we perform when we use a web browser (btw here is where you can add more functionality
to perform more browser actions), this is how you write this method's.

* Go back:

`self.lp.back()`

* Go forward:

`self.lp.forward()`

* Refresh the page:

`self.lp.refresh()`

* Scroll all the way down (to the bottom of the page):

`self.lp.scroll_downpage()`

* Quit the page:

`self.lp.quit()`

* Close the page:

`self.lp.close()`

* Maximize the window:

`self.lp.maximize_window()`

* Minimize the window:

`self.lp.minimize_window()`

* Make a screenshot (this method always save's the images inside the "screenshots" folder):

`self.lp.getscreenshotasFile(name)`

* Get the title of the window (don't forget to save it into a variable):

`self.lp.getTitle()`

* Get the source of the page (don't forget to save it into a variable):

`self.lp.getpageSource()`

###### Remeber that you can add more functionality if you need to.

Ok now here are the method's within the "base_element.py" script, and how to write them

* How to find an element, using the BaseElement(driver, locator) method.

We need to give it a driver and a "locator" (the namedtuple we talked above) that contains how the driver is going to search the element and what is going to search.
The driver is generated and given to it when use the "setup" method.
###### For a full example please check the script LoginPage.py

`locator = Locator(By.ID, "Email")`
`setuname = BaseElement(self.driver, locator)`

[Here you can find a list of By's you can use](https://selenium-python.readthedocs.io/locating-elements.html)

* How to input text once we found the element.

`setuname.input_text("Text to be send")`

* How to click an item, we need to find the element first.

`locator = Locator(By.XPATH, "//button[@type='submit']")`
`login_btn = BaseElement(self.driver, locator)`

Then we click it.

`login_btn.click()`

* Get an attribute.

`attr_locator = "@value"`
`attr_value = attr_element.attribute(attr_locator)`

* Lets suppose we want the text value from a button, well then we would do the following after we find the element (notice that we dont need the parenthesis at the end):

`text_value = login_btn.text`

* Lastly we can write to the log like this.
	
`self.logger.info("HERE WRITE A MESSAGE YOU WANT TO BE SAVED IN THE LOGS")`

> With all this in mind you can make your own "LoginPage.py" and then create your "test_example.py" and start automating.


> DISCLAIMER, by no means I'm an expert in automation, but in my opinion this is a good enough framework to build upon.

## Links used to build this framework.

###### Selenium info links
1. [Selenium Documentation](https://www.selenium.dev/selenium/docs/api/py/api.html)
2. [Page Objects](https://selenium-python.readthedocs.io/page-objects.html)
3. [Locating Elements](https://selenium-python.readthedocs.io/locating-elements.html)

###### HTML report generator implementation/info
[Youtube video](https://www.youtube.com/watch?v=DpfLjB84EQU&list=PLZMWkkQEwOPkFsyal6Uq3RvAGsBbLCfZV&index=10)

###### What is Selenium and its Components
[Youtube video](https://www.youtube.com/watch?v=nvrXp13eiCU)