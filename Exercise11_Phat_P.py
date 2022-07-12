# Input = 5
#  |12345|12345|
# 1|    *|     |
# 2|   **|*    |
# 3|  ***|**   |
# 4| ****|***  |
# 5|*****|**** |

inp = int(input("input your peramid floor : "))
for x in range(inp):
    x += 1
    print_row = ""
    for y_1_1 in range(inp-x):
        print_row += " "
    for y_1_2 in range(x):
        print_row += "*"
    for y_2_1 in range(x-1):
        print_row += "*"
    for y_2_2 in range(inp-x-1):
        print_row += " "
    print(print_row)
