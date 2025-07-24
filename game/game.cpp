#include <iostream>
#include <array>
#include "glad/glad.h"
#include "glfw/glfw3.h"
#include "modules/logger.h"

using namespace std;


void processInput(GLFWwindow* window) {
    if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS) {
        glfwSetWindowShouldClose(window, true);
    }
}


int main() {
    Logger logger("C:/Games/MEMorU/game/data/game.log");

    logger.info("Startup!");
}