def min_str_factor(X, Y, S, R):
    n, m = len(X), len(Y)
    reverse_y = Y[::-1]

    dp_array = [float('inf')] * (n + 1)
    dp_array[0] = 0  

    def is_substr(subX, source):
        return subX in source

    for i in range(n):
        for j in range(i + 1, n + 1):
            substrX = X[i:j]

            if is_substr(substrX, Y):
                dp_array[j] = min(dp_array[j], dp_array[i] + S)

            if is_substr(substrX, reverse_y):
                dp_array[j] = min(dp_array[j], dp_array[i] + R)

    return dp_array[n] if dp_array[n] != float('inf') else "Impossible"


if __name__ == '__main__':
    X= input().strip()
    Y= input().strip()
    S, R = map(int, input().strip().split())

    result = min_str_factor(X, Y, S, R)
    print(result)