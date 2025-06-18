from tableprint import pretty


def gen(n):
    dp = ['' for _ in range(n + 1)]
    dp[1] = ['()']

    return 1


n = 4
dp = [[] for j in range(n+1)]
dp[1].append('()')
for i in range(2, n+1):
    string_add = '()'
    handle_set = set()
    for s in dp[i - 1]:
        handle_set.add(string_add + s)
        handle_set.add(s + string_add)
        for j in range(1, len(s)):
            handle_set.add(string_add[0] + s[:j] + string_add[1] + s[j:])
    dp[i] = list(handle_set)

print(dp[3])
print(["((()))", "(()())", "(())()", "()(())", "()()()"])
print()
print(dp[4])
print()
truth = ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()", "(())(())", "(())()()",
         "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"]

for p in dp[4]:
    truth.remove(p)

print(truth)
