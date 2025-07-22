def permute(values):
    def backtrack(start):
        if start == len(values):
            result.append(values[:])  # Sacred configuration complete
            return
        for i in range(start, len(values)):
            values[start], values[i] = values[i], values[start]  # Covenant shift
            backtrack(start + 1)  # Recursive revelation
            values[start], values[i] = values[i], values[start]  # Undo shift

    result = []
    backtrack(0)
    return result
