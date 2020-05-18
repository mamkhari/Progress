# Problem 6_1: Write code using find() and string slicing (see section 6.10) 
# to extract the number at the end of the line below. Convert the extracted 
# value to a floating point number and print it out.

# Solution
text = "X-DSPAM-Confidence:    0.8475";
white_space = text.find(" ")
number = float(text[white_space::1])
print(number)