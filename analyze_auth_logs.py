import csv
from collections import Counter

LOG_FILE = "sample_auth_events.csv"

failed_logons = []
successful_logons = []

try:
    with open(LOG_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            event_id = int(row["event_id"])
            source = row["source"]

            if event_id == 4625:
                failed_logons.append(source)
            elif event_id == 4624:
                successful_logons.append(source)

    failures_by_source = Counter(failed_logons)

    print("Authentication Log Analysis")
    print("-" * 30)
    print(f"Failed logons: {len(failed_logons)}")
    print(f"Successful logons: {len(successful_logons)}")

    print("\nFailed logons by source:")
    for source, count in failures_by_source.items():
        print(f"{source}: {count}")

    print("\nSources with 3 or more failed logons:")
    found = False

    for source, count in failures_by_source.items():
        if count >= 3:
            print(f"Review {source}: {count} failed logons")
            found = True

    if not found:
        print("No sources met the review threshold.")
        
    print("\nAnalyst Assessment:")
    if found:
        print("Repeated failed logons detected. Review the related events before deciding whether activity is suspicious.")
    else:
        print("No sources met the review threshold in this sample.")

except FileNotFoundError:
    print(f"Error: Could not find {LOG_FILE}.")
    print("Make sure the CSV file is in the project folder.")
except (ValueError, KeyError) as error:
    print(f"Error: Check the CSV headers and event IDs. Details: {error}")
    
