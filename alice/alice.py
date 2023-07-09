import os
import random
import shutil
from wonderwords import RandomWord
from secret import flag

shutil.rmtree("dump")
os.mkdir("dump")

w = RandomWord()

real_words = w.random_words(100)
if "index" in real_words:
    real_words.remove("index")

real_words.insert(0, "index")
target = real_words[-1]

with open("dump/" + target + ".html", "w") as f:
    f.write(f"<html><body><pre>{flag}</pre></body></html>")
    f.close()

for i in range(len(real_words) - 1):
    with open("dump/" + real_words[i] + ".html", "w") as f:
        pre_fake_words = w.random_words(random.randint(500, 1000))
        suf_fake_words = w.random_words(random.randint(500, 1000))

        pre_html = " ".join(
            [f"<a>{pre_fake_word}</a>" for pre_fake_word in pre_fake_words]
        )

        suf_html = " ".join(
            [f"<a>{suf_fake_word}</a>" for suf_fake_word in suf_fake_words]
        )

        head = """
            <head>
                <style>
                    a, a:visited {
                        color: #0066CC;
                        text-decoration: underline;
                        cursor: pointer;
                    }
                </style>
            </head>
        """
        body = f"""
            <body>
                <p>
                    {pre_html} <a href="/{real_words[i + 1]}.html">{real_words[i + 1]}</a> {suf_html}
                </p>
            </body>
        """
        doc = f"<html>{head}{body}</html>"

        f.write(doc)
        f.close()
