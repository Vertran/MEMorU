# CMakeList.txt: проект CMake для game; включите исходный код и определения,
# укажите здесь логику для конкретного проекта.
#
cmake_minimum_required (VERSION 3.8)

# Включение горячей перезагрузки для компиляторов MSVC, если поддерживается.
if (POLICY CMP0141)
  cmake_policy(SET CMP0141 NEW)
  set(CMAKE_MSVC_DEBUG_INFORMATION_FORMAT "$<IF:$<AND:$<C_COMPILER_ID:MSVC>,$<CXX_COMPILER_ID:MSVC>>,$<$<CONFIG:Debug,RelWithDebInfo>:EditAndContinue>,$<$<CONFIG:Debug,RelWithDebInfo>:ProgramDatabase>>")
endif()

project ("game")

# Пути к библиотекам (измените на свои пути)
set(GLFW_DIR "${CMAKE_CURRENT_SOURCE_DIR}/libs/glfw")
set(GLAD_DIR "${CMAKE_CURRENT_SOURCE_DIR}/libs/glad")
set(GLM_DIR "${CMAKE_CURRENT_SOURCE_DIR}/libs/glm")

# Подключение заголовочных файлов
include_directories(${GLFW_DIR}/include)
include_directories(${GLAD_DIR}/include)
include_directories(${GLM_DIR})

# Добавьте источник в исполняемый файл этого проекта.
add_executable (game 
    "game.cpp" "game.h"
    "${GLAD_DIR}/src/glad.c"
    "modules/logger.cpp" "modules/logger.h"    "modules/UI/manager.cpp" "modules/UI/manager.h" "modules/onStartup.cpp")

# Подключение библиотек
target_link_libraries(game
    ${GLFW_DIR}/lib-vc2022/glfw3.lib  # Путь к GLFW библиотеке
    opengl32.lib  # Системная OpenGL библиотека
)

if (CMAKE_VERSION VERSION_GREATER 3.12)
  set_property(TARGET game PROPERTY CXX_STANDARD 20)
endif()

# TODO: Добавьте тесты и целевые объекты, если это необходимо.