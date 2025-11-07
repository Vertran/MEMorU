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


    logger.info("So... You've launched this game...");
    logger.info("Do you know what exactly you have launched? (y/n)");

    string userAnswer;
    cin >> userAnswer;
    logger.info("Your answer is..." + userAnswer);

    if (userAnswer == "y") {
		logger.info("No, you don't know.");
    }
    else {
        logger.info("So... Now I'll tell you...");
    }

    logger.warning("Launching supercollider.");
    logger.warning("Launching reactor.");
    logger.error("reactor may not function properly. DEACTIVATING IT.");
}

main();