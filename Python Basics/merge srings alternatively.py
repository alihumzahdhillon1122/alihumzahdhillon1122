# class Solution:
#     def mergeAlternately(self, word1, word2):
#         len1 = len(word1)
#         len2 = len(word2)
#         i = 0
#         j = 0
#         res = []

#         while i < len1 and j < len2:
#             res.append(word1[i])
#             res.append(word2[j])
#             i += 1
#             j += 1
#         res.extend(word1[i:])
#         res.extend(word2[j:])

#         return ''.join(res)

# word1 = "abc"
# word2 = "pqr"
# solution_instance = Solution()  # Create an instance of the Solution class
# merged = solution_instance.mergeAlternately(word1, word2)
# print(merged)





# class Solution:
#     def mergeAlternately(self, word1, word2):
#         # Get the lengths of the input words
#         len1 = len(word1)
#         len2 = len(word2)
        
#         # Initialize two index variables, i for word1 and j for word2
#         i = 0
#         j = 0
        
#         # Initialize an empty list to store the merged characters
#         res = []

#         # Loop to merge characters alternately from both words
#         while i < len1 and j < len2:
#             res.append(word1[i])  # Append a character from word1
#             res.append(word2[j])  # Append a character from word2
#             i += 1  # Move to the next character in word1
#             j += 1  # Move to the next character in word2
        
#         # Append any remaining characters from word1 and word2
#         res.extend(word1[i:])  # Append the remaining characters from word1
#         res.extend(word2[j:])  # Append the remaining characters from word2

#         # Join the merged characters to form the final result string
#         return ''.join(res)

# # Example usage
# word1 = "abc"
# word2 = "pqr"
# solution_instance = Solution()  # Create an instance of the Solution class
# merged = solution_instance.mergeAlternately(word1, word2)
# print(merged)





# # Define the find_max_element function (you can use the code provided earlier)

# def find_max_element(your_list):
#     # Initialize a variable to store the maximum value
#     max_value = your_list[0]

#     # Iterate through the list
#     for number in your_list:
#         # Compare the current number to the maximum value
#         if number > max_value:
#             # Update max_value if the current number is greater
#             max_value = number

#     # Return the maximum value
#     return max_value

# # Example usage:
# numbers = [12, 45, 6, 78, 23, 56, 89, 5]
# maximum = find_max_element(numbers)
# print("Maximum number in the list:", maximum)



# def count_even_number(your_list):

#     even_num = your_list[0]

#     for number in your_list:

#         if number % 2 == 0:
#             even_number +=1
#     return even_number

def sum_even_number(your_list):

    sum = 0

    for number in your_list:

        if number % 2 == 0:
            sum += number

    return sum

    

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_even_number(numbers)
print("sum of even number", result)