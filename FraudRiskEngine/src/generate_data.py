import os
import random
import pandas as pd
from datetime import datetime, timedelta

def generate_accounts():
    devices = ["iPhone", "Android", "MacBook", "Windows", "Tablet"]
    locations = ["NY", "CT", "CA", "TX", "FL", "NJ"]
    foreign_locations = ["RU", "CN", "UK"]

    accounts = []

    for i in range(10):
        account = {
            "account_id": f"acct_{i+1}",
            "home_location": random.choice(locations),
            "usual_devices": random.sample(devices, 2),
            "avg_amount": random.choice([40, 60, 85, 120, 175, 220]),
            "avg_velocity": random.choice([1, 2, 2, 3]),
            "account_age_days": random.randint(180, 2500)
        }
        accounts.append(account)

    return accounts


def choose_fraud_accounts(accounts):
    """
    Pick only a few accounts to contain fraud.
    Most accounts will have zero fraud transactions.
    """
    fraud_plan = {}

    # randomly choose 3 accounts total to have fraud
    fraud_accounts = random.sample(accounts, 3)

    # one account gets slightly more fraud
    fraud_plan[fraud_accounts[0]["account_id"]] = random.randint(4, 6)

    # the other two get only a small amount
    fraud_plan[fraud_accounts[1]["account_id"]] = random.randint(1, 3)
    fraud_plan[fraud_accounts[2]["account_id"]] = random.randint(1, 2)

    return fraud_plan


def generate_transactions(account, num_rows=150, fraud_count=0):
    rows = []
    current_time = datetime(2026, 1, 1, 8, 0, 0)

    fraud_indices = set(random.sample(range(num_rows), fraud_count)) if fraud_count > 0 else set()

    last_location = account["home_location"]

    for i in range(num_rows):
        fraud = 1 if i in fraud_indices else 0
        tx_time = current_time + timedelta(minutes=i * random.randint(8, 20))

        if fraud:
            amount = round(random.uniform(account["avg_amount"] * 4, account["avg_amount"] * 12), 2)
            location = random.choice(["RU", "CN", "UK", "CA", "TX", "FL"])
            device = random.choice(["UnknownDevice", "NewPhone", "UnrecognizedLaptop"])
            velocity = random.randint(5, 12)
            failed_logins = random.randint(2, 6)
            merchant_risk = round(random.uniform(0.75, 0.99), 2)
            new_device = 1
            location_change = 1
        else:
            amount = round(random.gauss(account["avg_amount"], account["avg_amount"] * 0.25), 2)
            amount = max(3.00, amount)

            if random.random() < 0.88:
                location = account["home_location"]
            else:
                location = random.choice(["NY", "CT", "CA", "TX", "FL", "NJ"])

            device = random.choice(account["usual_devices"])
            velocity = max(1, int(random.gauss(account["avg_velocity"], 0.5)))
            failed_logins = random.choice([0, 0, 0, 1])
            merchant_risk = round(random.uniform(0.05, 0.35), 2)
            new_device = 0
            location_change = 1 if location != last_location else 0

        row = {
            "account_id": account["account_id"],
            "timestamp": tx_time.isoformat(),
            "amount": amount,
            "location": location,
            "device_type": device,
            "transaction_velocity": velocity,
            "is_foreign_transaction": 1 if location in ["RU", "CN", "UK"] else 0,
            "location_change_since_last_tx": location_change,
            "new_device_used": new_device,
            "failed_login_attempts": failed_logins,
            "merchant_risk_score": merchant_risk,
            "account_age_days": account["account_age_days"],
            "amount_vs_avg": round(amount / account["avg_amount"], 2),
            "time_of_day": tx_time.hour,
            "fraud": fraud
        }

        rows.append(row)
        last_location = location

    return pd.DataFrame(rows)


def main():
    random.seed(42)
    os.makedirs("data/raw", exist_ok=True)

    accounts = generate_accounts()
    fraud_plan = choose_fraud_accounts(accounts)

    all_data = []
    summary = []

    for account in accounts:
        fraud_count = fraud_plan.get(account["account_id"], 0)

        df = generate_transactions(account, num_rows=150, fraud_count=fraud_count)

        file_path = f"data/raw/{account['account_id']}_transactions.csv"
        df.to_csv(file_path, index=False)

        print(f"Created: {file_path} | fraud transactions: {fraud_count}")

        all_data.append(df)

        summary.append({
            "account_id": account["account_id"],
            "home_location": account["home_location"],
            "usual_devices": ", ".join(account["usual_devices"]),
            "avg_amount": account["avg_amount"],
            "avg_velocity": account["avg_velocity"],
            "account_age_days": account["account_age_days"],
            "fraud_transactions": fraud_count,
            "total_transactions": len(df)
        })

    combined_df = pd.concat(all_data, ignore_index=True)
    combined_df.to_csv("data/raw/all_accounts.csv", index=False)

    summary_df = pd.DataFrame(summary)
    summary_df.to_csv("data/raw/account_summary.csv", index=False)

    print("\nCreated combined dataset: data/raw/all_accounts.csv")
    print("Created account summary: data/raw/account_summary.csv")
    print("\nOverall fraud counts:")
    print(combined_df["fraud"].value_counts())


if __name__ == "__main__":
    main()