# Multi-line statements with \
text = "A complex scenario path"
filename = ("spam.cfg", "spam.conf", "foo.cfg", "foo.conf")[0]
if (filename.endswith(".cfg") or filename.endswith(".conf")) \
        and not filename.startswith("test"):
    print(f"Valid config file: {filename}")
