# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

# An interleaving of two strings s and t is a configuration where s and t are divided into n and m 
# substrings
#  respectively, such that:

# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
# Note: a + b is the concatenation of strings a and b.

def isInterleave(s1, s2, s3):
    m, n = len(s1), len(s2)
    
    # Check if the lengths of s1, s2, and s3 add up correctly
    if m + n != len(s3):
        return False
    
    # Create a 2D array to store the intermediate results
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the base case
    dp[0][0] = True
    
    # Check if s1 matches with s3
    for i in range(1, m + 1):
        dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
    
    # Check if s2 matches with s3
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
    
    # Check if s1 and s2 interleaves to form s3
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
    
    return dp[m][n]