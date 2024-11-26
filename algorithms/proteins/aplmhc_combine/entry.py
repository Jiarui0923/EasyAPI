id='combine-apl-mhc'
name='Weighted Combine APL And MHC'
description='Combine APL and MHC values use a given weight.'
version='0.0.1'
references=[]
required_resources={'cpu':-1, 'cuda':0}
_types = {
    'float>1': dict(id='float-greater-than-1',
                meta='number',
                name='float>1',
                doc='The float number that is greater than 1.',
                condition={'min':1},
                version='0.0.1'),
    'float>0': dict(id='float-greater-than-0',
                meta='number',
                name='float>0',
                doc='The float number that is greater than 0.',
                condition={'min':0},
                version='0.0.1'),
    'float>=0': dict(id='float-greater-equal-than-0',
                meta='number',
                name='float>=0',
                doc='The float number that is greater or equal than 0.',
                condition={'min':-0.0001},
                version='0.0.1'),
    'peptide_likelihood': dict(id='apl-peptide-likelihood',
                 meta='numarray',
                 name='Peptide Likelihood',
                 doc='Peptide Level Likelihood',
                 condition=None,
                 version='0.0.1'),
    'json': dict(id='json',
                meta='string',
                name='JSON File',
                doc='The JSON format file',
                condition=None,
                version='0.0.1'),
}
in_params={
    'apl': dict(io_type=_types['peptide_likelihood'],
                                default_value=None,
                                desc='Peptide Level Likelihood.'),
    'mhc': dict(io_type=_types['json'],
                     default_value=None,
                     desc='The MHC-II binding outputs from IEDB following JSON formats'),
    'w_apl': dict(io_type=_types['float>0'],
                   default_value=0.5,
                   desc='The weight for APL. The weight for MHC will be `1-w_apl`.'),
    'apl_threshold': dict(io_type=_types['float>=0'],
                   default_value=0,
                   desc='The threshold for APL. If the value is smaller than this threshold, it will be ignored.'),
    'mhc_threshold': dict(io_type=_types['float>=0'],
                   default_value=0,
                   desc='The threshold for MHC. If the value is smaller than this threshold, it will be ignored.'),
}
out_params={
    'combined': dict(io_type=_types['json'],
                     default_value=None,
                     desc='Combined APL-MHC values for each MHC class.'),
}

from aplmhc_combine import combine_APL_MHC
import pandas as pd
from pandas.api.types import is_float_dtype
import io
def main(apl, mhc, w_apl=0.5, apl_threshold=0, mhc_threshold=0, resources={}):
    _mhc_df = pd.read_json(io.StringIO(mhc))
    _outputs = {}
    for column in _mhc_df.columns:
        if not is_float_dtype(_mhc_df[column]): _outputs[column] = _mhc_df[column].values
        else:
            _combined = combine_APL_MHC(structure=apl, MHC=_mhc_df[column].to_list(), r=w_apl, TProc=apl_threshold, TMHC=mhc_threshold)
            _outputs[column] = _combined
    _outputs = pd.DataFrame(_outputs).to_json(index=False)
    return dict(combined=_outputs)
