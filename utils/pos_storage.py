import os
from datetime import datetime
import pandas as pd

def record_transaction(order_id, item_name, modifier, qty, unit_price, mod_price, payment_method, storage_dir="data_cache"):
    """
    Dynamically generates or appends a transaction log entry into a 
    CSV file segregated by the active day.
    """
    # 1. Fetch current timestamp metrics dynamically
    now = datetime.now()
    current_date_str = now.strftime('%Y-%m-%d')
    timestamp_str = now.strftime('%Y-%m-%d %H:%M:%S')
    
    # 2. Complete financial line math automatically
    total_unit_price = float(unit_price) + float(mod_price)
    line_total = total_unit_price * int(qty)
    
    # 3. Structure standard log record line matching your schema
    new_record = {
        "OrderID": [order_id],
        "Timestamp": [timestamp_str],
        "ItemName": [item_name],
        "Modifier": [modifier],
        "Quantity": [int(qty)],
        "UnitPrice": [float(unit_price)],
        "ModifierPrice": [float(mod_price)],
        "TotalUnitPrice": [total_unit_price],
        "LineTotal": [line_total],
        "PaymentMethod": [payment_method]
    }
    
    new_df = pd.DataFrame(new_record)
    
    # 4. Construct path and write or append data seamlessly
    os.makedirs(storage_dir, exist_ok=True)
    target_csv_path = os.path.join(storage_dir, f"sales_{current_date_str}.csv")
    
    # Check if the file exists for the day to determine header insertion rules
    file_exists = os.path.exists(target_csv_path)
    
    # Append the row smoothly to disk
    new_df.to_csv(target_csv_path, mode='a', index=False, header=not file_exists)
    return target_csv_path
