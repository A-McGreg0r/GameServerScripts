#!/bin/bash
# todo add a debug mode
#/ Usage: createUser.sh [options]
#/  -h,  --help        show help text
#/  -u,  --user        user to be created normally the game_control-name (Required)
#/  -g,  --game_control        the name of the game_control that is being installed (Required)
#/  -gp, --group       user group to be created and add user to (Required)
#/  -p,  --path        path of the games install location (Optional)"
#/
#/ A general script for creating a new user  adding the to a user group for manageing a peticulate game_control on a se>#/ adding the to a user group
#/ crates a dir for sat game_control to be run form arg $3
#/ and updating the new dir to be owned but the new user and group
#/
#/ written by Andrew Mcgregor <a-mcgregor381@protonmail.com>


USER=$(unset)
GAME=$(unset)
GAMEPATH=$(unset)



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
    -h | --help)  HELP=1        usage    ;;
    -u | --user)  USER="$2"     shift 2  ;;
    -g | --game_control)  GAME="$2"     shift 2  ;;
    -r | --group) GROUP="$2" shift 2  ;;
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


echo  "$HELP $USER+$GAME $USER $GAME $GAMEPATH"


echo "creating new no login user '$USER' for managing this game server"
adduser --disabled-login --no-create-home --gecos "$USER $GROUP"
