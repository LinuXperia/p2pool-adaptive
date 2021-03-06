from p2pool.bitcoin import networks

PARENT = networks.nets['dogecoin']
SHARE_PERIOD = 15 # seconds target spacing
CHAIN_LENGTH = 12*60*60//15 # shares
REAL_CHAIN_LENGTH = 12*60*60//15 # shares
TARGET_LOOKBEHIND = 20 # shares coinbase maturity
SPREAD = 10 # blocks
IDENTIFIER = 'D0D1D2D3B2F68CD9'.decode('hex')
PREFIX = 'D0D3D4D541C11DD9'.decode('hex')
P2P_PORT = 29905
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 9555
BOOTSTRAP_ADDRS = 'p2pool.e-pool.net '.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
