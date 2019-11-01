
# REFERENCES:
# https://www.simba.com/drivers/bigquery-odbc-jdbc/
# https://github.com/mkleehammer/pyodbc
# https://www.cdata.com/kb/tech/bigquery-odbc-python-linux.rst

sudo yum install epel-release
sudo yum install python-pip gcc-c++ python-devel unixODBC-devel
sudo pip install pyodbc

echo ""
echo ""
echo ""
echo "Step 1: Download Simba BigQuery ODBC Driver for Linux from here: https://www.simba.com/drivers/bigquery-odbc-jdbc/"
echo ""
echo "Step 2: Unzip the download file"
echo ""
echo "Step 3: Run yum --nogpgcheck localinstall [RPMFileName] to install the driver"
echo ""
echo "Step 4: Copy license file (which should have been emailed when you downloaded the .zip driver file"
echo ""
echo "Step 5: Update odbc.ini as needed and copy to /etc/odbc.ini"
echo ""
echo "Step 6: Update odbcinst.ini as needed and copy to /etc/odbcinst.ini"
echo ""
echo ""
