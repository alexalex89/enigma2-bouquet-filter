# enigma2-bouquet-filter

Filters stream bouquets for a certain language (Currently only German). Might be used for removing foreign streams from an IPTV bouquet.
Input data will be read from `/etc/enigma2/userbouquet.IPTV_OTT_IPTV__tv_.tv` and filtered data saved in the same file, so it appears as Bouquet e.g. on an VU+ box with VTI image installed.

Uses Python2.7, since this is the preinstalled version on the VU+ boxes with VTI image.
