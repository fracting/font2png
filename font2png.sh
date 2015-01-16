#!/bin/bash
#
BINPATH=$(which "$0")
CURDIR=$(dirname $BINPATH)
FONT=$1

$CURDIR/ttf2sfd.pe $FONT

LIST=$(grep Encoding $FONT.sfd | sed '1d' | cut -f2 -d' ')
printf $LIST

OUTPUT=$FONT.png
mkdir $OUTPUT 

for num in $LIST; do
    printf $num
    if test $num -lt 65536; then
        char=$(printf "\\\\u%x" $num)
        printf $char
    else
        char=$(printf "\\\\U%x" $num)
        printf $char
    fi
    printf " "
    printf $char | convert -font $FONT -background white -fill black -pointsize 300 label:@- $OUTPUT/$FONT-$num.png
    FROM=$((FROM+1))
done
printf '\n'
tar czvf $OUTPUT.tar.gz $OUTPUT
