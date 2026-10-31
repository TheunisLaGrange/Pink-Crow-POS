import os

def save_to_txt(data_list, output_path="output.txt"):
    """
    Saves a list of strings to a specified text file.
    Each item in the list is written on a new line.
    """
    # Ensure the directory path exists
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        for line in data_list:
            f.write(f"{line}\n")
    print(f"Successfully saved {len(data_list)} records to {output_path}")
