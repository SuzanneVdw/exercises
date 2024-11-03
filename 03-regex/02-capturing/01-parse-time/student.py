import re

def parse_time(string):

    match = re.fullmatch(r'(\d{2}):(\d{2}):(\d{2})(\.(\d{3}))?', string)

    if not match:
        return None
    
    h = match.group(1)
    m = match.group(2)
    s = match.group(3)
    ms = match.group(5) or 0

    return (int(h),int(m),int(s),int(ms))