# simple cmake example
cmake_minimum_required(VERSION 3.14.3 FATAL_ERROR)
project(event)
add_compile_options(-Wall -Wextra)

list(APPEND CMAKE_PREFIX_PATH $ENV{ROOTSYS})
find_package(ROOT REQUIRED COMPONENTS RIO Net TreePlayer Physics)
include(${ROOT_USE_FILE})

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/header)				# add the header directories


# possibility 1 (wihtout root, more or less same as: g++ source/src.C main.C -o main.out)
#file(GLOB SOURCES "source/*.C" main.C)
#add_executable(hello_world ${SOURCES})

# possibility 2 (with root)
#add_library(src SHARED source/src.C)
#target_link_libraries(src PUBLIC ROOT::Physics ROOT::TreePlayer)
#add_executable(hello_world main.C)
#target_link_libraries(hello_world src)



# possibility 3 (with root + dic)

ROOT_GENERATE_DICTIONARY(G__AnalysisLib ../header/head.h LINKDEF LinkDef.h)
add_library(AnalysisLib SHARED source/src.C G__AnalysisLib.cxx)
add_library(src SHARED source/src.C)

add_dependencies(AnalysisLib G__AnalysisLib)

add_executable(hello_world main.C)
target_link_libraries(hello_world src ${ROOT_LIBRARIES})


