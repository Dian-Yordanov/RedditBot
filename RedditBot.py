import praw
from praw.helpers import comment_stream

r = praw.Reddit("raiseyourdongers clone by /u/shaggorama")
r.login()

target_text = "hunter = cancer"
response_text = "SMOrc ME GO FACE SMOrc"
#test
processed = []
while True:
    for c in comment_stream(r, 'test'):
        if target_text in c.body and c.id not in processed:
            c.reply(response_text)
            processed.append(c.id)