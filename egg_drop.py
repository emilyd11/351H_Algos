''' "egg drop" dynamic programming problem 
    ChatGPT-generated code '''
def egg_drop(num_eggs, num_floors):
    # A 2D table where entry dp[i][j] will represent minimum
    # number of trials needed for i eggs and j floors.
    dp = [[0 for x in range(num_floors + 1)] for x in range(num_eggs + 1)]

    # We need one trial for one floor and zero trials for zero floors
    for i in range(1, num_eggs + 1):
        dp[i][1] = 1
        dp[i][0] = 0

    # We always need j trials for one egg and j floors.
    for j in range(1, num_floors + 1):
        dp[1][j] = j

    # Fill rest of the entries in table using optimal substructure property
    for i in range(2, num_eggs + 1):
        for j in range(2, num_floors + 1):
            dp[i][j] = float('inf')
            for x in range(1, j + 1):
               ''' print("comparing \n" + str(i-1) + " eggs and " + str(x-1)
               + "\n with " + str(i) + " eggs and " + str(j-x)) '''
               res = 1 + max(dp[i - 1][x - 1], dp[i][j - x])
               if res < dp[i][j]:
                dp[i][j] = res

    # dp[num_eggs][num_floors] holds the result
    count = 0
    for row in dp:
        print("when you have " + str(count) + " eggs" )
        print(" ".join(map(str, row)))
        count += 1

    return dp[num_eggs][num_floors]

print(egg_drop(2, 10))