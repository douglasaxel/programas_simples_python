def main():
    num = 0
    nums = []
    for n in range(1000):
        if n % 3 == 0 or n % 5 == 0:
            nums.append(n)
            num += n

    print(nums)
    return num

if __name__ == '__main__':
    print(main())
