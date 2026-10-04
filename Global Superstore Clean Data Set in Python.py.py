import pandas as pd

#==================================================
#1. Load Data
#==================================================

Orders = pd.read_csv(r"C:\Users\Admin\OneDrive\Desktop\Global Superstore.csv")

print("Original Data:")
print(Orders.head())

print("\nOriginal Shape:")
print(Orders.shape)


#==================================================
#2. Check Missing Values
#==================================================

print("\nMissing Values before Cleaning:")
print(Orders.isnull().sum())


#==================================================
#3. Check Duplicate Rows
#==================================================

print("\nDuplicate rows before cleaning:")
print(Orders.duplicated().sum())


#==================================================
#4. Remove Extra spaces from text columns
#==================================================

text_columns = [
    "Order ID",
    "Ship Mode",
    "Customer ID",
    "Segment",
    "City",
    "Country",
    "Market",
    "Region",
    "Product ID",
    "Category",
    "Sub-Category",
    "Product Name"
]

for column in text_columns:
    Orders[column] = Orders[column].astype(str).str.strip()


#==================================================
#5. Clean Postal Code
#==================================================

Orders["Postal Code"] = Orders["Postal Code"].astype(str).str.strip()

print("\nMissing Postal Codes:")
print(Orders["Postal Code"].isnull().sum())


#==================================================
#6. Remove completely duplicate rows
#==================================================

Orders = Orders.drop_duplicates()

print("\nDuplicate rows after cleaning:")
print(Orders.duplicated().sum())


#==================================================
#7. Convert Date columns to date format
#==================================================

Orders["Order Date"] = pd.to_datetime(
    Orders["Order Date"],
    errors="coerce"
)

Orders["Ship Date"] = pd.to_datetime(
    Orders["Ship Date"],
    errors="coerce"
)


#==================================================
#8. Check Numeric Columns
#==================================================

numeric_columns = [
    "Row ID",
    "Sales",
    "Quantity",
    "Discount",
    "Profit",
    "Shipping Cost"
]

for column in numeric_columns:
    Orders[column] = pd.to_numeric(
        Orders[column],
        errors="coerce"
    )


#==================================================
#9. Check important categorical values
#==================================================

print("\nShip mode Values:")
print(Orders["Ship Mode"].unique())

print("\nSegment Values:")
print(Orders["Segment"].unique())

print("\nCategory Values:")
print(Orders["Category"].unique())

print("\nMarket Values:")
print(Orders["Market"].unique())

print("\nRegion Values:")
print(Orders["Region"].unique())


#==================================================
#10. Check duplicate Order IDs
#==================================================

print("\nDuplicate Order IDs:")
print(Orders["Order ID"].duplicated().sum())

# IMPORTANT:
# We are NOT deleting duplicate Order IDs because
# one order can contain multiple products.


#==================================================
#11. Check Missing Values after cleaning
#==================================================

print("\nMissing Values after cleaning:")
print(Orders.isnull().sum())


#==================================================
#12. Check datatypes after cleaning
#==================================================

print("\nData Types After Cleaning:")
print(Orders.dtypes)


#==================================================
#13. Check final shape
#==================================================

print("\nFinal Shape:")
print(Orders.shape)


#==================================================
#14. Display Cleaned Data
#==================================================

print("\nCleaned Data:")
print(Orders.head())


#==================================================
#15. Save Cleaned Data
#==================================================

Orders.to_excel(
    r"C:\Users\Admin\OneDrive\Desktop\Global Superstore_Cleaned.xlsx",
    index=False
)

print("\n======================================")
print("Cleaning Completed Successfully!")
print("File saved as: Global Superstore_Cleaned.xlsx")
print("======================================")
