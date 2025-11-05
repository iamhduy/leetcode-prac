try:
    max_code = ''
    max_duration = -1
    with open('space_missions.log', 'r') as f:
        for line in f:
            if not line[0].isnumeric():
                continue
            line_ = line.strip()
            # Date | Mission ID | Destination | Status | Crew Size | Duration (days) | Success Rate | Security Code
            mission_data = line_.split('|')
            print(mission_data)
            duration = int(mission_data[5].strip())
            sec_code = mission_data[-1].strip()
            status = mission_data[3].strip()
            if status != "Completed":
                continue

            if duration > max_duration:
                max_code = sec_code
                max_duration = duration

        print(max_code, max_duration)

except FileNotFoundError:
    print("Error: Log file not found.")
except Exception as e:
    print(f"An error occurred: {e}")