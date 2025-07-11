#pragma once
#include <fstream>
#include <iostream>
#include <string>
#include <chrono>
#include <iomanip>
#include <sstream>

enum class LogLevel {
    INFO,
    WARNING,
    ERROR,
    DEBUG
};

class Logger {
private:
    std::ofstream logFile;
    bool writeToConsole;
    bool writeToFile;

    std::string getCurrentTime();
    std::string levelToString(LogLevel level);

public:
    // Конструктор
    Logger(const std::string& filename = "app.log",
        bool console = true, bool file = true);

    // Деструктор
    ~Logger();

    // Основной метод логирования
    void log(LogLevel level, const std::string& message,
        const std::string& annotation = "");

    // Удобные методы для разных уровней
    void info(const std::string& message, const std::string& annotation = "");
    void warning(const std::string& message, const std::string& annotation = "");
    void error(const std::string& message, const std::string& annotation = "");
    void debug(const std::string& message, const std::string& annotation = "");

    // Методы для управления выводом
    void setConsoleOutput(bool enable);
    void setFileOutput(bool enable);

    // Проверка состояния
    bool isFileOpen() const;
};