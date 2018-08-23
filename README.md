# ccjparser

* compile_commands.json parser
* ccj: Compile_Commands.Json

* input:  compile_commands.json
* output: shell script

## NOTE
* default params are set for `clang-tidy`

## FYI

```
cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=ON ..
```

`compile_commands.json`

```
[
  {
    "directory": "/home/user/development/project",
    "command": "/usr/bin/c++ ... -c ../foo/foo.cc",
    "file": "../foo/foo.cc"
  },

  ...

  {
    "directory": "/home/user/development/project",
    "command": "/usr/bin/c++ ... -c ../foo/bar.cc",
    "file": "../foo/bar.cc"
  }
]
```

[CMAKE\_EXPORT\_COMPILE\_COMMANDS — CMake 3\.5\.2 Documentation]( https://cmake.org/cmake/help/v3.5/variable/CMAKE_EXPORT_COMPILE_COMMANDS.html )
