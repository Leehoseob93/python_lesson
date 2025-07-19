text = 'abc123$%def'

fi = ''.join(filter(lambda x : x.isalpha(), text))
print(fi)

# 정답 → ''.join(c for c in text if c.isalpha())
# +_+;; 