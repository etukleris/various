def largest_increas_subseq(arr):
    #
    long_start = 0
    long_count = 0
    current_start = 0
    current_count = 1
    for i in range(len(arr) - 1):
        print(arr[i], arr[i+1])
        if arr[i +1] > arr[i]:
            print(arr[current_start:current_start+current_count+1])
            current_count += 1
            print(current_count, long_count, 'debug cur/long')
            if current_count > long_count:
                print('heeyyyy')
                long_count = current_count
                long_start = i - current_count + 1
                print(long_start, long_count)
                print(arr[long_start:long_start + long_count ])
        else:
            #print(current_start,arr[current_start:current_start+current_count+1])
            current_count = 1
            current_start = i+1


    if long_count >= 3:
        print(long_start, long_count)
        return (arr[long_start+1:long_start + long_count +1])
    else:
        print(long_start, long_count)
        return ("No increasing subsequence")
tmp=[133, 543, 221, 335, 819, 796, 686, 473, 644, 135, 572, 456, 647, 359, 1195, 754, 698, 609, 875, 409, 59, 654, 1064, 736, 459, 285, 540, 376, 460, 854, 776, 390, 1122, 120, 836, 1433, 1317, 1208, 692, 94, 360, 943, 412, 1459, 1347, 1290, 1432, 1331, 1237, 1129, 1115, 1081, 971, 969, 953, 879, 783, 766, 693]
tmpp = [1247, 1171, 1152, 1139, 1111, 1110, 1062, 1049, 965, 922, 851, 776, 766, 733, 692, 771, 1157, 1123, 1183, 431, 1017, 608, 320, 1200, 801, 343, 676, 91, 532, 1203, 608, 419, 436, 692, 325, 846, 171, 580, 1129, 350, 663, 738, 54, 481, 935, 1050, 825, 1160, 111, 159, 196, 303, 310, 361, 400, 519, 626, 740]
print(largest_increas_subseq(tmp))