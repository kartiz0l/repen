from pathlib import Path

import cv2 as cv
import matplotlib.pyplot as plt
import pandas as pd
from repen import Report

# Create a report
report = Report(title="Sales Analysis Q4 2023")

# Add content - Repen automatically adapts different data types
report.add("# Executive Summary")
report.add("Monthly sales performance with **key metrics** and trends.")

# Add metrics
report.add(
    {
        "Revenue": ("$1.2M", "USD", "highlight"),
        "Growth": ("15.2%", None, "success"),
        "Customers": (1250, "active", "default"),
    }
)

# Add a pandas DataFrame
df = pd.DataFrame(
    {
        "Month": ["Oct", "Nov", "Dec"],
        "Sales": [350000, 420000, 430000],
        "Growth": ["12%", "20%", "2.4%"],
    }
)
report.add(df)

# Add a matplotlib figure
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [350, 420, 430])
ax.set_xlabel("Month")
ax.set_ylabel("Sales (K)")
ax.set_title("Sales Trend")
report.add(fig)

# OpenCV
cv_image = cv.imread(str(Path(__file__).parent / "basic_image.png"))
report.add(cv_image)

# Render and save
report.save("sales_report.html")
