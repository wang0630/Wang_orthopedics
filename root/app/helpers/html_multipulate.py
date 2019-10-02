import re

def traverse_insert_img_src(html, imgurl, s3domain):
  if not imgurl:
    return
  counter = 0
  # Function returns the replacement string
  def replace_func(match):
    nonlocal counter
    s = imgurl[counter]
    counter += 1
    return f'<img class="editor__inline-img" src={s3domain}{s}>'
  return re.sub('<img[^>]*>', replace_func, html)
