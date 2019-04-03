# MembersListPlot
This Python code can be used to plot coordinates on a map corresponding to each HVDSA member's address (approximately, in most cases).

Work flow for installation of the necessary packages:
1. Install anaconda. https://www.anaconda.com/distribution/
2. Once anaconda is installed, open up the "anaconda prompt" in Windows and type "pip install geopy"
3. Sign up for an OpenMapQuest API key through https://developer.mapquest.com/. The resulting API key will be used in the Python code. It's free below 15,000 address requests per month.
4. In the anaconda prompt, type: "conda install folium -c conda-forge"

Download the .py files from the repository. These files are ideally run as Jupyter notebooks, which can be found in Windows by typing in "Jupyter notebook".
1. Generating member list coordinate file and plotting coordinates.py
Generates a new .xlsx (Excel file) from a spreadsheet that is copied from AirTable or any other spreadsheet program/app. Should be used each time a new members list is generated. Also plots the points at the end of the notebook.
The .xlsx file that is generated has three new columns: latitude, longitude, and goodOrBad. If the address lookup fails, the goodOrBad column will be "False".

2. Plot HVDSA member list.py
Imports a pre-generated coordinate file created using the previous .py file. Should be used on a normal basis just for accessing the data, rather than generating a new .xlsx file.

Important information about data formatting:
spreadsheet headers should at least include (pay attention to upper and lower casing)
first_name, last_name, Address_Line_1, City, Zip
