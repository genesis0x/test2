import pandas as pd

def csv_to_excel(csv_file, excel_file):
  """
  Converts a CSV file to an Excel file.

  Args:
    csv_file: The path to the CSV file.
    excel_file: The path to the output Excel file.
  """

  # Read the CSV file into a pandas DataFrame
  df = pd.read_csv(csv_file)

  # Write the DataFrame to an Excel file
  df.to_excel(excel_file, index=False)

if __name__ == "__main__":
  csv_file = "N-List.csv"
  excel_file = "Nursery.xlsx"
  csv_to_excel(csv_file, excel_file)
  print("CSV file converted to Excel successfully!")