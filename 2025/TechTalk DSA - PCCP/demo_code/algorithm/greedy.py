# Greedy Algorithm: Activity Selection Problem
def activity_selection(activities):
    # Sort activities by their finish time
    activities.sort(key=lambda x: x[1])
    print("Sorted Activities:", activities)
    selected_activities = []
    last_end_time = 0

    for start, end in activities:
        # If the activity starts after or when the last selected activity ends
        if start >= last_end_time:
            selected_activities.append((start, end))
            last_end_time = end

    return selected_activities


# Example Usage
if __name__ == "__main__":
    # List of activities with (start_time, end_time)
    # 1-9  
    activities = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 9), (8, 9)]

    print("Activities:", activities)
    selected = activity_selection(activities)
    print("Selected Activities:", selected)