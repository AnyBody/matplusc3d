# -*- coding: utf-8 -*-
import os

import click

from matplusc3d import combine_files


@click.command()
@click.argument('c3dfile', metavar='[filename.c3d]', required=False, type=click.Path())
@click.option('--overwrite', is_flag=True, help="Overwrite existing c3dfiles. "
              "If not set, a file new file 'filename_updated.c3d' will be created")
def main(c3dfile, overwrite):
    """Command line tool for adding virtual makers to Coda Motion
       C3D files from the information in exported Mat files.

       The tool assume the c3d and mat files have the same filename
       but different extensions. If called without arguments the tool
       will find all matching c3d/mat files in the working directory.

    """

    if not c3dfile:
        click.confirm('Combine all C3D/Mat files in current dir?', abort=True)
        filelist = [(f, os.path.splitext(f)[0]+'.mat')
                     for f in os.listdir('.') if f.upper().endswith('.C3D')]
    elif os.path.isfile(c3dfile):
        matfile = os.path.splitext(c3dfile)[0]+'.mat'
        if not os.path.isfile(matfile):
            raise click.UsageError('No mat file found matching {}'
                                   ''.format(c3dfile))
        filelist = [(c3dfile, matfile)]
    else:
        raise click.UsageError('No such file {}'.format(c3dfile))

    filelist = [(str(f), str(m)) for f, m in filelist
                if os.path.exists(f) and os.path.exists(m)]

    for c3dfile, matfile in filelist:
        postfix = '' if overwrite else '_updated'
        new_c3d = combine_files(c3dfile, matfile, postfix=postfix)
        print('Updated: {}'.format(new_c3d))



if __name__ == "__main__":
    main()

