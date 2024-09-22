import pandas as pd

def remove_empty_rows(input_file, output_file):
    """
    Removes empty rows from an Excel file.

    Args:
        input_file: The path to the input Excel file.
        output_file: The path to the output Excel file.
    """

    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(input_file)

    # Drop rows with all NaN values
    df.dropna(how='all', inplace=True)

    # Write the cleaned DataFrame to a new Excel file
    df.to_excel(output_file, index=False)

if __name__ == "__main__":
    input_file = "test.xlsx"
    output_file = "cleaned_output.xlsx"
    remove_empty_rows(input_file, output_file)
    print("Empty rows removed successfully!")