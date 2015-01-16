#!/usr/bin/python
# create html table from csv
# Author(s): Chris Trombley <ctroms@gmail.com>
# Version 2 - added css class to all columns except header

#!/usr/bin/python
# create html table from csv

import sys
import csv
 
if len(sys.argv) < 3:
    print "Usage: csvToTable.py csv_file html_file"
    exit(1)

# Open the CSV file for reading
reader = csv.reader(open(sys.argv[1]))

# Create the HTML file for output
htmlfile = open(sys.argv[2],"w")

# initialize rownum variable
rownum = 0

# write <table> tag
htmlfile.write("<html>\n<body>\n")
htmlfile.write('<table border="1" align="center">')
htmlfile.write("\n")

# generate table contents
htmlfile.write('<tr><td>Target Glyph</td><td>Candidate Glyph 1</td><td>Candidate Glyph 2</td><td>Candidate Glyph 3</td><tr>')
htmlfile.write("\n")

for row in reader: # Read a single row from the CSV file

    htmlfile.write('<tr>')    
    for column in row:
        uni_dec_str = column.split('.ttf-')[1].split('.png')[0]
        font_name = column.split('.ttf-')[0]
        uni_dec = int(uni_dec_str)
        if uni_dec < 0xffff:
            uni_hex = "u+" + format(int(uni_dec), '04x')
        else:
            uni_hex = "U+" + format(int(uni_dec), '08x')

        htmlfile.write('<td align="center">' + font_name + ':' + "<br/>" + uni_hex + '</td>')
    htmlfile.write('</tr>')
    htmlfile.write("\n")

    htmlfile.write('<tr>')    
    for column in row:
        htmlfile.write('<td><img src="' + column + '" height="120px" width="120px" /></td>')
    htmlfile.write('</tr>')
    htmlfile.write("\n")
    
    htmlfile.write('<tr>')    
    for column in row:
        htmlfile.write('<td><br/></td>')
    htmlfile.write('</tr>')
    htmlfile.write("\n")



    #increment row count    
    rownum += 1

# write </table> tag
htmlfile.write('</table>')
htmlfile.write("\n")
htmlfile.write("</html>\n</body>\n")

# print results to shell
print "Created " + str(rownum) + " row table."
exit(0)
