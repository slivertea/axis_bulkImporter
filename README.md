# axis_bulkImporter
Convert UI json objects to Bulk-Import templates<br>
_Currently only supports network ranges._

## Use Cases
Example - Migrating applications from one tenant to another

* Use this tool to create bulk import csv files for import to the Axis portal.  
Source data by default is the Applications json data file taken from the UI via browser debug tools

* This tool can be imported to any other python script/tool to parse source data
into the correct schema necessary for bulk import.



## Requirements:
* Source data in json format.  From UI
