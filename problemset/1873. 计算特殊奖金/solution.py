import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    ans = pd.DataFrame({
        "employee_id": employees["employee_id"],
        "bonus": employees["salary"] * (employees["employee_id"] % 2 & ~employees["name"].str.startswith("M"))
    })
    
    ans = ans.sort_values("employee_id");
    
    return ans;
