# -*- coding: utf8 -*-

import pantyshot as p

print

text = '''

Tables?

Does ~~this~~ work?

So? http://example.com/ "It" <b>Test</b> works?

| Function name | Description                    |
| ------------- | ------------------------------ |
| `help()`      | Display the help window.       |
| `destroy()`   | **Destroy your computer!**     |

<div>Stripped **or** "not"?</div> Test

Test <b>test</b> test

'''

result = p.markdown(
    text,
    p.EXT_TABLES | p.EXT_STRIKETHROUGH | p.EXT_LAX_HTML_BLOCKS,
    p.HTML_SKIP_HTML | p.HTML_EXPAND_TABS | p.HTML_SKIP_LINKS
)
print result
