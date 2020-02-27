# This imports the Service Map Results from a CSV file and removed the standard connections

import csv
from os import system
system("cls")
filename = input("Enter the file name you would like to process: ")
try:
    with open(filename, mode="r") as fr, open(f"{filename}_result.csv", mode="x") as fout:
        #reader = csv.reader(f, delimiter=",")
        reader = csv.DictReader(fr)
        field_names = ['ï»¿Computer', 'ProcessName', "Direction", "SourceIp", "DestinationIp", "DestinationPort", "Protocol", "Remote"]
        writer = csv.DictWriter(fout, fieldnames=field_names)
        counter = 0

        for row in reader:
            if row['Direction'] == 'outbound' and row['DestinationIp'][:2] != "10":
                if row['SourceIp'] != row['DestinationIp']:
                    if row['ProcessName'] not in ("svchost", "HealthService", "wmiprvse", "oneagentos", "policyHost", "oneagentloganalytics", "System", "mcdatrep", "activeconsole", "ccmsetup"):
                        
                        writer.writerow(row)
                        counter += 1
        print("=" * 80)
        print(f"Writen {counter} rules to {filename}_result.csv")
        print("=" * 80)
except:
    print("=" * 125)
    print(f"\tFile '{filename}_result.csv' already exists or the filename is incorrent\n\tPlease remove or rename the old file before trying again!")
    print("=" * 125)
