# Write your code here

import re

def scrape_email_addresses(string):

    return re.findall(r"[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z0-9]+",string)

#print(scrape_email_addresses("a@c.com fsjdf jfslk fkls fjl df jalfkj b@d.be fjdlkf jfkljdlkf qpoiopc fdfqpof ifppopo fkpqo qfjlkl xyz@ppp.fr jkfljqlkj opfpqsjkl<...@...>"))