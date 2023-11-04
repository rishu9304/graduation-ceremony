def graduation_ceremony_problem(no_of_days,allowed_consecutive_days):
    """
    Time Complexity: O(allowed_consecutive_days * no_of_days)
    Space Complexity: O(allowed_consecutive_days)

    1. The outer loop runs for each day from 1 to no_of_days.
    2. The inner loop calculates the valid ways to attend classes, ensuring that the student doesn't miss four or more consecutive days.
    3. The dp array stores the number of valid ways at each iteration. temp array is used to calculate the next state.
    4. The value at dp[j] represents the number of valid ways to attend classes without missing j consecutive days.
    5. "valid_way_to_attend_classes" represents the total number of valid ways to attend classes without missing more than three consecutive days.
    6. "total_number_way_to_miss_last_day" represents the total number of ways the student can miss the last day.
    7. The function returns the result in the format "number of ways to miss last day/total number of valid ways to attend classes."
    """
    no_of_days, allowed_consecutive_days = no_of_days, allowed_consecutive_days
    dp = [1] * (allowed_consecutive_days + 1)
    dp[allowed_consecutive_days] = 0
    # print("S", dp)
    for _ in range(1, no_of_days + 1):
        temp = [0] * (allowed_consecutive_days + 1)
        for j in range(allowed_consecutive_days - 1, -1, -1):
            temp[j] = dp[0] + dp[j + 1]
        temp, dp = dp, temp

    valid_way_to_attend_classes = dp[0]  # total number of valid way to attend classes
    total_number_way_to_miss_last_day = temp[1]  # total number of way to miss last day

    return f"{total_number_way_to_miss_last_day}/{valid_way_to_attend_classes}"

try:
    n = int(input("Enter the number of days: "))
    m = 4 # As per problem statment
    print(graduation_ceremony_problem(n,4))
except:
    print("Something went wrong. Please try again with valid inputs")
