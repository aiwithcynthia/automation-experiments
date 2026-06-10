# Excel Automation Demo
# Created by Cynthia Perez

import pandas as pd

data = {
    "Client": ["Client A", "Client B", "Client C"],
    "Status": ["Complete", "Pending", "In Progress"],
    "Priority": ["High", "Medium", "High"]
}

df = pd.DataFrame(data)

print("Automation Report")
print(df)

high_priority = df[df["Priority"] == "High"]

print("\nHigh Priority Items:")
print(high_priority)
