cmake_minimum_required(VERSION 3.15)
project(gdal_test CXX)

add_library(gdal_test src/gdal_test.cpp)
target_include_directories(gdal_test PUBLIC include)

set_target_properties(gdal_test PROPERTIES PUBLIC_HEADER "include/gdal_test.h")
install(TARGETS gdal_test)
