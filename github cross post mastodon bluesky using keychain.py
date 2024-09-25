from atproto import Client, AtUri, client_utils
import keyring
import keyring.util.platform_ as keyring_platform
import tkinter
import tkinter.simpledialog
from mastodon import Mastodon

NAMESPACE = "REPLACE-WITH-KEYCHAIN-APPNAME-FOR-BSKY"
#ENTRY = tkinter.simpledialog.askstring("username", "enter username: ")
ENTRY = "REPLACE-WITH-BSKY-NAME.bsky.social"
cred = keyring.get_credential(NAMESPACE, ENTRY)

cli = Client()
cli.login(cred.username, cred.password)
TextToPost=tkinter.simpledialog.askstring("Text to post", "Enter text to post")
SplitTextToPost=TextToPost.split('...')
for i in SplitTextToPost:
    print(i)
    print("")
SectionChoosen=tkinter.simpledialog.askinteger(title="Section Selection", prompt="Section for bluesky")
NewTextToPost=SplitTextToPost[SectionChoosen-1]
NewTextToPost=NewTextToPost.replace('\n','').replace('  ',' ').replace('  ', ' ')
ArticleLinkUrl=tkinter.simpledialog.askstring("Link to post", "Enter link to post")
ArticleLinkText=tkinter.simpledialog.askstring("Link name", "Enter link label")
ArticleLinkText=' '+ArticleLinkText
HashtagText=tkinter.simpledialog.askstring("Hashtags", "Enter hashtags")
AmountToTrim=300-((len(NewTextToPost)+len(ArticleLinkText)+2))
TrimTextToPost = (NewTextToPost[:AmountToTrim]+'..') if AmountToTrim < 0 else NewTextToPost
tb=client_utils.TextBuilder()
#tb.text('"'+TrimTextToPost+'"')
tb.text(TrimTextToPost)
if len(ArticleLinkUrl)>2:
    tb.link(ArticleLinkText, ArticleLinkUrl)

cli.send_post(tb)

NAMESPACE = "REPLACE-WITH-KEYCHAIN-APPNAME-FOR-BSKY"
#ENTRY = tkinter.simpledialog.askstring("username", "enter username: ")
ENTRY = "REPLACE-WITH-MASTODON-USERNAME"
cred = keyring.get_credential(NAMESPACE, ENTRY)
mastodon = Mastodon(
    access_token=cred.password,
    api_base_url='https://REPLACE-WITH-MASTODONSERVER-ADDRESS'
)
