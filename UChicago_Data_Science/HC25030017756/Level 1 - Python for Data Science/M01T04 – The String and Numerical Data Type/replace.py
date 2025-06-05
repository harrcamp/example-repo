
# save this as a single string
writing_test = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# remove ! from the text
readable_test = writing_test.replace("!", " ")
print(readable_test)

#make the text upper case
upper_case_test = str.upper(readable_test)
print(upper_case_test)

# reverse the text 
reverse_test = readable_test[::-1]
print(reverse_test)

