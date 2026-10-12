
import csv
import requests
import json



if __name__ == "__main__":
    

    with open("data/test_suite.json", "r") as file:
        test_cases = json.load(file)

    #log the test suite results

    csv_headers = [
    "Issue ID", 
    "Input", 
    "Bri's Response", 
    "Expected Output", 
    "Confidence",
    "Severity", 
    "Failure Type", 
    "Prompt Category"
    ]


    with open("data/test_results.csv", mode="w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        writer.writeheader()

        count = 0

        for test_case, test_data in test_cases.items():
            input_text = test_data["input"]
            expected_output = test_data["expected_output"]
            prompt_category = test_data["prompt_category"]

            api = "http://localhost:8000"

            response = requests.post(f"{api}/chat", json={"message": input_text})
            
            actual_output = response.json().get("reply")
            confidence = response.json().get("confidence")
            latency_ms = response.json().get("latency_ms")

            row = {
                "Issue ID": test_case,
                "Input": input_text,
                "Bri's Response": actual_output,
                "Expected Output": expected_output,
                "Confidence": confidence,
                "Severity": "TBD",
                "Failure Type": "TBD",
                "Prompt Category": prompt_category,
            }
            
            writer.writerow(row)
