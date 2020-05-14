# - Find FFTW
# Find the native FFTW includes and library
#
#  FFTW_INCLUDES    - where to find fftw3.h
#  FFTW_LIBRARIES   - List of libraries when using FFTW.
#  FFTW_FOUND       - True if FFTW found.

if (FFTW_INCLUDES)
  # Already in cache, be silent
  set (FFTW_FIND_QUIETLY TRUE)
endif (FFTW_INCLUDES)

find_path (FFTW_INCLUDES fftw3.h)

find_library (FFTW3F_OMP NAMES fftw3f_omp)
find_library (FFTW3_MPI NAMES fftw3_mpi)
find_library (FFTW3F_MPI NAMES fftw3f_mpi)
find_library (FFTW3L_OMP NAMES fftw3l_omp)
find_library (FFTW3L NAMES fftw3l)
find_library (FFTW3F_THREADS NAMES fftw3f_threads)
find_library (FFTW3_OMP NAMES fftw3_omp)
find_library (FFTW3_THREADS NAMES fftw3_threads)
find_library (FFTW3L_THREADS NAMES fftw3l_threads)
find_library (FFTW3 NAMES fftw3)
find_library (FFTW3F NAMES fftw3f)
find_library (FFTW3L_MPI NAMES fftw3l_mpi)

# handle the QUIETLY and REQUIRED arguments and set FFTW_FOUND to TRUE if
# all listed variables are TRUE
include (FindPackageHandleStandardArgs)
find_package_handle_standard_args (FFTW DEFAULT_MSG FFTW_LIBRARIES FFTW_INCLUDES)

mark_as_advanced (FFTW_LIBRARIES FFTW_INCLUDES)
