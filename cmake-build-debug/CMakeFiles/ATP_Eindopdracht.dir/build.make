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
include CMakeFiles/ATP_Eindopdracht.dir/depend.make
# Include the progress variables for this target.
include CMakeFiles/ATP_Eindopdracht.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/ATP_Eindopdracht.dir/flags.make

CMakeFiles/ATP_Eindopdracht.dir/pythonConnection.cpp.obj: CMakeFiles/ATP_Eindopdracht.dir/flags.make
CMakeFiles/ATP_Eindopdracht.dir/pythonConnection.cpp.obj: CMakeFiles/ATP_Eindopdracht.dir/includes_CXX.rsp
CMakeFiles/ATP_Eindopdracht.dir/pythonConnection.cpp.obj: ../pythonConnection.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/ATP_Eindopdracht.dir/pythonConnection.cpp.obj"
	C:\MinGW\w64devkit\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\ATP_Eindopdracht.dir\pythonConnection.cpp.obj -c C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht\pythonConnection.cpp

CMakeFiles/ATP_Eindopdracht.dir/pythonConnection.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/ATP_Eindopdracht.dir/pythonConnection.cpp.i"
	C:\MinGW\w64devkit\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht\pythonConnection.cpp > CMakeFiles\ATP_Eindopdracht.dir\pythonConnection.cpp.i

CMakeFiles/ATP_Eindopdracht.dir/pythonConnection.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/ATP_Eindopdracht.dir/pythonConnection.cpp.s"
	C:\MinGW\w64devkit\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht\pythonConnection.cpp -o CMakeFiles\ATP_Eindopdracht.dir\pythonConnection.cpp.s

# Object files for target ATP_Eindopdracht
ATP_Eindopdracht_OBJECTS = \
"CMakeFiles/ATP_Eindopdracht.dir/pythonConnection.cpp.obj"

# External object files for target ATP_Eindopdracht
ATP_Eindopdracht_EXTERNAL_OBJECTS =

ATP_Eindopdracht.exe: CMakeFiles/ATP_Eindopdracht.dir/pythonConnection.cpp.obj
ATP_Eindopdracht.exe: CMakeFiles/ATP_Eindopdracht.dir/build.make
ATP_Eindopdracht.exe: C:/Python310/libs/Python310.lib
ATP_Eindopdracht.exe: CMakeFiles/ATP_Eindopdracht.dir/linklibs.rsp
ATP_Eindopdracht.exe: CMakeFiles/ATP_Eindopdracht.dir/objects1.rsp
ATP_Eindopdracht.exe: CMakeFiles/ATP_Eindopdracht.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ATP_Eindopdracht.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\ATP_Eindopdracht.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/ATP_Eindopdracht.dir/build: ATP_Eindopdracht.exe
.PHONY : CMakeFiles/ATP_Eindopdracht.dir/build

CMakeFiles/ATP_Eindopdracht.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\ATP_Eindopdracht.dir\cmake_clean.cmake
.PHONY : CMakeFiles/ATP_Eindopdracht.dir/clean

CMakeFiles/ATP_Eindopdracht.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht\cmake-build-debug C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht\cmake-build-debug C:\Users\marti\Desktop\HBO-ict\ATP_Eindopdracht\cmake-build-debug\CMakeFiles\ATP_Eindopdracht.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/ATP_Eindopdracht.dir/depend

