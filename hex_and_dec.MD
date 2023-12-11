First, let's make a table of the digits from 0 to 15 in decimal and hex:

Hex	0	1	2	3	4	5	6	7	8	9	A	B	C	D	E	F
Decimal	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15
Let's say your number has four digits. You make a table where the columns are 16^3, 16^2, 16^1, and 16^0. Put the hex digits in a row below the columns and then the decimal equivalent of each digit in the next row.

Consider the hex number 7A69.

16^3 (4096)	16^2 (256)	16^1 (16)	16^0 (1)
Hex digit	7	A	6	9
Decimal digit	7	10	6	9
Then you multiply each decimal digit by the number in the column and add them all together:

7 * 4096 + 10 * 256 + 6 * 16 + 9 * 1 = 31337
To convert from decimal to hex, we take a different approach. We use division to divide the number by 16 and take the remainder. We convert the remainder to hex and that's our digit. Here's an example:

# Let 31337 be the number we want to convert to hex
# First we check the remainder using modulo
31337 % 16 = 9           # 9 is our rightmost digit            ___9
(31337 - 9) / 16 = 1958  # 1958 is our new number to divide
1958 % 16 = 6            # 6 is our next digit                 __69
(1958 - 6) / 16 = 122    # 122 is our new number to divide
122 % 16 = 10            # 10 is our next digit (hex: A)       _A69
(122 - 0) / 16 = 7       # 7 is our new number to divide
7 % 16 = 7               # 7 is our next digit                 7A69
(7 - 7) / 16 = 0         # 0 is our new number to divide