# utils/file_handler.py
import os

def save_menu_to_file(menu_text, filename="extracted_menu.txt"):
    """
    Saves the extracted menu text into a file inside the 'output' directory.
    """
    # Define the output directory path (one level up from utils)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(base_dir, "output")
    
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")
        
    file_path = os.path.join(output_dir, filename)
    
    # Write the contents to the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(menu_text)
        
    print(f"Successfully saved menu data to: {file_path}")
    return file_path
