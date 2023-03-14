from montepi import monte_pi

if __name__ == "__main__":
    points = int(input("Enter the number of points to use for the approximation: "))
    if not isinstance(points, int):
        raise ValueError("Points must be an integer type")

    pi = monte_pi(points)

    print("𝝅 ≈ ", pi)    