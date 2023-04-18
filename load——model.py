import torch
#pthfile = r'/common-data/kehanwang/mace-main/checkpoint_longkunfreeze/MACE_model_run-123_epoch-6.pt'
pthfile = '/data/test_cp2k/cp2k_two_double/checkpointsft_kcal/MACE_model_run-123.model'
device = torch.device('cpu')
#net = torch.load(pthfile,map_location=device)
pthfile ='/data/test_cp2k/cp2k_two_double/checkpointsft_kcal/MACE_model_run-123_epoch-434.pt'
l = torch.load(pthfile,map_location=device)
#net.load_state_dict(l['model'])
print(l['model'])#['atomic_energies_fn.atomic_energies'].dtype)

l['model']['atomic_energies_fn.atomic_energies'] =  torch.tensor([ 0, 0, 0], dtype=torch.float32)
l['model']['scale_shift.scale'] = torch.tensor(0.994186)
l['model']['scale_shift.shift'] = torch.tensor(-18815.428617)
l['optimizer']['param_groups'][0]['lr'] =   0
l['optimizer']['param_groups'][1]['lr'] =   0
l['optimizer']['param_groups'][2]['lr'] =   0
l['optimizer']['param_groups'][3]['lr'] =   0
l['optimizer']['param_groups'][4]['lr'] =   0.01

l = l.to(torch.float32)
torch.save(l,'MACE_model_run-123_epoch-434.pt')
