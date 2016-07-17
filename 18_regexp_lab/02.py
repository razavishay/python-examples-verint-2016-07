import re

def toCamelCase(str):
    return re.sub(r'(_)([a-z])', lambda m: m.group(2).upper(), str)

print toCamelCase('a_b')
print toCamelCase('a_b_c')
print toCamelCase('a_bbb')
print toCamelCase('word1_word2_word3')

