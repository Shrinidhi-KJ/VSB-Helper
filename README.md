# PESUACADEMY-AUTO-LOGIN
Automatically logs onto PESUACADEMY website and goes to courses section for semester of choice.
Uses selenium.

## Download the zip file and extract to any location of your choice

## Prerequisites  
  
 - Python3 ([Download](https://www.python.org/downloads/))  
 
## Configuration options  

 - **myuser/mypwd:**
  The username and password of your pesuacademy profile.

- **sleep_time:**  
  Set to 1 if you're running on fast internet speed.
  Set to higher values such as 3 on slower internet speeds.
  This is the time it waits for the page to load before acting upon it.
  If a page stops before reaching the **courses** page, increase sleep_time.

- **semester:**  
Choose the semester you require. eg: 'Sem-1' or 'Sem-2' or 'Sem-3' or 'Sem-4' and so on.

- **browser_type:**  
Choose which browser you want to run it on. You may even choose one which you don't have on your laptop. : "msedge" or "chrome"  or "firefox"

## Run the script

 1. Open Pesu.py in an editor. Edit the variables under "set variables here" to your preference.
 2. Install dependencies:   ```pip install -r requirements.txt```
 3. Run [Pesu.py](Pesu.py): `python Pesu.py`
 4. After starting, do not click anything until the page loads onto courses page. In case it did not reach here, try changing the sleep_time to a higher value to accomodate for slower internet. 
 5. If code ran properly once. You can choose to right click on python file, and click create shortcut. Move this shortcut onto your desktop for a very easy shortcut to pesuacademy courses:) All you have to do is double click on the shortcut!
 
 EXTRA: If you want your shortcut to look nice, download this image :https://play-lh.googleusercontent.com/5OUK2rqyCA1rVe_NHjXZiKJ2HficO5PC7fmwP62LHusOc6iu0lYVhYb1ZkBaOg5B9_KP
  ![alt text](https://github.com/siddharthp02/PESUACADEMY-AUTO-LOGIN/blob/master/pesu.png?raw=true)
 
 Go to this website and convert it into an icon(ICO) : https://icoconvert.com/
 
 Right click on your shortcut -> select properties -> select change icon -> click on browse and choose your icon.
 
 VOILA! YOU'RE SET!
 
 ![alt text](https://github.com/siddharthp02/PESUACADEMY-AUTO-LOGIN/blob/master/SHORTCUT.JPG?raw=true)
 
## PS:
Extra functionality for future use: Creates a file called topics.txt with every topic in every sem in your directory. It's pretty cool to see:)

To run: Uncomment line 92 : write_topics_to_file()
As long as the file is empty, it will iterate through semesters and get every topic.

## Enjoy your easy shortcut! :)
