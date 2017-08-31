#!/bin/bash

episodes=("Dude Ranch" "When Good Kids Go Bad" "Phil on Wire" "Door to Door" "Hit and Run" "Go Bullfrogs!" "Treehouse" "After the Fire" "Punkin Chunkin" "Express Christmas" "Lifetime Supply" "Egg Drop" "Little Bo Bleep" "Me? Jealous?" "Aunt Mommy" "Virgin Territory" "Leap Day" "Send Out the Clowns" "Election Day" "The Last Walt" "Planes, Trains and Cars" "Disneyland" "Tableau Vivant" "Baby on Board")
echo ${#episodes[@]}"episodes";
for i in `seq 1 ${#episodes[@]}`;
do
    if [ $i -lt 10 ];then
         file="S03E0"$i 
    else
        file="S03E"$i 
    fi
    f="*$file*.avi"
    new=$file"-"${episodes[$i-1]}".avi"
    if [ -f $f ]; then
         cmd='mv '$f' "'$new'"';
         echo $cmd;
         `$cmd`;
    else
        #touch $new"*";
        echo "$f doesnt exists" 
    fi
    
done
