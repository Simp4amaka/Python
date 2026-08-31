DATA_FILE = "bank_data.txt"
def load_data():
    try: 
        file = open(DATA_FILE, 'r') 
        lines = file.readlines()     
        file.close()
        name = lines[0].strip()
        balance = float(lines[1].strip())
        expenses = []
        for line in lines[2:]:
            description, category, amount = line.strip().split("|")
            expenses.append({
                "description": description,
                "category": category,
                "amount": float(amount)
                })
        return name, balance, expenses
    except FileNotFoundError:
        return None, 0, []
    except Exception as error:
        print("Error loading data:", error)
        return None, 0, []