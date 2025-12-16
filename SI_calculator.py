def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


if __name__ == "__main__":
    p = float(input("Enter Principal amount: "))
    r = float(input("Enter Rate of Interest: "))
    t = float(input("Enter Time (in years): "))

    si = simple_interest(p, r, t)
    print(f"Simple Interest is: {si}")
