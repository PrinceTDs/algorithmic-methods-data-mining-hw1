"""
The solutions are organized by topic and exercise.
Each exercise is separate and should be run on its own
with the corresponding HackerRank input.
"""
# ============================================================
# PROBLEM 1 - PYTHON PROGRAMMING
# ============================================================

# ------------------------------------------------------------
# 1. INTRODUCTION
# ------------------------------------------------------------

# 1. Say "Hello, World!"
print("Hello, World!")


# 2. Arithmetic Operators
a = int(input())
b = int(input())

print(a + b)
print(a - b)
print(a * b)


# 3. Python: Division
a = int(input())
b = int(input())

print(a // b)
print(a / b)


# 4. Loops
n = int(input())

for i in range(n):
    print(i ** 2)
  
# 5

# 6. Print Function
n = int(input())

for i in range(1, n + 1):
    print(i, end="")


# 7. If-Else
n = int(input())

if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")

# ============================================================
# 2. DATA TYPES
# ============================================================

# 1. List Comprehensions
x = int(input())
y = int(input())
z = int(input())
n = int(input())

result = []

for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if i + j + k != n:
                result.append([i, j, k])

print(result)


# 2. Find the Runner-Up Score


# 3. Nested Lists
students = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

scores = sorted(set(score for name, score in students))
second_lowest = scores[1]

names = sorted(name for name, score in students if score == second_lowest)

for name in names:
    print(name)


# 4. Finding the Percentage
n = int(input())
student_marks = {}

for _ in range(n):
    name, *marks = input().split()
    student_marks[name] = [float(mark) for mark in marks]

query_name = input()

average = sum(student_marks[query_name]) / len(student_marks[query_name])

print(f"{average:.2f}")


# 5. Lists
N = int(input())
numbers = []

for _ in range(N):
    command = input().split()

    if command[0] == "insert":
        numbers.insert(int(command[1]), int(command[2]))
    elif command[0] == "print":
        print(numbers)
    elif command[0] == "remove":
        numbers.remove(int(command[1]))
    elif command[0] == "append":
        numbers.append(int(command[1]))
    elif command[0] == "sort":
        numbers.sort()
    elif command[0] == "pop":
        numbers.pop()
    elif command[0] == "reverse":
        numbers.reverse()


# 6. Tuples

n = int(input())
values = tuple(map(int, input().split()))

print(hash(values))
# ============================================================
# 3. STRINGS
# ============================================================

# 1. sWAP cASE
def swap_case(s):
    result = ""

    for char in s:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char

    return result


# 2. String Split and Join
def split_and_join(line):
    words = line.split(" ")
    return "-".join(words)


# 3. What's Your Name?
def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")


# 4. Mutate String
def mutate_string(string, position, character):
    chars = list(string)
    chars[position] = character
    return "".join(chars)


# 5. Find a String
def count_substring(string, sub_string):
    count = 0

    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1

    return count


# 6. String Validators
text = input()

print(any(char.isalnum() for char in text))
print(any(char.isalpha() for char in text))
print(any(char.isdigit() for char in text))
print(any(char.islower() for char in text))
print(any(char.isupper() for char in text))


# 7. Text Wrap
import textwrap

def wrap(string, max_width):
    pieces = []

    for i in range(0, len(string), max_width):
        pieces.append(string[i:i + max_width])

    return "\n".join(pieces)


# 8. Designer Door Mat



# 9. String Formatting
n = int(input())

width = len(str(n))

for i in range(1, n + 1):
    print(
        str(i).rjust(width),
        oct(i)[2:].rjust(width),
        hex(i)[2:].upper().rjust(width),
        bin(i)[2:].rjust(width)
    )


# 10. Capitalize!

def solve(s):
    words = s.split(" ")
    result = []

    for word in words:
        if word:
            result.append(word[0].upper() + word[1:])
        else:
            result.append("")

    return " ".join(result)


# 11. Text Alignment

thickness = int(input())
c = "H"

for i in range(thickness):
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) +
          (c * thickness).center(thickness * 6))

for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))

for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) +
          (c * thickness).center(thickness * 6))

for i in range(thickness):
    part = (c * (thickness - i - 1)).rjust(thickness)
    part += c
    part += (c * (thickness - i - 1)).ljust(thickness)

    print(part.rjust(thickness * 6))


# 12. The Minion Game
def minion_game(string):
    vowels = "AEIOU"
    kevin = 0
    stuart = 0

    for i in range(len(string)):
        points = len(string) - i

        if string[i] in vowels:
            kevin += points
        else:
            stuart += points

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")


# 13. Merge the Tools!

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        section = string[i:i + k]
        unique = ""

        for char in section:
            if char not in unique:
                unique += char

        print(unique)


# 14. String Validators / Additional String Practice

def check_string(s):
    return {
        "alphanumeric": any(c.isalnum() for c in s),
        "alphabetical": any(c.isalpha() for c in s),
        "digits": any(c.isdigit() for c in s),
        "lowercase": any(c.islower() for c in s),
        "uppercase": any(c.isupper() for c in s)
    }

# ============================================================
# 4. SETS
# ============================================================

# 1. Introduction to Sets

n = int(input())
values = list(map(float, input().split()))

numbers = set(values)

print(sum(numbers) / len(numbers))


# 2. No Idea!

n, m = map(int, input().split())

array = list(map(int, input().split()))
happy = set(map(int, input().split()))
sad = set(map(int, input().split()))

score = 0

for number in array:
    if number in happy:
        score += 1
    elif number in sad:
        score -= 1

print(score)


# 3. Symmetric Difference

n = int(input())
first = set(map(int, input().split()))

m = int(input())
second = set(map(int, input().split()))

difference = first.symmetric_difference(second)

for number in sorted(difference):
    print(number)


# 4. Set .add()

n = int(input())
countries = set()

for _ in range(n):
    countries.add(input())

print(len(countries))


# 5. Set .discard(), .remove() & .pop()

n = int(input())
numbers = set(map(int, input().split()))

for _ in range(int(input())):
    command = input().split()

    if command[0] == "pop":
        numbers.pop()
    elif command[0] == "remove":
        numbers.remove(int(command[1]))
    elif command[0] == "discard":
        numbers.discard(int(command[1]))

print(sum(numbers))


# 6. Set .union() Operation

n = int(input())
english = set(map(int, input().split()))

m = int(input())
french = set(map(int, input().split()))

print(len(english | french))


# 7. Set .intersection() Operation

n = int(input())
english = set(map(int, input().split()))

m = int(input())
french = set(map(int, input().split()))

print(len(english & french))


# 8. Set .difference() Operation

n = int(input())
english = set(map(int, input().split()))

m = int(input())
french = set(map(int, input().split()))

print(len(english - french))


# 9. Set .symmetric_difference() Operation

n = int(input())
english = set(map(int, input().split()))

m = int(input())
french = set(map(int, input().split()))

print(len(english ^ french))


# 10. Set Mutations

n = int(input())
main_set = set(map(int, input().split()))

for _ in range(int(input())):
    command = input().split()
    other_set = set(map(int, input().split()))

    if command[0] == "update":
        main_set.update(other_set)
    elif command[0] == "intersection_update":
        main_set.intersection_update(other_set)
    elif command[0] == "difference_update":
        main_set.difference_update(other_set)
    elif command[0] == "symmetric_difference_update":
        main_set.symmetric_difference_update(other_set)

print(sum(main_set))


# 11. The Captain's Room

k = int(input())
rooms = list(map(int, input().split()))

room_counts = {}

for room in rooms:
    room_counts[room] = room_counts.get(room, 0) + 1

for room, count in room_counts.items():
    if count == 1:
        print(room)
        break


# 12. Check Subset

for _ in range(int(input())):
    n = int(input())
    first = set(map(int, input().split()))

    m = int(input())
    second = set(map(int, input().split()))

    print(first.issubset(second))


# 13. Check Strict Superset

main_set = set(map(int, input().split()))

result = True

for _ in range(int(input())):
    other = set(map(int, input().split()))

    if not (main_set > other):
        result = False
        break

print(result)

# ============================================================
# 5. COLLECTIONS
# ============================================================

# 1. collections.Counter()

from collections import Counter

x = int(input())
shoes = list(map(int, input().split()))

stock = Counter(shoes)

customers = int(input())
total = 0

for _ in range(customers):
    size, price = map(int, input().split())

    if stock[size] > 0:
        total += price
        stock[size] -= 1

print(total)


# 2. DefaultDict Tutorial

from collections import defaultdict

n, m = map(int, input().split())

group_a = defaultdict(list)

for i in range(1, n + 1):
    word = input()
    group_a[word].append(i)

for _ in range(m):
    word = input()

    if word in group_a:
        print(*group_a[word])
    else:
        print(-1)


# 3. Collections.namedtuple()

from collections import namedtuple

n = int(input())

fields = input().split()
Student = namedtuple("Student", fields)

total_marks = 0

for _ in range(n):
    student = Student(*input().split())
    total_marks += int(student.MARKS)

print(total_marks / n)


# 4. Collections.OrderedDict()

from collections import OrderedDict

n = int(input())

items = OrderedDict()

for _ in range(n):
    data = input().split()
    name = " ".join(data[:-1])
    price = int(data[-1])

    items[name] = items.get(name, 0) + price

for name, price in items.items():
    print(name, price)


# 5. Word Order

from collections import OrderedDict

n = int(input())

words = OrderedDict()

for _ in range(n):
    word = input()
    words[word] = words.get(word, 0) + 1

print(len(words))
print(*words.values())


# 6. Collections.deque()

from collections import deque

d = deque()

n = int(input())

for _ in range(n):
    command = input().split()

    if command[0] == "append":
        d.append(int(command[1]))
    elif command[0] == "appendleft":
        d.appendleft(int(command[1]))
    elif command[0] == "pop":
        d.pop()
    elif command[0] == "popleft":
        d.popleft()

print(*d)


# 7. Company Logo

from collections import Counter

s = input()

counts = Counter(s)

for char, count in sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:3]:
    print(char, count)


# 8. Piling Up!

from collections import deque

for _ in range(int(input())):
    n = int(input())
    blocks = deque(map(int, input().split()))

    possible = True
    previous = float("inf")

    while blocks:
        left = blocks[0]
        right = blocks[-1]

        if left >= right:
            chosen = blocks.popleft()
        else:
            chosen = blocks.pop()

        if chosen > previous:
            possible = False
            break

        previous = chosen

    print("Yes" if possible else "No")

# ============================================================
# 6. DATE AND TIME
# ============================================================

# 1. Calendar Module

import calendar

month, day, year = map(int, input().split())

weekday = calendar.weekday(year, month, day)

print(calendar.day_name[weekday].upper())


# 2. Time Delta

from datetime import datetime

format_string = "%a %d %b %Y %H:%M:%S %z"

for _ in range(int(input())):
    first = datetime.strptime(input(), format_string)
    second = datetime.strptime(input(), format_string)

    difference = abs(int((first - second).total_seconds()))

    print(difference)

# ============================================================
# 7. EXCEPTIONS
# ============================================================

# 1. Exceptions
a, b = input().split()

    try:
        print(int(a) // int(b))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError:
        print("Error Code: invalid literal for int() with base 10")

# ============================================================
# 8. BUILT-INS
# ============================================================

# 1. Zipped!
n, x = map(int, input().split())

marks = []

for _ in range(x):
    marks.append(list(map(float, input().split())))

for student in zip(*marks):
    print(sum(student) / x)


# 2. Athlete Sort
n, m = map(int, input().split())

rows = []

for _ in range(n):
    rows.append(list(map(int, input().split())))

k = int(input())

rows.sort(key=lambda row: row[k])

for row in rows:
    print(*row)


# 3. ginortS
s = input()

lowercase = sorted(c for c in s if c.islower())
uppercase = sorted(c for c in s if c.isupper())
odd_digits = sorted(c for c in s if c.isdigit() and int(c) % 2 == 1)
even_digits = sorted(c for c in s if c.isdigit() and int(c) % 2 == 0)

print("".join(lowercase + uppercase + odd_digits + even_digits))

# ============================================================
# 9. REGEX AND PARSING
# ============================================================

# 1. Detect Floating Point Number

import re

pattern = r"^[+-]?\d*\.\d+$"

for _ in range(int(input())):
    value = input()
    print(bool(re.fullmatch(pattern, value)))


# 2. Re.split()

import re

regex_pattern = r"[,\.]+"

print("\n".join(re.split(regex_pattern, input())))


# 3. Group(), Groups() & Groupdict()

import re

text = input()

match = re.search(r"([a-zA-Z0-9])\1+", text)

if match:
    print(match.group(1))
else:
    print(-1)


# 4. Re.findall() & Re.finditer()

import re

text = input()

matches = re.findall(r"(?<=[^aeiouAEIOU])[aeiouAEIOU]{2,}(?=[^aeiouAEIOU])", text)

if matches:
    for item in matches:
        print(item)
else:
    print(-1)


# 5. Re.start() & Re.end()

import re

text = input()
pattern = input()

found = False

for match in re.finditer(f"(?={re.escape(pattern)})", text):
    print((match.start(), match.start() + len(pattern) - 1))
    found = True

if not found:
    print((-1, -1))


# 6. Regex Substitution

import re

n = int(input())

for _ in range(n):
    line = input()
    line = re.sub(r"(?<= )&&(?= )", "and", line)
    line = re.sub(r"(?<= )\|\|(?= )", "or", line)
    print(line)


# 7. Validating Roman Numerals

import re

roman = input()

pattern = r"^(?=[MDCLXVI])M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

print(bool(re.fullmatch(pattern, roman)))


# 8. Validating phone numbers

import re

n = int(input())

for _ in range(n):
    number = input()
    print("YES" if re.fullmatch(r"[789]\d{9}", number) else "NO")


# 9. Validating and Parsing Email Addresses

import re

n = int(input())

pattern = r"<([a-zA-Z][a-zA-Z0-9._-]*)@([a-zA-Z]+)\.([a-zA-Z]{1,3})>"

for _ in range(n):
    name, email = input().split()

    if re.fullmatch(pattern, email):
        print(name, email)


# 10. Validating UID

import re

n = int(input())

for _ in range(n):
    uid = input()

    valid_length = len(uid) == 10
    valid_chars = bool(re.fullmatch(r"[A-Za-z0-9]+", uid))
    two_upper = len(re.findall(r"[A-Z]", uid)) >= 2
    three_digits = len(re.findall(r"\d", uid)) >= 3
    no_repeat = len(set(uid)) == len(uid)

    if valid_length and valid_chars and two_upper and three_digits and no_repeat:
        print("Valid")
    else:
        print("Invalid")


# 11. Validating Credit Card Numbers

import re

n = int(input())

for _ in range(n):
    card = input()

    digits = card.replace("-", "")

    valid_format = bool(re.fullmatch(r"\d{16}", digits))
    valid_start = digits[0] in "456"
    no_long_run = not bool(re.search(r"(\d)\1{3,}", digits))

    if valid_format and valid_start and no_long_run:
        print("Valid")
    else:
        print("Invalid")


# 12. Validating Postal Codes

import re

postal = input()

pattern = r"^[1-9][0-9]{5}$"

valid_digits = bool(re.fullmatch(pattern, postal))
alternating = bool(re.search(r"(\d)(?=\d\1)", postal))

print(valid_digits and alternating)


# 13. Detect HTML Tags, Attributes and Attribute Values

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print(tag)

        for name, value in attrs:
            print("->", name, ">", value)

    def handle_startendtag(self, tag, attrs):
        print(tag)

        for name, value in attrs:
            print("->", name, ">", value)

parser = MyHTMLParser()

for _ in range(int(input())):
    parser.feed(input())


# 14. HTML Parser - Part 1

from html.parser import HTMLParser

class Parser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for name, value in attrs:
            print("->", name, ">", value)

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for name, value in attrs:
            print("->", name, ">", value)

parser = Parser()

for _ in range(int(input())):
    parser.feed(input())

# ============================================================
# 10. XML
# ============================================================

# 1. Find the Score

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    total = 0

    for element in node.iter():
        total += len(element.attrib)

    return total


# 2. Find the Maximum Depth

import xml.etree.ElementTree as etree

maxdepth = 0

def depth(elem, level):
    global maxdepth

    maxdepth = max(maxdepth, level)

    for child in elem:
        depth(child, level + 1)

# ============================================================
# 11. CLOSURES AND DECORATORS
# ============================================================

# 1. Standardize Mobile Number Using Decorators

def wrapper(f):
    def fun(l):
        numbers = []

        for number in l:
            digits = number[-10:]
            formatted = "+91 " + digits[:5] + " " + digits[5:]
            numbers.append(formatted)

        f(numbers)

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep="\n")


# 2. Decorators 2 - Name Directory

def person_lister(f):
    def inner(people):
        people.sort(key=lambda person: int(person[2]))
        return [f(person) for person in people]

    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

# ============================================================
# 12. NUMPY
# ============================================================

# 1. Arrays

import numpy as np

def arrays(arr):
    return np.array(arr, dtype=float)[::-1]


# 2. Shape and Reshape

import numpy as np

values = list(map(int, input().split()))
arr = np.array(values)

print(arr.reshape(3, 3))


# 3. Transpose and Flatten

import numpy as np

n, m = map(int, input().split())

arr = np.array(
    [input().split() for _ in range(n)],
    dtype=int
)

print(arr.transpose())
print(arr.flatten())


# 4. Concatenate

import numpy as np

n, m, p = map(int, input().split())

first = np.array(
    [input().split() for _ in range(n)],
    dtype=int
)

second = np.array(
    [input().split() for _ in range(m)],
    dtype=int
)

print(np.concatenate((first, second), axis=0))


# 5. Zeros and Ones

import numpy as np

shape = tuple(map(int, input().split()))

print(np.zeros(shape, dtype=int))
print(np.ones(shape, dtype=int))


# 6. Eye and Identity

import numpy as np

n, m = map(int, input().split())

np.set_printoptions(legacy="1.13")

print(np.eye(n, m))


# 7. Array Mathematics

import numpy as np

n, m = map(int, input().split())

a = np.array(
    [input().split() for _ in range(n)],
    dtype=int
)

b = np.array(
    [input().split() for _ in range(n)],
    dtype=int
)

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(a ** b)


# 8. Floor, Ceil and Rint

import numpy as np

arr = np.array(input().split(), dtype=float)

np.set_printoptions(legacy="1.13")

print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))


# 9. Sum and Prod

import numpy as np

n, m = map(int, input().split())

arr = np.array(
    [input().split() for _ in range(n)],
    dtype=int
)

print(np.prod(np.sum(arr, axis=0)))


# 10. Min and Max

import numpy as np

n, m = map(int, input().split())

arr = np.array(
    [input().split() for _ in range(n)],
    dtype=int
)

minimums = np.min(arr, axis=1)

print(np.max(minimums))


# 11. Mean, Var and Std

import numpy as np

n, m = map(int, input().split())

arr = np.array(
    [input().split() for _ in range(n)],
    dtype=float
)

print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(np.std(arr, axis=None))


# 12. Dot and Cross

import numpy as np

n = int(input())

a = np.array(
    [input().split() for _ in range(n)],
    dtype=int
)

b = np.array(
    [input().split() for _ in range(n)],
    dtype=int
)

print(np.dot(a, b))


# 13. Inner and Outer

import numpy as np

a = np.array(input().split(), dtype=int)
b = np.array(input().split(), dtype=int)

print(np.inner(a, b))
print(np.outer(a, b))


# 14. Polynomials

import numpy as np

coefficients = list(map(float, input().split()))
x = float(input())

print(np.polyval(coefficients, x))


# 15. Linear Algebra

import numpy as np

n = int(input())

matrix = np.array(
    [input().split() for _ in range(n)],
    dtype=float
)

print(round(np.linalg.det(matrix), 2))



# ============================================================
# PROBLEM 2 - ALGORITHMS
# ============================================================

# 1. Birthday Cake Candles

def birthdayCakeCandles(candles):
    tallest = max(candles)
    count = 0

    for candle in candles:
        if candle == tallest:
            count += 1

    return count

# 2. kangaroo

def kangaroo(x1, v1, x2, v2):
    distance = x2 - x1
    speed_difference = v1 - v2

    if speed_difference == 0:
        return "YES" if distance == 0 else "NO"

    if distance % speed_difference == 0:
        jumps = distance // speed_difference

        if jumps >= 0:
            return "YES"
          
# 3. Viral Advertising

def viralAdvertising(n):
    people = 5
    total_likes = 0

    for _ in range(n):
        likes = people // 2
        total_likes += likes
        people = likes * 3

    return total_likes

# 4. Recursive Digit Sum

def superDigit(n, k):
    total = sum(int(digit) for digit in n) * k

    while total >= 10:
        total = sum(int(digit) for digit in str(total))

    return total

# 5. Insertion Sort - Part 1

def insertionSort1(n, arr):
    value = arr[-1]
    position = n - 2

    while position >= 0 and arr[position] > value:
        arr[position + 1] = arr[position]
        print(*arr)
        position -= 1

    arr[position + 1] = value
    print(*arr)

# 6. Insertion Sort - Part 2

def insertionSort2(n, arr):
    for i in range(1, n):
        current = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = current
        print(*arr)
