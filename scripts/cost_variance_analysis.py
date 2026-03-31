import pandas as pd

def calculate_variance(current_cost, previous_cost):
    variance = current_cost - previous_cost
    
    if previous_cost == 0:
        percent_change = 0
    else:
        percent_change = (variance / previous_cost) * 100

    return variance, percent_change

def main():
    # Example dataset (replace with real data source later)
    data = {
        "service": ["EC2", "S3", "RDS"],
        "previous_cost": [1000, 500, 800],
        "current_cost": [1300, 450, 1000]
    }

    df = pd.DataFrame(data)

    results = []

    for index, row in df.iterrows():
        variance, percent = calculate_variance(
            row["current_cost"],
            row["previous_cost"]
        )

        results.append({
            "service": row["service"],
            "variance": variance,
            "percent_change": round(percent, 2)
        })

    result_df = pd.DataFrame(results)

    print("Cost Variance Analysis:")
    print(result_df)

if __name__ == "__main__":
    main()
