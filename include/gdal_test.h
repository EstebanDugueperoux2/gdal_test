#pragma once

#ifdef _WIN32
  #define gdal_test_EXPORT __declspec(dllexport)
#else
  #define gdal_test_EXPORT
#endif

gdal_test_EXPORT void gdal_test();
