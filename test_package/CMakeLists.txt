cmake_minimum_required(VERSION 3.15)
project(PackageTest CXX)

find_package(gdal_test CONFIG REQUIRED)

add_executable(example src/example.cpp)
target_link_libraries(example gdal_test::gdal_test)
