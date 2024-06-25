# axis_bulkImporter
Convert UI json objects to Bulk-Import templates

Use this tool to create bulk import csv files for import to the Axis portal.  
Source data by default is the Applications json data file taken from the UI via browser debug tools

This tool can be imported to any other python script/tool to parse source data
into the correct schema necessary for bulk import.

Example - Migrating applications from one tenant to another, or customer, or service.

Requirement:
* Source data in json format.  
