# -*- coding: utf-8 -*-
import optparse
import os
import sys
import json
from datetime import datetime

# config file name
config_file_name = "ipa-package-config.file"
# project name
project_name = None
# tag name
tag_name = None
# project path(default path for the execution of the current script)
project_path = os.getcwd()
# output folder name
out_out_dir_name = "Output"
# certificate name
certificate_name = None
# provisioning profile name
provisioning_profile_name = None
# tag version
tag_version = None
# fir token (Optional)
fir_token = None
# address when ipa uplaod fir.im success(Optional)
fir_address = None
# build date (y-m-r h:m:s)
config_date = None

# Welcome message
def welcome_message():
    print "======================================"
    print "Welcome to the ipa packaged script."
    print "Version:     1.0.0"
    print "Platform:    python 2.7"
    print "Contact:     kepenj@gmail.com"
    print "======================================="

# init option info
def init_config():
    p = optparse.OptionParser()
    # config option
    p.add_option("--edit", "-e", action="store_true", default=None, help="edit file about config")
    p.add_option("--config", "-c", action="store_true", default=None, help="show config file content")
    options, arguments = p.parse_args()

    # show config file info
    if options.config == True and len(arguments) == 0:
        read_config_file()
        show_config_content()
        sys.exit()
    # edit config file
    if options.edit == True and len(arguments) == 0:
        input_config_data()
        sys.exit()

# determine whether the string is empty
def is_empty(string):
    if string == None or len(string) == 0:
        return True
    else:
        return False

# config file and inti data
def init_config_file_and_data():
    global out_out_dir_name
    global project_path
    # Output folder if not , create one
    if not os.path.exists(project_path + '/' + out_out_dir_name):
        os.system("cd %s;mkdir %s" % (project_path, out_out_dir_name))
        os.system("chmod -R 777 %s" % out_out_dir_name)

    # no config file, create one
    if not os.path.isfile(project_path + '/' + out_out_dir_name + '/' + config_file_name):
        os.system("cd %s;touch %s" % (project_path + '/' + out_out_dir_name, config_file_name))
        # create config file
        init_config_file()
        # input config data
        input_config_data()
    else:
        # read file information
        read_config_file()
        if not isd_data_available():
            input_config_data()


# init the config file contents
def init_config_file():
    global config_file_name
    global project_path
    global out_out_dir_name
    global tag_name

    fout = open(project_path + '/' + out_out_dir_name + '/' + config_file_name, 'w')
    js = {}
    js["tag_version"] = "1.0.0"
    js["provisioning_profile_name"] = None
    js["project_path"] = None
    js["project_name"] = None
    js["tag_name"] = None
    js["certificate_name"] = None
    js["fir_token"] = None
    js["config_date"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    outStr = json.dumps(js)
    fout.write(outStr.strip().encode('utf-8') + '\n')
    fout.close()


# inti data
def input_config_data():
    os.system("clear")
    global certificate_name
    global project_path
    global project_name
    global fir_token
    global provisioning_profile_name
    global tag_version
    global tag_name

    print "Please enter the following parameters:"
    # show config file info
    show_config_content()
    project_path = raw_input("input project dir path:")
    # determine whether the project path of the current input is empty
    if is_empty(project_path):
        print "Project dir path is empty！"
        sys.exit()
    # analyzing the current out of the project path is available
    if not os.path.exists(project_path):
        print "Can not find this project dir!"
        sys.exit()
    project_name = raw_input("input project name:")
    # analyzing the current project name is empty
    if is_empty(project_name):
        print "project name is empty！"
        sys.exit()
    tag_name = raw_input("input tag name:")
    # analyzing the current project name is empty
    if is_empty(tag_name):
        print "Tag name is empty！"
        sys.exit()
    certificate_name = raw_input("input certificate name:")
    # determining whether the current certificate is empty
    if is_empty(certificate_name):
        print "Certificate is empty！"
        sys.exit()
    provisioning_profile_name = raw_input("input provisioning profile name:")
    # determine whether the current configuration file is empty
    if is_empty(provisioning_profile_name):
        print "Provisioning profile is empty！"
        sys.exit()
    fir_token = raw_input("input fir token (Optional):")
    tag_version = raw_input("input release tag version:")
    if is_empty(tag_version):
        tag_version = "1.0.0"
    # saved locally
    write_config_file()

# display configuration information
def show_config_content():
    global certificate_name
    global provisioning_profile_name
    global project_path
    global project_name
    global fir_token
    global tag_version
    global tag_name

    print "************CONFIG FILE*******************"
    print "PROJECT PATH:                %s" % project_path
    print "TAG NAME:                    %s" % tag_name
    print "PROJECT NAME:                %s" % project_name
    print "TAG VERSION:                 %s" % tag_version
    print "CERTIFICATE NAME:            %s" % certificate_name
    print "PROVISIONING PROFILE NAME:   %s" % provisioning_profile_name
    print "FIR TOKEN(Optional):         %s" % fir_token
    print "************CONFIG FILE********************"

# read config file contents
def read_config_file():
    global out_out_dir_name
    global certificate_name
    global provisioning_profile_name
    global project_path
    global project_name
    global fir_token
    global config_date
    global tag_version
    global tag_name

    fin = open(project_path + '/' + out_out_dir_name + '/' + config_file_name, 'r')
    for each_line in fin:
        line = each_line.strip().decode('utf-8')
        line = line.strip(',')
        js = None
        try:
            js = json.loads(line)
            provisioning_profile_name = js["provisioning_profile_name"]
            project_path = js["project_path"]
            project_name = js["project_name"]
            tag_name = js["tag_name"]
            certificate_name = js["certificate_name"]
            fir_token = js["fir_token"]
            config_date = js["config_date"]
            tag_version = js["tag_version"]

        except Exception, e:
            print Exception
            print e
            continue
    fin.close()


# saved local
def write_config_file():
    global provisioning_profile_name
    global certificate_name
    global project_path
    global project_name
    global fir_token
    global out_out_dir_name
    global tag_version
    global tag_name

    fout = open(project_path + '/' + out_out_dir_name + '/' + config_file_name, 'w')
    js = {}
    js["provisioning_profile_name"] = provisioning_profile_name
    js["project_path"] = project_path
    js["project_name"] = project_name
    js["tag_name"] = tag_name
    js["certificate_name"] = certificate_name
    js["fir_token"] = fir_token
    js["config_date"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    js["tag_version"] = tag_version

    outStr = json.dumps(js)
    fout.write(outStr.strip().encode('utf-8') + '\n')
    fout.close()


# determining whether the current data available
def isd_data_available():
    global certificate_name
    global project_path
    global project_name
    global provisioning_profile_name
    global tag_name

    if is_empty(project_path) or is_empty(project_name) or is_empty(tag_name) or is_empty(certificate_name) or is_empty(provisioning_profile_name):
        return False
    else:
        return True

# cleanup pbxproj file
def clean_project():
    global all_the_text
    global project_path
    global project_name
    global tag_name

    print "Cleanup project..."
    os.system("cd %s;xcodebuild -target '%s' clean" % (project_path, tag_name))

    print "Cleanup pbxproj file..."
    path = "%s/%s.xcodeproj/project.pbxproj" % (project_path, project_name)
    file_object = open(path)
    try:
        all_the_text = file_object.readlines()
        for text in all_the_text:
            if 'PROVISIONING_PROFILE' in text:
                all_the_text.remove(text)
    finally:
        file_object.close()

    file_object = open(path, 'w')
    try:
        for text in all_the_text:
            file_object.write(text)
    finally:
        file_object.close()
    return


# create ipa
def build_creat_ipa():
    global project_path
    global certificate_name
    global config_date
    global provisioning_profile_name
    global tag_version
    global tag_name

    # build
    print "Build project..."
    os.system("cd %s;xcodebuild -configuration Release -target '%s' CODE_SIGN_IDENTITY='%s' PROVISIONING_PROFILE='%s'" % (project_path, tag_name, certificate_name,provisioning_profile_name))
    # if you do not Release_xx folder , then create one
    if os.path.exists(project_path + '/' + out_out_dir_name+'/'+"Release_%s"%(tag_version)):
        print "Emptying the previous folder..."
        # empty the contents of the original folder and below
        os.system("cd %s;rm -r -f %s" %(project_path + '/' + out_out_dir_name+'/',"Release_%s"%(tag_version)))

    print "Creating new folders..."
    # create a new folder
    os.system("cd %s;mkdir %s" % (project_path + '/' + out_out_dir_name, "Release_%s"%(tag_version)))
    os.system("chmod 777 %s" %"Release_%s"%(tag_version))
    # generate ipa file
    print "Generating ipa file..."
    # find .app file
    file = find_file('.app',"%s/build/Release-iphoneos"%project_path)
    if is_empty(file):
        print "Do not have .app file!"
        sys.exit()
    file_name = file[0:len(file)-len('.app')]
    os.system(
        "cd %s;xcrun -sdk iphoneos PackageApplication -v %s/build/Release-iphoneos/'%s'.app -o %s/'%s'.ipa CODE_SIGN_IDENTITY='%s' PROVISIONING_PROFILE='%s'" % (
            project_path, project_path,file_name, project_path + '/' + out_out_dir_name+'/'+"Release_%s"%(tag_version),file_name, certificate_name,provisioning_profile_name))

    # the translation of the build / Release-iphoneos / folder below the content over this new folder inside
    os.system("cp -R %s/build/Release-iphoneos/ %s/%s/Release_'%s'/" % (project_path, project_path, out_out_dir_name, tag_version))
    # delete the previous build / folder below the content
    os.system("cd %s;rm -r -f %s" % (project_path,"./build"))
    # record Time
    config_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    write_config_file()
    return

# upload fir.im (Optional)
def upload_to_fir():
    global fir_token
    global tag_name
    global project_path
    global out_out_dir_name
    global fir_address

    fir_address = ""
    if not is_empty(fir_token):
        if os.path.exists("%s/'%s'/Release_'%s'/'%s'.ipa" % (project_path,out_out_dir_name,tag_version, tag_name)):
            print "Uploading fir..."
            ret = os.popen("fir p '%s/%s/Release_%s/'%s'.ipa' -T '%s'" % (project_path,out_out_dir_name,tag_version, tag_name, fir_token))
            for info in ret.readlines():
                if "Published succeed" in info:
                    location = info.find('http://')
                    if location < len(info):
                        fir_address = info[location:len(info)]
                    break
        else:
            print "Cant find ipa file."

    os.system('open %s' % (project_path + '/' + out_out_dir_name))
    return fir_address

#find .app file
def find_file(file,dir_path):
    for root, subFolders, files in os.walk(dir_path):
        for f in subFolders:
            if f[-4:] == file:
                return f

if __name__ == '__main__':
    os.system("clear")

    welcome_message()

    init_config()

    init_config_file_and_data()

    show_config_content()

    clean_project()

    build_creat_ipa()


    url = upload_to_fir()
    if not is_empty(url):
        os.system("clear")
        print "**********UPLOAD SUCCESS**********"
        print "TAG NAME:            '%s'"%tag_name
        print "FIR ADDRESS:         '%s'"%fir_address
        print "RELEASE VERSION:     '%s'"%tag_version
        print "DATE:                '%s'"%datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print "**********UPLOAD SUCCESS**********"

    # root = "%s/build/Release-iphoneos/"%project_path
    # print "root=",root
    # file = find_file('.app',"%s/build/Release-iphoneos/"%project_path)
    # print "file=",file
    # file_name = file[0:len(file)-len('.app')]
    # print "file_name=",file_name