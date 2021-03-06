from __future__ import print_function

import os
import h5py

DEBUG = True

using_in_memory = False

# dataset_source_type = 'hdf5 file paths'
dataset_source_type = h5py.File

path_to_training_datasets = '/groups/turaga/home/turagas/data/FlyEM/fibsem_medulla_7col/'
path_to_testing_datasets = '/groups/turaga/home/turagas/data/FlyEM/fibsem_medulla_7col/'
testing_dataset_names = ['trvol-250-2-h5']
dvid_uuid = 'e402c09ddd0f45e980d9be6e9fcb9bd0'

training_dataset_names = os.listdir(path_to_training_datasets)
training_dataset_names = [n for n in training_dataset_names if 'trvol-250-1' in n]
if DEBUG or True:
    training_dataset_names = training_dataset_names[0:1]

using_filenames = dataset_source_type == 'hdf5 file paths'


