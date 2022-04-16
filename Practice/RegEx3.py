#Regular Expression re.sub() method(for replace)
import re
repl="Whitespace   replaced as    per user's  wish"
print("Before Repalced:-",repl)
sub=re.sub(r"\s+"," ",repl)
print("After:-", sub)
