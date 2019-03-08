import os
import tempfile
import subprocess


def run_with_config(command, config):
    myinput = open(config)
    p = subprocess.Popen(command, stdin=myinput)
    p.wait()


def autoslic_config(inputfile, ncell=(1, 1, 1), output_file=None, beam_energy=60, wavefunction_size=(512, 512),
                    slice_thickness=5):
    partial_coherence='n'
    start_from_previous_result='n'
    tilt = (0, 0)
    record_beam_vs_thickness='n'
    thermal_vibrations='n'
    intensity_vs_cross_section='n'

    if output_file is None:
        output_file = tempfile.mktemp(suffix='.tiff')

    config_file = tempfile.mktemp(prefix='autoslic_config_')
    with open(config_file, 'w') as f:
        f.write('{}\n'.format(inputfile))
        f.write('{} {} {}\n'.format(ncell[0], ncell[1], ncell[2]))
        f.write('{}\n'.format(output_file))
        f.write('{}\n'.format(partial_coherence))
        f.write('{}\n'.format(start_from_previous_result))
        f.write('{}\n'.format(beam_energy))
        f.write('{} {}\n'.format(wavefunction_size[0], wavefunction_size[1]))
        f.write('{} {}\n'.format(tilt[0], tilt[1]))
        f.write('{}\n'.format(slice_thickness))
        f.write('{}\n'.format(record_beam_vs_thickness))
        f.write('{}\n'.format(thermal_vibrations))
        f.write('{}\n'.format(intensity_vs_cross_section))
    return config_file, output_file


def run_autoslic(inputfile, ncell=(1, 1, 1), output_file=None, beam_energy=60, wavefunction_size=(512, 512),
                 slice_thickness=5):
    config, output = autoslic_config(inputfile, ncell=ncell, output_file=output_file, beam_energy=beam_energy,
                                     wavefunction_size=wavefunction_size, slice_thickness=slice_thickness)
    run_with_config('./build/autoslic', config)
    return output


def image_config(inputfile, outputfile, Cs3=0, Cs5=0, defocus=0, aperture_size=30, two_fold_astigmatism=(0, 0),
                three_fold_astigmatism=(0, 0), lens_center=(0, 0)):
    image_type = 0 # coherent real space image
    config_file = tempfile.mktemp(prefix='image_config_')
    with open(config_file, 'w') as f:
        f.write('{}\n'.format(inputfile))
        f.write('{}\n'.format(image_type))
        f.write('{}\n'.format(outputfile))
        f.write('{} {}\n'.format(Cs3, Cs5))
        f.write('{}\n'.format(defocus))
        f.write('{}\n'.format(aperture_size))
        f.write('{} {}\n'.format(two_fold_astigmatism[0], two_fold_astigmatism[1]))
        f.write('{} {}\n'.format(three_fold_astigmatism[0], three_fold_astigmatism[1]))
        f.write('{} {}\n'.format(lens_center[0], lens_center[1]))
    return config_file

def run_image(inputfile, outputfile, Cs3=0, Cs5=0, defocus=0, aperture_size=30, two_fold_astigmatism=(0, 0),
              three_fold_astigmatism=(0, 0), lens_center=(0, 0)):
    config = image_config(inputfile, outputfile, Cs3=Cs3, Cs5=Cs5, defocus=defocus, aperture_size=aperture_size,
                          two_fold_astigmatism=two_fold_astigmatism, three_fold_astigmatism=three_fold_astigmatism,
                          lens_center=lens_center)
    run_with_config('./build/image', config)
