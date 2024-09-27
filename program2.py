def decode_message( s: str, p: str) -> bool:

def is_match(message, pattern):
    m, n = len(message), len(pattern)
    
    # DP table where dp[i][j] is True if the first i characters of message match the first j characters of pattern
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Base case: Empty message matches with empty pattern
    dp[0][0] = True
    
    # Base case: Message is empty but pattern has '*' characters that can match an empty sequence
    for j in range(1, n + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern[j - 1] == '?' or pattern[j - 1] == message[i - 1]:
                # Current character matches: Either '?', or exact match
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[j - 1] == '*':
                # '*' can match zero or more characters
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
    
    # The answer is whether the entire message matches the entire pattern
    return dp[m][n]
  
        return False