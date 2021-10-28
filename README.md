# dmn2csv

Simple Python tool to generate a CSV file from a DMN file. <br>
This tool was built primarily for DMN files exported from Alfresco Process Services. 
It hasn't been tested with other DMN files.<br>
<br>

# Software requirements

Python version greater than 3.5 is required.

<br>

# How to use this tool

It is recommended to create a Python virtual environment before installing the requirements for this project. More info [here](https://realpython.com/python-virtual-environments-a-primer/). <br>
<br>

Install python requirements:<br>
`pip install -r requirements.txt`

<br>

In APS, export the decision table you need to analyse:
- go to `App Designer`-> `Decision Tables` tab
- click on the decision table you need
- click on the export icon. This will download locally the .dmn file.
 
 <br>

Run script `dmn-to-csv.py` and provide the .dmn file path as argument. For example:<br>
`python dmn-to-csv.py my-rules-file.dmn`

<br>

Using a relative or absolute path to a file in another folder will work too. If the .dmn file is not provided, the script will look for a default file name `rules.dmn` in the same folder as `dmn-to-csv.py`.

<br>

A new file named `rules.csv` will be generated. Import that file into excel, making sure you use character `|` as separator.