# -*- coding: utf-8 -*-
import os
import time
import codecs
start_path = u'/media'
tags = [u'-мкрк', u'-диз', u'мкрк-', u'диз-']
count_of_target_files_in_folder = 0
folders_collection = {}
current_folder_number = 0
for current_folder, folders, files in os.walk(start_path):    
    count_of_target_files_in_folder = 0
    current_folder_number = current_folder_number + 1
    for current_file in files:
        for current_tag in tags:
            if current_tag in current_file:
                count_of_target_files_in_folder\
                    = count_of_target_files_in_folder + 1
                if count_of_target_files_in_folder == 1:
                    current_path_of_file\
                        = current_folder + u'/' + current_file
                    date_of_the_first_target_file_in_folder__unix\
                        = time.gmtime(os.stat(current_path_of_file).st_mtime)
                    date_of_the_first_target_file_in_folder__human_cn\
                        = time.strftime(u'%Y-%m-%d'\
                        , date_of_the_first_target_file_in_folder__unix)
                    target_folder_id\
                        = date_of_the_first_target_file_in_folder__human_cn\
                        + u'-f'\
                        + str(current_folder_number)
                break
        continue # searching files
    if count_of_target_files_in_folder > 0:
        folders_collection[target_folder_id]\
            = [len(files)\
            , count_of_target_files_in_folder\
            , current_folder]
current_time__unix = time.localtime()
current_time__human_cn\
    = time.strftime(u'%Y-%m-%d_%H-%M-%S', current_time__unix)
index_root = u'trigger-index'
folders_index_path\
    = u'./' + index_root + u'/'\
    + current_time__human_cn + u'_folders-index.txt'
with codecs.open(folders_index_path, 'a', encoding='utf-8') as f:
    for i, id_ in enumerate(folders_collection):
        folders_index_string = u'{}\t{}\t{}\t{}'\
            .format\
            ( folders_collection[id_][0]\
            , folders_collection[id_][1]\
            , id_\
            , folders_collection[id_][2]\
            )
        f.write(folders_index_string)
        f.write(u'\n')
