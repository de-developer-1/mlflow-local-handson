import pandas as pd

df = pd.DataFrame({
    "feature1": range(100),
    "feature2": range(100, 200),
    "label": [1 if x % 2 == 0 else 0 for x in range(100)]
})
df.to_csv("data/raw/sample.csv", index=False)
print("Sample data saved to data/raw/sample.csv")
