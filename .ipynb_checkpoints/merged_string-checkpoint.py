s1 = 'glucose'
s2 = 'dabur'
i = 0
merged = ''
while i < len(s1) or i < len(s2):
    if i < len(s1):
        merged += s1[i]
    if i < len(s2):
        merged += s2[i]

    i += 1

print(merged)

string1 = 'tenet'
text = ''

for i in string1:
    text = i + text

if text == string1:
    print("Palindrome")
else:
    print("Not a Palindrome")


new = []
i = 0


def is_palindrome(num):
    temp = num
    palin = 0
    while num < len(str(num)):
        rem = num % 2
        palin = 10 * palin + rem
        num /= 10
    if temp == palin:
        msg = "Palindrome"
    else:
        msg = "Not a Palindrome"
    return msg


is_palindrome(3163)

