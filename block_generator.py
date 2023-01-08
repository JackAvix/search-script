from pandas import *

data = read_csv("job_list.csv")

jobs = data.iloc[:,0].tolist()

with open('blocked_companies.txt', 'w') as f:
    for line in jobs:
        f.write(f"www.linkedin.com##li:has-text({line})\n")

print("\nImport the 'blocked_companies.txt' file to the 'My filters' tab of Ublock Origin to block them from your Linkedin searches.")