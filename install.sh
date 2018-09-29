INSTALL_ROOT=/usr/share/openstack-dashboard
if [ ! -z "$1" ]
        then
	INSTALL_ROOT=$1
fi
DIR_PATH=$(dirname $0)
echo "Installing Stella_Horizon "
echo "Directory path for the script: $DIR_PATH"
echo "OpenStack Dashboard Root folder: $INSTALL_ROOT"
sleep 3

SOURCE_FILES=$DIR_PATH/openstack_dashboard/enabled/*.py
DESTN_DIR=$INSTALL_ROOT/openstack_dashboard/enabled/
echo "About to copy enabled file from $SOURCE_FILES to $DESTN_DIR"
sleep 3
cp $SOURCE_FILES $DESTN_DIR

SOURCE_FILES=$DIR_PATH/openstack_dashboard/api/*.py
DESTN_DIR=$INSTALL_ROOT/openstack_dashboard/api/
echo "About to copy API files from $SOURCE_FILES to $DESTN_DIR"
sleep 3
cp $SOURCE_FILES $DESTN_DIR

SOURCE_FILES=$DIR_PATH/openstack_dashboard/dashboards/*
DESTN_DIR=$INSTALL_ROOT/openstack_dashboard/dashboards
echo "About to copy dashboard code from $SOURCE_FILES to $DESTN_DIR"
sleep 3
cp -R $SOURCE_FILES $DESTN_DIR

