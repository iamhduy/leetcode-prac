def maxFreeTime(eventTime, startTime, endTime):
    res = 0

    gap_list = list()  # Construct the gap list (reverse sort to see biggest gap first)
    if startTime[0] > 0:
        gap_list.append((startTime[0], 0))

    for i in range(len(startTime) - 1):
        gap_list.append((startTime[i + 1] - endTime[i], endTime[i]))

    if endTime[-1] < eventTime:
        gap_list.append((eventTime - endTime[-1], endTime[-1]))
    gap_list.sort(reverse=True)
    #print(gap_list)

    for i in range(len(startTime)):
        if i == 0:  # Merge 2 gap left+right of this event
            start = 0
            end = startTime[i + 1]
        elif i == len(startTime) - 1:
            start = endTime[i - 1]
            end = eventTime
        else:
            start = endTime[i - 1]
            end = startTime[i + 1]

        event_len = endTime[i] - startTime[i]
        gap_found = False

        # Find a suitable gap from gap list
        for gap_len, gap_start in gap_list:
            if gap_len < event_len:  # No more gap has enough size
                break
            if gap_start == start or gap_start == end - gap_len:  # We already use this gap above
                continue

            gap_found = True
            break

        if gap_found:  # Move this event to the gap founded, so no event on this gap
            event_len = 0
        res = max(end - start - event_len, res)

    return res


eventTime1 = 5
startTime1 = [1, 3]
endTime1 = [2, 5]

eventTime2 = 10
startTime2 = [0, 7, 9]
endTime2 = [1, 8, 10]

eventTime3 = 10
startTime3 = [0, 3, 7, 9]
endTime3 = [1, 4, 8, 10]

eventTime4 = 5
startTime4 = [0, 1, 2, 3, 4]
endTime4 = [1, 2, 3, 4, 5]

eventTime5 = 34
startTime5 = [0, 17]
endTime5 = [14, 19]

print('Test 1:', maxFreeTime(eventTime1, startTime1, endTime1))
print('Test 2:', maxFreeTime(eventTime2, startTime2, endTime2))
print('Test 3:', maxFreeTime(eventTime3, startTime3, endTime3))
print('Test 4:', maxFreeTime(eventTime4, startTime4, endTime4))
print('Test 5:', maxFreeTime(eventTime5, startTime5, endTime5))