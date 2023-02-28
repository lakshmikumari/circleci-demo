import pandas as pd
import json

def Add(a,b):
    return a+b

def Hello():
    print("Hello Luck, 2.0")


def parseExcel():
    excel_data_df = pd.read_excel('Alerts.xlsx', sheet_name='UCSAlerts', skiprows=range(0, 4), engine='openpyxl')
    json_str = excel_data_df.to_json(orient='records')
    parsed = json.loads(json_str)
    with open('Alerts.json', 'w') as f:
        f.write(json.dumps(parsed,indent=2))

    fault_df = pd.read_json('Alerts.json')
    fault_df = fault_df[fault_df.Severity != 'cleared']
    al_str=fault_df.to_json(orient='index')
    al =  json.loads(al_str)

    with open('AlertsNoCleared.json', 'w') as f:
        f.write(json.dumps(al,indent=2))

if __name__ == '__main__':
    parseExcel()
