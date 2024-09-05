try:
    # Manually raise an exception
    raise ValueError("This is a custom error message")
except ValueError as e:
    print(f"Exception caught: {e}")
else:
    print("No exceptions occurred")
finally:
    print("This block always runs")
