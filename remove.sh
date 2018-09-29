INSTALL_ROOT=/usr/share/openstack-dashboard
if [ ! -z "$1" ]
        then
	INSTALL_ROOT=$1
fi
echo "Removing Stella_Horizon "
echo "OpenStack Dashboard Root folder: $INSTALL_ROOT"
sleep 3

DESTN_DIR=$INSTALL_ROOT/openstack_dashboard/enabled
echo "About to Delete enabled file from $DESTN_DIR"
sleep 3
rm -i $DESTN_DIR/_50_stella_openstack.py

DESTN_DIR=$INSTALL_ROOT/openstack_dashboard/api/
echo "About to Delete API files from $DESTN_DIR"
sleep 3
rm -i $DESTN_DIR/cloudbuilder_neutron.py

DESTN_DIR=$INSTALL_ROOT/openstack_dashboard/dashboards
echo "About to Delete dashboard code from $DESTN_DIR"
sleep 3
rm -ir $DESTN_DIR/cloudbuilder/ 

service apache2 restart