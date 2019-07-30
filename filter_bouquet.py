import optparse


def filter_bouquet(country_code, input_filename, output_filename):
    if output_filename is None:
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

            if line.startswith("#DESCRIPTION ##### {} - ".format(country_code)):
                keep = True
            elif line.startswith("#DESCRIPTION ##### "):
                keep = False

            if keep:
                channels.append(line)
            elif "greetings" not in line and (".mp4" in line or ".mkv" in line) and last_line.upper().startswith("#DESCRIPTION {} - ".format(country_code)):
                channels.append(last_line)
                channels.append(line)

            last_line = line

    with open(output_filename, "wb") as f_out:
        f_out.write("".join(channels))


if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option("-i", "--input", dest="input",
                      default="/etc/enigma2/userbouquet.IPTV_OTT_IPTV__tv_.tv",
                      help="Path to input filename (Bouquet). Default: /etc/enigma2/userbouquet.IPTV_OTT_IPTV__tv_.tv",
                      type="string")
    parser.add_option("-o", "--output", dest="output",
                      default=None,
                      help="Path to output filename (Bouquet). Default: Same as input", type="string")
    parser.add_option("-c", "--country", dest="country_code", default="DE",
                      help="Country code to search and filter for. Default: DE",
                      type="string")
    options, _ = parser.parse_args()

    country_code = options.country_code.upper()

    filter_bouquet(country_code=country_code, input_filename=options.input, output_filename=options.output)
