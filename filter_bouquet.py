def filter_bouquet(input_filename, output_filename=None):
    if not output_filename:
        output_filename = input_filename
    keep = False
    channels = []

    last_line = ""

    with open(input_filename, "rb") as f_in:
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
            elif "greetings" not in line and (".mp4" in line or ".mkv" in line) and last_line.upper().startswith("#DESCRIPTION DE - "):
                channels.append(last_line)
                channels.append(line)

            last_line = line

    with open(output_filename, "wb") as f_out:
        f_out.write("".join(channels))


if __name__ == "__main__":
    filename = "/etc/enigma2/input_bouquet.tv"
    filter_bouquet(input_filename=filename)
