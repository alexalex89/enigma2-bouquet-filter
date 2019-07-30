keep = False
channels = []

filename = "/etc/enigma2/userbouquet.IPTV_OTT_IPTV__tv_.tv"
last_line = ""

with open(filename, "rb") as f_in:
    for line in f_in:
        # First line
        if line.startswith("#NAME "):
            channels.append(line)
            continue

        if line.startswith("#DESCRIPTION ##### DE - "):
            keep = True
        elif line.startswith("#DESCRIPTION ##### "):
            keep = False

        if keep:
            channels.append(line)
        elif "greetings" not in line and (".mp4" in line or ".mkv" in line) and last_line.startswith("#DESCRIPTION DE - "):
            channels.append(last_line)
            channels.append(line)

        last_line = line

with open(filename, "wb") as f_out:
    f_out.write("".join(channels))
