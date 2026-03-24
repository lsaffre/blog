from lino.utils.soup import sanitize
body = """
<p>
  <span style="color: rgb(102, 102, 102); background-color: rgb(220, 220, 220);">
    This is some text.
  </span>
</p>
""".strip()

print(sanitize(body))
