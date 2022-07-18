# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Constraints:
#  1 <= s.length <= 104
#  s consists of parentheses only '()[]{}'.

# ----------------------------------------------------->>>>>>>>>>>>>>>>>

# n = input("Enter Brackets: ")
# l = []
# l1 = []
# for i in range(len(n)):
#     l.append(n[i])

# for j in range(len(n)):
#     for k in range(len(n)):
#         if l[j] == '(':
#             if l[k] == ')':
#                 l1.append(l[j])
#                 l1.append(l[k])
#         if l[j] == '{':
#             if l[k] == '}':
#                 l1.append(l[j])
#                 l1.append(l[k])
#         if l[j] == '[':
#             if l[k] == ']':
#                 l1.append(l[j])
#                 l1.append(l[k])
# print(l)
# print(l1)
# if len(l) == len(l1):
#     print("True")
# else:
#     print("False")


n = input("Enter Brackets: ")
l = []
for i in range(len(n)):
    if n[i] == '(':
        l.append(n[i])
    if n[i] == '{':
        l.append(n[i])
    if n[i] == '[':
        l.append(n[i])
print(l)
for j in range(len(n)):
    if n[j] == ')' and '(' in l:
        l.remove('(')
    if n[j] == '}' and '{' in l:
        l.remove('{')
    if n[j] == ']' and '[' in l:
        l.remove('[')
print(l)
if len(l) == 0:
    print("True")
else:
    print("False")
