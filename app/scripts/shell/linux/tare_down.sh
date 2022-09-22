#!/bin/bash
# todo add a debug mode
# todo error logging mode
#/ Usage: tare_down.sh [options]
#/  --help        show help text
#/  --user        user to be removed normally the game_control-name (Required)
#/  --game_control        the name of the game_control that is being uninstalled (Required)
#/  --group       user group to be created and add user to (Optional)
#/  -p,  --path        path of the games install location (Optional)
#/
#/
# todo write description
#/
#/ written by Andrew Mcgregor <a-mcgregor381@protonmail.com>


`HELP=$(unset)`
USER=unset
GAME=unset
INTUSER=unset
INTPATH=unset

usage()
{
 echo "Usage: create_user.sh [options] [--] [<shell-script>...]"
 echo "-h,  --help        show help text"
 echo "-u,  --user        user to be created normally the game-name (Required)"
 echo "-g,  --game        the name of the game that is bein installed (Required)"
 echo "-gp, --group       user group to be created and add user to (Required)"
 echo "-p,  --path        path of the games install location (Optional)"


# debug stuff
echo "parsted stuff"
echo ""
echo "$PARSED_ARGUMENTS"
echo ""
echo "result"
echo ""
echo "$VALID_ARGUMENTS"
exit 2
}

PARSED_ARGUMENTS=$(getopt -n createUser -o hu:g: --longoptions "help,user:,game:" -- "$@")

VALID_ARGUMENTS=$?
if [ "$VALID_ARGUMENTS" != "0" ]; then
  usage
fi

#debug stuff
echo "PARSED_ARGUMENTS is $PARSED_ARGUMENTS"
eval set -- "$PARSED_ARGUMENTS"

while :
do
  case "$1" in
    -h | --help)  HELP=1        usage   ;;
    -u | --user)  USER="$2"     shift 2 ;;
    -g | --game_control)  GAME="$2"     shift 2 ;;
    -r | --group) GROUP="$2" shift 2 ;;
    -p | --path)  GAMEPATH="$2"  shift 2 ;;

    # -- means the end of the arguments; drop this, and break out of the while loop
    --) shift; break ;;
    # If invalid options were passed, then getopt should have reported an error,
    # which we checked as VALID_ARGUMENTS when getopt was called...
    *)
    echo ""
    echo "Unexpected option: $1 - this should not happen."
    usage ;;
  esac
done




delusr USER="$2"
rm -rf /opt/$GAME