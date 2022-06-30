# -*- coding: utf-8 -*-
# nmea_zu_geojson_konverter_muloe.py
#
# https://tools.ietf.org/html/rfc7946
# https://de.wikipedia.org/wiki/NMEA_0183#Recommended_Minimum_Sentence_C_(RMC)


def nmea_to_geojson(nmea, geojson):

    header = ('var track = {"type": "Feature", "geometry": {'
              '"type": "LineString", "coordinates": [\n')
    footer = ']}};'

    # Open the NMEA file for reading and the GeoJSON file for writing.
    with open(nmea, encoding='ascii') as f_nmea,\
            open(geojson, 'w', encoding='ascii') as f_geojson:

        # Write the header to the GeoJSON file.
        f_geojson.write(header)

        # Read the NMEA file line by line.
        for line in f_nmea:

            # Clean up the line, e.g. remove \n at the end.
            line = line.strip()

            # If the line does not contains the RMC message.
            if not any(line.startswith(s)
                       for s in ['$GPRMC', '$GNRMC', '$GLRMC']):
                continue

            try:
                # Compute the checksum.
                chksum = 0
                for c in line[1:-3].encode('ascii'):
                    chksum ^= c
                # If the checksum does not match.
                if chksum != int(line[-2:], 16):
                    # Skip the current line.
                    continue
            except (UnicodeEncodeError, ValueError):
                # If any error occurred skip the current line.
                continue

            # Split the line into a list of items.
            items = line.split(',')

            # If the number of items does not match.
            if len(items) != 13:
                # Skip the current line.
                continue

            # If the status is not active. (A=active or V=void)
            if items[2] != 'A':
                # Skip the current line.
                continue

            try:
                # Compute the latitude.
                temp = float(items[3])
                lat = temp//100 + (temp % 100)/60
                lat = lat if items[4] == 'N' else -lat
                # Compute the longitude.
                temp = float(items[5])
                lon = temp//100 + (temp % 100)/60
                lon = lon if items[6] == 'E' else -lon
            except ValueError:
                # If any errors occurred skip the current line.
                continue

            # Write the longitude and latitude into the GeoJSON file.
            f_geojson.write('[{:.6f},{:.6f}],\n'.format(lon, lat))

        # Write the footer into the GeoJSON file.
        f_geojson.write(footer)


# --- Test --------------------------------------------------------------------
if __name__ == '__main__':
    nmea_to_geojson(nmea='logfile.nmea', geojson='data.js')
