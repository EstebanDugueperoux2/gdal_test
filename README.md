# gdal_test

Using conan 1.x

```
docker run --rm -ti -v ${PWD}:/home/conan/project conanio/gcc8-ubuntu18.04
cd project
export PACKAGE_NAME=`conan inspect . --raw name`
export PACKAGE_VERSION=`conan inspect . --raw version`
export OPTIONS="--build missing --profile:build .conan/profiles/gcc8 --profile:host .conan/profiles/gcc8"
conan install .  $OPTIONS
conan build .
```