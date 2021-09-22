## This script output the latest file version located on a website
## This script will fetch all files in the following format "bigdata-<number>.<number>.<number>.tar"
# 1. list all the files on a website
# 2. Using regex extract the version
# 3. Print the latest version

For example:
When browsing to webserver http://1.1.1.1/project/release-1/ you will have the follwoing files 
bigdata-10.1.1.2.tar
bigdata-10.1.1.9.tar
bigdata-10.1.1.12.tar
bigdata-10.1.1.20.tar

The Script will print teh file bigdata-10.1.1.20.tar
