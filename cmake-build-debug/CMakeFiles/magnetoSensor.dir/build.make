# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.20

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "C:\Program Files\JetBrains\CLion 2021.2.1\bin\cmake\win\bin\cmake.exe"

# The command to remove a file.
RM = "C:\Program Files\JetBrains\CLion 2021.2.1\bin\cmake\win\bin\cmake.exe" -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht\cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/magnetoSensor.dir/depend.make
# Include the progress variables for this target.
include CMakeFiles/magnetoSensor.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/magnetoSensor.dir/flags.make

CMakeFiles/magnetoSensor.dir/CppCode/MagnetoSensor/magnetoSensor.cpp.obj: CMakeFiles/magnetoSensor.dir/flags.make
CMakeFiles/magnetoSensor.dir/CppCode/MagnetoSensor/magnetoSensor.cpp.obj: CMakeFiles/magnetoSensor.dir/includes_CXX.rsp
CMakeFiles/magnetoSensor.dir/CppCode/MagnetoSensor/magnetoSensor.cpp.obj: ../CppCode/MagnetoSensor/magnetoSensor.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/magnetoSensor.dir/CppCode/MagnetoSensor/magnetoSensor.cpp.obj"
	C:\MinGW\w64devkit\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\magnetoSensor.dir\CppCode\MagnetoSensor\magnetoSensor.cpp.obj -c C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht\CppCode\MagnetoSensor\magnetoSensor.cpp

CMakeFiles/magnetoSensor.dir/CppCode/MagnetoSensor/magnetoSensor.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/magnetoSensor.dir/CppCode/MagnetoSensor/magnetoSensor.cpp.i"
	C:\MinGW\w64devkit\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht\CppCode\MagnetoSensor\magnetoSensor.cpp > CMakeFiles\magnetoSensor.dir\CppCode\MagnetoSensor\magnetoSensor.cpp.i

CMakeFiles/magnetoSensor.dir/CppCode/MagnetoSensor/magnetoSensor.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/magnetoSensor.dir/CppCode/MagnetoSensor/magnetoSensor.cpp.s"
	C:\MinGW\w64devkit\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht\CppCode\MagnetoSensor\magnetoSensor.cpp -o CMakeFiles\magnetoSensor.dir\CppCode\MagnetoSensor\magnetoSensor.cpp.s

# Object files for target magnetoSensor
magnetoSensor_OBJECTS = \
"CMakeFiles/magnetoSensor.dir/CppCode/MagnetoSensor/magnetoSensor.cpp.obj"

# External object files for target magnetoSensor
magnetoSensor_EXTERNAL_OBJECTS =

magnetoSensor.cp310-win_amd64.pyd: CMakeFiles/magnetoSensor.dir/CppCode/MagnetoSensor/magnetoSensor.cpp.obj
magnetoSensor.cp310-win_amd64.pyd: CMakeFiles/magnetoSensor.dir/build.make
magnetoSensor.cp310-win_amd64.pyd: C:/Python310/libs/python310.lib
magnetoSensor.cp310-win_amd64.pyd: CMakeFiles/magnetoSensor.dir/linklibs.rsp
magnetoSensor.cp310-win_amd64.pyd: CMakeFiles/magnetoSensor.dir/objects1.rsp
magnetoSensor.cp310-win_amd64.pyd: CMakeFiles/magnetoSensor.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared module magnetoSensor.cp310-win_amd64.pyd"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\magnetoSensor.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/magnetoSensor.dir/build: magnetoSensor.cp310-win_amd64.pyd
.PHONY : CMakeFiles/magnetoSensor.dir/build

CMakeFiles/magnetoSensor.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\magnetoSensor.dir\cmake_clean.cmake
.PHONY : CMakeFiles/magnetoSensor.dir/clean

CMakeFiles/magnetoSensor.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht\cmake-build-debug C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht\cmake-build-debug C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht\cmake-build-debug\CMakeFiles\magnetoSensor.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/magnetoSensor.dir/depend

