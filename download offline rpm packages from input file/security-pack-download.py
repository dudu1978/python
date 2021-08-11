import os
none_strip_package_list = []
package_list =[]
download_dir_path ='/opt/file'


def yum_download (package_list):
    for package in package_list:
        print('yum install --downloadonly --downloaddir='+download_dir_path +'  '+package)
        os.system('yum install --downloadonly --downloaddir='+download_dir_path+'  '+ package)


# Using readlines()

file_packages = open('package.txt', 'r')
lines = file_packages.readlines()
for line in lines:
    #print (line)
    none_strip_package_list.append(line)

for element in none_strip_package_list:
    package_list.append(element.strip())
print (package_list)

yum_download (package_list)
