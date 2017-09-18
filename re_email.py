
import re

re_email = re.compile(r'^([0-9a-zA-Z\_\.]+?)\@([0-9a-zA-Z\_]+?.com)$')
print(re_email.match("szcls89@gmail.com"))
print(re_email.match("bill.gates@microsoft.com"))