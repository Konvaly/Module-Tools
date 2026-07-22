Do not use any tools or programming to solve these problems. Work it out yourself by hand, and fill in the answers.

Do not convert any binary numbers to decimal when solving a question unless the question explicitly tells you to.

The goal of these exercises is for you to gain an intuition for binary numbers. Using tools to solve the problems defeats the point.

The answers to these questions will require a bit of explanation, not just a simple answer.

Q16: How can you test if a binary number is a power of two (e.g. 1, 2, 4, 8, 16, ...)?
Answer: A power of two in binary has only one 1 bit, followed by zero or more 0 bits: 2² = 4 = 100₂, 2⁴ = 16 = 10000₂

Q17: If reading the byte 0x21 as an ASCII character, what character would it mean?
Answer: (2 × 16) + (1 × 1) = 32 + 1 = 33₁₀ ASCII value 33 = character '!'

Q18: If reading the byte 0x21 as a greyscale colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
Answer: 0x21 = 33₁₀ If we consider greyscale range: 0 (black) to 255 (white), 33 is very close to 0, so it's a very dark grey

Q19: If reading the bytes 0xAA00FF as a sequence of three one-byte decimal numbers, what decimal numbers would they be?
Answer: 0xAA = (10 × 16) + (10 × 1) = 160 + 10 = 170₁₀
0x00 = (0 × 16) + (0 × 1) = 0₁₀
0xFF = (15 × 16) + (15 × 1) = 240 + 15 = 255₁₀

Q20: If reading the bytes 0xAA00FF as an RGB colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
Answer: Red = 170₁₀ (high, but not maximum)
Green = 0₁₀ (none)
Blue = 255₁₀ (maximum)
Red + Blue = violet/purple
Since Blue is max and Red is substantial, it leans toward Blue-Violet
