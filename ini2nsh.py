
#-------------------------------------------------------------------------------
# Name:        ini2nsh
# Purpose:
#
# Author:      Darko Boto darko.boto@gmail.com
# Description: Parse qgis customization .ini file and generate nsis .nsh file for windows registry setup
# Created:     14.04.2014
# Copyright:   (c) darko.boto 2014
# Licence:     MIT
#-------------------------------------------------------------------------------
import os

def main():

    in_file = 'cutomization.ini'
    out_file = 'cutomization.nsh'

    # -- open qgis customization ini file
    qgis_inifile = open(in_file, 'r')

    # -- create and open out reg2nsis .nsh file
    if os.path.exists(out_file):
        os.remove(out_file)
    reg_outfile = open(out_file,'w')
    # -- read lines i input file
    for line in qgis_inifile:

        # -- registy structure
        reg_cmd = 'WriteRegStr'
        reg_key = 'HKEY_CURRENT_USER'
        reg_keys = ' "Software\\QGIS\\QGISCUSTOMIZATION2\\Customization\\'
        reg_subkeys = line.rsplit('\\', 1)[0]
        reg_name = line.split('\\')[-1].split('=')[0]
        reg_data = line.split('=', 1)[-1].strip()

        # -- exclude customization header
        if line.startswith("["):
            print line
        # -- write QGISCUSOMIZATION2 root keys
        elif len(line.split('\\')) == 1:
            reg_outfile.write(reg_cmd + ' ' +  reg_key + ' ' + reg_keys[:-1] + '" ' + ' "' + reg_name + '" "' + reg_data + '"\n')
        # -- write other keys
        else:
            reg_outfile.write(reg_cmd + ' ' + reg_key + ' ' + reg_keys + reg_subkeys + '" "' + reg_name + '" "' + reg_data + '"\n')

    reg_outfile.close()
    qgis_inifile.close()
if __name__ == '__main__':
    main()
