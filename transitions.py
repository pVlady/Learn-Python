from transitions import Machine

# object with different states
class Matter(object):
    pass

lump = Matter()

# list of the states
states=['solid', 'liquid', 'gas', 'plasma']

# state transition table
transitions = [
    { 'trigger': 'melt', 'source': 'solid', 'dest': 'liquid' },
    { 'trigger': 'evaporate', 'source': 'liquid', 'dest': 'gas' },
    { 'trigger': 'sublimate', 'source': 'solid', 'dest': 'gas' },
    { 'trigger': 'ionize', 'source': 'gas', 'dest': 'plasma' }
]

# machine initializing
machine = Machine(lump, states=states, transitions=transitions, initial='liquid')

# check initial state
lump.state
>>> 'liquid'

# try to change state using tiggers
lump.evaporate()
lump.state
>>> 'gas'
lump.trigger('ionize')
lump.state
>>> 'plasma'
