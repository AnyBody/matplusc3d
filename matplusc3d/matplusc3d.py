# -*- coding: utf-8 -*-
import os

from scipy.io import loadmat

try:
    import btk
except ImportError:
    raise ImportError

def open_acqusition(c3d_file):
    """ Opens a c3d file with BTK """
    reader = btk.btkAcquisitionFileReader()
    reader.SetFilename(c3d_file)
    reader.Update()
    return reader.GetOutput()

def write_acqusition(acq, c3d_file, postfix=''):
    """ Writes an acqusition back to a C3D file """
    writer = btk.btkAcquisitionFileWriter()
    writer.SetInput(acq)
    c3dfile = postfix.join(os.path.splitext(c3d_file))
    writer.SetFilename(c3dfile)
    writer.Update()
    return c3dfile




def combine_files(c3d_file, mat_file, postfix='_Updated'):
    """ Combine a c3d file with the 'RefPoints' markers from a corresponding
        mat file 
    """
    c3dacq = open_acqusition(c3d_file)
    acq_frames = c3dacq.GetPointFrameNumber()
    
    matobj = loadmat(mat_file, struct_as_record=False, squeeze_me=True)
    
    for refname in matobj['RefPoint']._fieldnames:
        value = getattr(matobj['RefPoint'],refname).value
        if value.shape[0] != acq_frames:
            raise ValueError('The number of frames in the C3D file ({}) and '
                             'the mat file ({}) does not match'
                             ''.format(acq_frames, value.shape[0]))
        point = btk.btkPoint(acq_frames)
        point.SetLabel(refname)
        point.SetValues(value) 
        c3dacq.AppendPoint(point)
    
    
    updated_filename = write_acqusition(c3dacq, c3d_file, postfix=postfix)
    return updated_filename



if __name__ == '__main__':
    datadir = os.path.join(os.path.dirname(__file__), '../tests/data')
    
    c3d_file = os.path.join(datadir,'test.c3d')
    mat_file = os.path.join(datadir,'test.mat')

    dd = combine_files(c3d_file, mat_file)