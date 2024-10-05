def get_sorted_customers(customers):
    result = []
    for customer in customers:
        combined_name = customer['FIRST_NAME'] + customer['LAST_NAME']
        if len(combined_name) < 12:
            result.append({
                "ID": customer["ID"],
                "FIRST_NAME": customer["FIRST_NAME"],
                "LAST_NAME": customer["LAST_NAME"],
                "COMBINED_NAME": combined_name
            })
    
    result.sort(key=lambda x: (len(x["COMBINED_NAME"]), x["COMBINED_NAME"].lower(), x["ID"]))
    return result


