# Tax Account Validation Demo

accounts = [
    {"state": "NJ", "account": "123456", "valid": True},
    {"state": "PA", "account": "", "valid": False},
]

for account in accounts:
    if not account["valid"]:
        print(f"Missing account for {account['state']}")
