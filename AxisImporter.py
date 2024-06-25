import sys
import csv
import json
defaultsource = "example-source-ui.json"
defaultfilename = "bulk_import-NR.csv"
schemaNR = {
    'Name': None,
    'IP Ranges': None,
    'DNS Searches': None,
    'ICMP enabled (Optional)': None,
    'Allowed Ports & Protocols': None,
    'Connector Zone': None,
    'Tags (Optional)': None
}




def setNet(arg1):
    if "nativeIPRangesOrCIDRs" in arg1.keys():
        nets = ";".join(arg1["nativeIPRangesOrCIDRs"])
        return nets
    else:
        return None

def setDomain(arg1):
    if "nativeDnsSearches" in arg1.keys():
        domains = ";".join(arg1["nativeDnsSearches"])
        return domains
    else:
        return None

def setPorts(arg1):
    if "nativeTypedPortRanges" in arg1.keys():
        portList = []
        for range in arg1["nativeTypedPortRanges"]:
            port = range["range"]
            proto = range["protocol"].lower()
            if proto == "all":
                allPort = port
            else:
                allPort = port + ":" + proto
            portList.append(allPort)
        ports = ";".join(portList)
        return ports
    else:
        return None

def setZone(arg1):
    return arg1["connectorZone"]["name"]


def setTags(arg1):
    if "applicationGroups" in arg1.keys():
        taglist = []
        for tag in arg1["applicationGroups"]:
            taglist.append(tag["name"])
        tags = ";".join(taglist)
        return tags
    else:
        return None


def parse(argv):
    parseList = []
    for app in argv:
        dict = {
            'Name': None,
            'IP Ranges': None,
            'DNS Searches': None,
            'ICMP enabled (Optional)': None,
            'Allowed Ports & Protocols': None,
            'Connector Zone': None,
            'Tags (Optional)': None
        }
        if app["applicationProtocol"] == "Native" and app["applicationEntityType"] == "Legacy":
            dict["Name"] = app["name"]
            if app["isIcmpEnabled"]:
                dict["ICMP enabled (Optional)"] = 'true'
            else:
                dict["ICMP enabled (Optional)"] = 'false'
            dict["Connector Zone"] = setZone(app)
            dict['IP Ranges'] = setNet(app)
            dict['DNS Searches'] = setDomain(app)
            dict['Allowed Ports & Protocols'] = setPorts(app)
            dict['Tags (Optional)'] = setTags(app)

        parseList.append(dict)

    return parseList


def write(argv, filename=defaultfilename):
    with open(filename, 'w') as csvFh:
        writer = csv.DictWriter(csvFh, fieldnames=schemaNR.keys())
        writer.writeheader()
        writer.writerows(argv)


def main(argv):
    ### FIle Creation(s)
    # Dump the pareList array into the axis bulk import template for Network Ranges
    with open (defaultsource) as jf:
        appSource = json.load(jf)
    parsedList = parse(appSource)
    write(parsedList)


if __name__ == "__main__":
   main(sys.argv[1:])
