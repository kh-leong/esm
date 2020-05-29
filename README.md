# esm
### How to setup
Make sure Python is installed (3.5.6 or above). If it isn't, go to https://www.python.org/downloads/ and download the latest version for your OS.
Once Python is installed, go to the root directory of the project.

    cd esm
If running on Mac/Linux, activate the virtual environment by running:

    source venv/bin/activate
Or if you're running on Windows:

    python -m venv venv #create the files for activating
    venv\Scripts\activate.bat
Once the virtual environment is running, your console will change to look something like this:

    (venv) $
    
Next, install all the required libraries by running:

    pip install -r requirements.txt

Once done, run the following command to start the server:

    python manage.py runserver

Then in your browser, go to http://localhost:8000/salary_mgmt/ to access the web app.