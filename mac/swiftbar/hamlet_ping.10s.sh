ping hamlet -c 3 > /dev/null
rc=$?
if [[ $rc -eq 0 ]] ; then
    echo "Hamlet | color=green"
else
    echo "Hamlet | color=red"
fi
