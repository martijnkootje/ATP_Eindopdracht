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
include CMakeFiles/motor.dir/depend.make
# Include the progress variables for this target.
include CMakeFiles/motor.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/motor.dir/flags.make

CMakeFiles/motor.dir/CppCode/Motor/Motor.cpp.obj: CMakeFiles/motor.dir/flags.make
CMakeFiles/motor.dir/CppCode/Motor/Motor.cpp.obj: CMakeFiles/motor.dir/includes_CXX.rsp
CMakeFiles/motor.dir/CppCode/Motor/Motor.cpp.obj: ../CppCode/Motor/Motor.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/motor.dir/CppCode/Motor/Motor.cpp.obj"
	C:\MinGW\w64devkit\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\motor.dir\CppCode\Motor\Motor.cpp.obj -c C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht\CppCode\Motor\Motor.cpp

CMakeFiles/motor.dir/CppCode/Motor/Motor.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/motor.dir/CppCode/Motor/Motor.cpp.i"
	C:\MinGW\w64devkit\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht\CppCode\Motor\Motor.cpp > CMakeFiles\motor.dir\CppCode\Motor\Motor.cpp.i

CMakeFiles/motor.dir/CppCode/Motor/Motor.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/motor.dir/CppCode/Motor/Motor.cpp.s"
	C:\MinGW\w64devkit\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht\CppCode\Motor\Motor.cpp -o CMakeFiles\motor.dir\CppCode\Motor\Motor.cpp.s

# Object files for target motor
motor_OBJECTS = \
"CMakeFiles/motor.dir/CppCode/Motor/Motor.cpp.obj"

# External object files for target motor
motor_EXTERNAL_OBJECTS =

motor.cp310-win_amd64.pyd: CMakeFiles/motor.dir/CppCode/Motor/Motor.cpp.obj
motor.cp310-win_amd64.pyd: CMakeFiles/motor.dir/build.make
motor.cp310-win_amd64.pyd: C:/Python310/libs/python310.lib
motor.cp310-win_amd64.pyd: CMakeFiles/motor.dir/linklibs.rsp
motor.cp310-win_amd64.pyd: CMakeFiles/motor.dir/objects1.rsp
motor.cp310-win_amd64.pyd: CMakeFiles/motor.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared module motor.cp310-win_amd64.pyd"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\motor.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/motor.dir/build: motor.cp310-win_amd64.pyd
.PHONY : CMakeFiles/motor.dir/build

CMakeFiles/motor.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\motor.dir\cmake_clean.cmake
.PHONY : CMakeFiles/motor.dir/clean

CMakeFiles/motor.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht\cmake-build-debug C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht\cmake-build-debug C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht\cmake-build-debug\CMakeFiles\motor.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/motor.dir/depend

