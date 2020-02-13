
def maxProfit(arr):
    if len(arr) <2:
        return (0)

    buy = arr[0]
    profit = 0
    for price in arr[1:]:
        buy = min(price, buy)
        profit = max(price - buy, profit)
    return profit


if __name__ == '__main__':
    dayPrice = [3,5,2,9,10,3,100,1,45]
    print maxProfit(dayPrice)

