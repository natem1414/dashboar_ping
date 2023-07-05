#!/bin/bash
while true;
        do
        LINE=1
        awk '{print $1}' < /mnt/ctn-hd1-server1-d1/EIC/dashboard_addresses.txt | while read ip;
                do
        CONFIG=$(awk "NR==$LINE" /mnt/ctn-hd1-server1-d1/EIC/dashboard_addresses.txt)
        STRING=$(awk "NR==$LINE" /mnt/ctn-hd1-server1-d1/EIC/dashboard_addresses.txt)
#       CONFIG2=$CONFIG
#       CONFIG=($CONFIG)
#       LED=${CONFIG[1]}
#       DESTINATIONIP=${CONFIG[2]}
#       DESTINATIONPORT=${CONFIG[3]}
#       DESTINATIONTCPUDP=${CONFIG[4]}

#####Dashboard LED use port 4242#######
#TESTIP;LEDNUMBER;ON_OFF;ACTIVETEXT;INACTIVETEXT;ACTIVETEXTCOLOR;INACTIVETEXTCOLOR;ACTIVECOLOR;INACTIVECOLOR;DESTINATIONIP;DESTINATIONPORT;DESTINATIONPROTO
#192.168.116.1;001;ON;TEXT_ON;TEXT_OFF;FFFFFF;0000FF;00FF00;FF0000;192.168.115.95.4242;TCP
        TESTIP=$(echo $STRING | cut -f1 -d";")
        LED=$(echo $STRING | cut -f2 -d";")
        STATE=$(echo $STRING | cut -f3 -d";")
        ACTIVETEXT=$(echo $STRING | cut -f4 -d";")
        INACTIVETEXT=$(echo $STRING | cut -f5 -d";")
        ACTIVETEXTCOLOR=$(echo $STRING | cut -f6 -d";")
        INACTIVETEXTCOLOR=$(echo $STRING | cut -f7 -d";")
        ACTIVECOLOR=$(echo $STRING | cut -f8 -d";")
        INACTIVECOLOR=$(echo $STRING | cut -f9 -d";")
        DESTINATIONIP=$(echo $STRING | cut -f10 -d";")
        DESTINATIONPORT=$(echo $STRING | cut -f11 -d";")
        DESTINATIONPROTO=$(echo $STRING | cut -f12 -d";")
#       echo testip=$TESTIP
#       echo led=$LED
#       echo state=$STATE
#       echo activetext=$ACTIVETEXT
#       echo inactivetext=$INACTIVETEXT
#       echo activecolor=$ACTIVECOLOR
#       echo inactivecolor=$INACTIVECOLOR
#       echo destinationip=$DESTINATIONIP
#       echo destinationport=$DESTINATIONPORT
#       echo destinationprotp=$DESTINATIONPROTO
#       echo config2=$CONFIG2
#       echo testip=$TESTIP
#       echo led=$LED2
#       echo IP=$ip
        ip=$TESTIP
#       echo IP2=$ip
        let LINE=LINE+1
                    if ping -c2 $ip >/dev/null 2>&1; then
                        if [ "$STATE" = "ON" ];
                                then
                                STATE2="ON"
                        fi
                        if [ "$STATE" = "OFF" ];
                                then
                                STATE2="OFF"
                        fi
                        echo $ip IS UP $LED $DESTINATIONIP $DESTINATIONPORT
                        sleep 1
                        else
                        echo $ip IS DOWN
                        if [ "$STATE" = "ON" ];
                                then
                                STATE2="OFF"
                        fi
                        if [ "$STATE" = "OFF" ];
                                then
                                STATE2="ON"
                        fi
                fi
                TCPSTRING="LIGHT;"$LED";"$STATE2";"$ACTIVETEXT";"$INACTIVETEXT";"$ACTIVETEXTCOLOR";"$INACTIVETEXTCOLOR";"$ACTIVECOLOR";"$INACTIVECOLOR
                echo "$TCPSTRING" | nc -w 1 $DESTINATIONIP $DESTINATIONPORT
                echo "TCPSTRING=" $TCPSTRING
#       sleep 2
        done
        sleep 0
done
