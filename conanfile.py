from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout


class GdalTestConan(ConanFile):
    name = "gdal_test"
    version = "0.0.1"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of GdalTest here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "test": [True, False],
        "analyse_code_quality": [True, False],
    }
    
    default_options = {
        "shared": False,
        "fPIC": True,
        "test": False,
        "analyse_code_quality": False,
        }

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def requirements(self):
         self.requires("gdal/3.5.2")
    
    def build_requirements(self):
        self.tool_requires("cmake/3.25.2")
        self.tool_requires("ninja/1.11.1")
        self.tool_requires("ccache/4.6")
        if self.options.test:
            # FIXME once migrated to a more recent gcc than gcc8, we could use latest gtest release
            # See https://github.com/google/googletest/issues/3552#issuecomment-918520846
            self.test_requires("gtest/1.10.0")
        if self.options.analyse_code_quality:
            self.tool_requires("cppcheck/2.10")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["gdal_test"]
