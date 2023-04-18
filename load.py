import torch
#pthfile = r'/common-data/kehanwang/mace-main/checkpoint_longkunfreeze/MACE_model_run-123_epoch-6.pt'
pthfile = '/data/test_cp2k/cp2k_two_double/freeze/checkpointsft/MACE_model_run-123.model'#'/data/test_cp2k/lammps_two_double/checkpointsft/MACE_model_run-123.model'
device = torch.device('cpu')
net = torch.load(pthfile,map_location=device)
model_config = dict(atomic_energies = [0,0,0])
net.scale_shift.scale = torch.tensor(0.994186)
net.scale_shift.shift = torch.tensor(-18815.428617)

net.atomic_energies_fn.atomic_energies = torch.tensor([ 0, 0, 0], dtype=torch.float64)
print(net)
torch.save(net,'1.model')
'''
import torch
import torchvision.models as models


net = models.squeezenet1_1(pretrained=False)
pthfile = r'/common-data/kehanwang/mace-main/checkpoint_longkunfreeze/MACE_model_run-123_epoch-6.pt'
net.load_state_dict(torch.load(pthfile))
print(net)
'''
