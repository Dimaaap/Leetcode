def letter_combinations(digits: str):
    d = {"2": "abc",
         "3": "def",
         "4": "ghi",
         "5": "jkl",
         "6": "mno",
         "7": "pqrs",
         "8": "tuv",
         "9": "wxyz"}
    ans = []

    def dfs(digits, comb):
        if len(digits) == 0:
            ans.append(comb)
        for i in range(len(digits)):
            for l in d[digits[i]]:
                dfs(digits[i+1:], comb+[l])
    dfs(digits, [])

