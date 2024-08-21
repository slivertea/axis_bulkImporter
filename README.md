# axis_bulkImporter
Convert UI json objects to Bulk-Import templates<br>
_Currently only supports network ranges._ <br>
_Currently does not support new-tenant Zone mapping or detection.  This is manual_

## Use Cases
Example - Migrating applications from one tenant to another

* Use this tool to create bulk import csv files for import to the Axis portal.  
Source data by default is the Applications json data file taken from the UI via browser debug tools

* This tool can be imported to any other python script/tool to parse source data
into the correct schema necessary for bulk import.


## Limitations
1. Currently only supports network ranges
2. Any RnD Customizations are not supported.
3. Web App and custom redirect, nonce support, or custom header pass through are not supported in this script.



## Requirements:
* Source data in json format.  From UI
* Connector Zones in "new tenanat", or the "upload tenant" mapped correctly.  
