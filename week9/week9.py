# # 1
# def is_odd(n):
#   return n % 2 != 0
#
#
# # 2
# def is_leap_year(year):
#   if year % 400 == 0:
#     return True
#   elif year % 100 == 0:
#     return False
#   elif year % 4 == 0:
#     return True
#   return False
#
#
#
# # 3
# def print_triangular_numbers(n):
#   total = 0
#   for i in range(1, n + 1):
#     total += i
#     print(f"{i} {total}")
#
#
#
#
# # 4
# def is_prime(n):
#   if n <= 1:
#     return False
#   for i in range(2, int(n**0.5) + 1):
#     if n % i == 0:
#       return False
#   return True


# def reverse(s):
#     result = ""
#     for ch in s:
#         result = ch + result
#     return result
#
# print(reverse("hello"))


# def remove_all_occurences(sub, s):
#     return s.replace(sub, "")
#
# print(remove_all_occurences("abcdefg", ""))



# def substitute(message, key):
#     alphabet = "abcdefghklmnoptrsyuzqwx123456"
#     result = ""
#     for ch in message:
#         index = alphabet.find(ch.lower())
#         if index == -1:
#             result = result + ch
#         elif ch.isupper():
#             result = result + key[index].upper()
#         else:
#             result = result + key[index].lower()
#
#     return result
#
# key = "çşğplömkoıjnbhuygvcftrdxzsewq"
#
# print(substitute("hhhhhhh", key))

# def remove_dups(s):
#     result = ""
#     for ch in s:
#         if ch.lower() not in result.lower():
#             result = result + ch
#     return result
#
# print(remove_dups("aabcddaadd"))




