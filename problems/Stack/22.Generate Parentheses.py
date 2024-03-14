
def generate_parenthesis(n: int):
    # Add open parenthesis if open < n
    # Add close parenthesis if closed < open
    # Valid if open == closed == n

    result = []

    def dfs(open_n, close_n, cur_str):
        if open_n == 0 and close_n == 0:
            result.append(cur_str)
            return
        if open_n > 0:
            dfs(open_n - 1, close_n, cur_str + '(')
        if close_n > 0 and open_n < close_n:
            dfs(open_n, close_n - 1, cur_str + ')')

    dfs(n, n, '')
    return result


print(generate_parenthesis(3))
