from modules.optim.adam import AdamOptim
from modules.optim.adabelief import AdaBeliefOptim
from modules.optim.scheduler import ScheduledOptim
from modules.optim.adamW import AdamWOptim

optimizers = {"Adam": AdamOptim, "AdaBelief": AdaBeliefOptim, "AdamW": AdamWOptim}
