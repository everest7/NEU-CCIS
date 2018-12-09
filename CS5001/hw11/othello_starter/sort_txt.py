score = 11
with open("sco.txt", 'r+') as rf:
    string = "cathy" + str(score) +"\n"
    old = rf.read()
    rf.seek(0)
    rf.write(string + old)
    # line = rf.readline()
    # print(line)

# def match_algorith(Boots, Kids):
#     mergeSort(Boots)
#     mergeSort(Kids)
#     matched_pair = []
#     for i from 1 to n:
#         pair = (Boots[i], Kids[i])
#         matched_pair.append(pair)
#     return matched_pair
