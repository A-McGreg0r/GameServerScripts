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

HELP=$(unset)
USER=$(unset)
GAME=$(unset)
INSTALL_PATH=$(unset)

USER=factorio
GAME=factorio
GROUP=gamehosts
VERSION=1.1.61
#todo get full path form server

#todo update
usage()
{
 echo "Usage: create_user.sh [options] [--] [<shell-script>...]"
 echo " -h,  --help        show help text"
 echo " -u,  --user        user to be created normally the game-name (Required)"
 echo " -g,  --game        the name of the game that is bein installed (Required)"
 echo " -gp, --group       user group to be created and add user to (Required)"
 echo " -p,  --path        path of the games install location (Optional) over writes default opt/GAME"


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
    -h | --help)    HELP=1         usage    ;;
    -u | --user)    USER="$2"      shift 2  ;;
    -g | --game_control)    GAME="$2"      shift 2  ;;
    -r | --group)   GROUP="$2"     shift 2  ;;
    -p | --path)    INSTALL_PATH="$2"  shift 2  ;;
    -v | --version) VERSION="$2"   shift 2  ;;
    -d | --debug)   DEBUG=1        shift 2  ;;
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

# $GAME will determans the custome instill path will defult to /opt/$GAME
if [ "$INSTALL_PATH" == "" ]; then
  echo "creating dir for game $GAME in $INSTALL_PATH"
  mkdir "$INSTALL_PATH"
  chown -R "$USER:$GROUP" "$INSTALL_PATH"
else
  echo "creating dir for game $GAME in /opt/$GAME"
  mkdir "/opt/$GAME"
  chown -R "$USER:$GROUP" "/opt/$GAME"
  INSTALL_PATH="/opt/$GAME"
fi


# todo need to some how be able to swap easily between games
echo "downloading $GAME to $INSTALL_PATH"
wget -O factorio_headless.tar.gz "https://www.factorio.com/get-download/$VERSION/headless/linux64"  -P $INSTALL_PATH
tar -xzf $INSTALL_PATH/factorio_headless.tar.gz

# creating a user
echo starting to creat a user
source createUser

