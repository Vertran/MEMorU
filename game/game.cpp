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

    // Initialize GLFW
    glfwInit();
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 2);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 1);

    // Create window
    GLFWwindow* window = glfwCreateWindow(800, 600, "Modern OpenGL Triangle", NULL, NULL);
    if (window == NULL) {
		logger.error("Failed to create GLFW window");
        glfwTerminate();
        return -1;
    }

    glfwMakeContextCurrent(window);

    // Load OpenGL functions
    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)) {
		logger.error("Failed to initialize GLAD");
        return -1;
    }


    std::string userInput;

    // Render loop
    while (!glfwWindowShouldClose(window)) {
        processInput(window);

        // Clear screen
        glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);


        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    glfwTerminate();
    return 0;
}