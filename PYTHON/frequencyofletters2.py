def count_alphabet_frequency(s):
    # Create a dictionary to store the frequency of each alphabet
    frequency_dict = {}
    
    # Loop through each character in the string
    for char in s:
        # Consider only alphabets
        if char.isalpha():
            # Convert character to lowercase (if case-insensitive)
            char = char.lower()
            # Increment the frequency count in the dictionary
            if char in frequency_dict:
                frequency_dict[char] += 1
            else:
                frequency_dict[char] = 1
    
    # Print the frequency of each alphabet in the order of their first appearance
    for char in frequency_dict:
        print(f"{char}: {frequency_dict[char]}")

# Example usage
input_string = "Hello World!"
count_alphabet_frequency(input_string)
