cmake_minimum_required(VERSION 3.9)

project(kirkland C CXX)

set(CMAKE_VERBOSE_MAKEFILE OFF)
set(CMAKE_BUILD_TYPE RELEASE)
set(CMAKE_CXX_STANDARD 11)
set(CXX_STANDARD_REQUIRED ON)
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/CMakeModules/")

if (CMAKE_COMPILER_IS_GNUCXX OR (CMAKE_CXX_COMPILER_ID MATCHES "Clang"))
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall")
endif ()

find_package(OpenMP REQUIRED)
if (OPENMP_FOUND)
  set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
endif()

find_package(FFTW REQUIRED)
INCLUDE_DIRECTORIES(${INCLUDE_DIRECTORIES} ${FFTW_INCLUDE_DIRS})
LINK_DIRECTORIES(${LINK_DIRECTORIES} ${FFTW_LIBRARY_DIRS})

add_library(cfpix STATIC cfpix.cpp)
add_library(slicelib STATIC slicelib.cpp)
add_library(floatTIFF STATIC floatTIFF.cpp)
add_library(kirkland_common STATIC cfpix slicelib floatTIFF)

add_executable(atompot atompot.cpp)
target_link_libraries(atompot kirkland_common fftw3f_threads fftw3f)

add_executable(autoslic autoslic.cpp autosliccmd.cpp)
target_link_libraries(autoslic kirkland_common fftw3f_threads fftw3f OpenMP::OpenMP_CXX)

add_executable(autostem autostem.cpp autostemcmd.cpp)
target_link_libraries(autostem kirkland_common fftw3f_threads fftw3f OpenMP::OpenMP_CXX)

add_executable(image image.cpp)
target_link_libraries(image kirkland_common fftw3f_threads fftw3f)

add_executable(incostem incostem.cpp incostemcmd.cpp probe.cpp)
target_link_libraries(incostem kirkland_common fftw3f_threads fftw3f OpenMP::OpenMP_CXX)

add_executable(mulslice mulslice.cpp)
target_link_libraries(mulslice kirkland_common fftw3f_threads fftw3f)

add_executable(probe probe.cpp probecmd.cpp)
target_link_libraries(probe kirkland_common fftw3f_threads fftw3f)

add_executable(stemslic stemslic.cpp)
target_link_libraries(stemslic kirkland_common fftw3f_threads fftw3f)

add_executable(sumpix sumpix.cpp)
target_link_libraries(sumpix kirkland_common fftw3f_threads fftw3f)

