import os
from shared.utils.constants import ROOT
from shared.utils.time import now

metadata_path = os.path.join(ROOT, 'shared', 'utils', 'metadata.py')

def update_constant():
    content = [
        'LAST_UPDATED = \'%s\'' % now(True),
        '',
    ]
    with open(metadata_path, 'w') as f:
        f.write('\n'.join(content))
