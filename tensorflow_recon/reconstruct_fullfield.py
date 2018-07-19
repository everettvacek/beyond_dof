from fullfield import reconstruct_fullfield
import numpy as np


params_adhesin = {'fname': 'data_adhesin_360_soft.h5',
                  'theta_st': 0,
                  'theta_end': 2 * np.pi,
                  'n_epochs': 'auto',
                  'alpha_d': 1.e-9,
                  'alpha_b': 1.e-10,
                  'gamma': 0,
                  'learning_rate': 1e-7,
                  'center': 32,
                  'energy_ev': 800,
                  'psize_cm': 0.67e-7,
                  'batch_size': 10,
                  'n_epochs_mask_release': 200,
                  'shrink_cycle': 10,
                  'free_prop_cm': None,
                  'n_batch_per_update': 1,
                  'output_folder': 'test',
                  'cpu_only': True,
                  'save_folder': 'adhesin',
                  'phantom_path': 'adhesin/phantom',
                  'multiscale_level': 1,
                  'n_epoch_final_pass': None,
                  'save_intermediate': True,
                  'full_intermediate': True,
                  'probe_type': 'plane'}

params = params_adhesin

reconstruct_fullfield(fname=params['fname'],
                         theta_st=0,
                         theta_end=params['theta_end'],
                         n_epochs=params['n_epochs'],
                         n_epochs_mask_release=params['n_epochs_mask_release'],
                         shrink_cycle=params['shrink_cycle'],
                         crit_conv_rate=0.03,
                         max_nepochs=200,
                         alpha_d=params['alpha_d'],
                         alpha_b=params['alpha_b'],
                         gamma=params['gamma'],
                         learning_rate=params['learning_rate'],
                         output_folder=params['output_folder'],
                         minibatch_size=params['batch_size'],
                         save_intermediate=params['save_intermediate'],
                         full_intermediate=params['full_intermediate'],
                         energy_ev=params['energy_ev'],
                         psize_cm=params['psize_cm'],
                         cpu_only=params['cpu_only'],
                         save_path=params['save_folder'],
                         phantom_path=params['phantom_path'],
                         multiscale_level=params['multiscale_level'],
                         n_epoch_final_pass=params['n_epoch_final_pass'],
                         initial_guess=None,
                         n_batch_per_update=params['n_batch_per_update'],
                         dynamic_rate=True,
                         probe_type=params['probe_type'],
                         probe_initial=None,
                         probe_learning_rate=1e-3,
                         pupil_function=None)