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
    // �����������
    Logger(const std::string& filename = "app.log",
        bool console = true, bool file = true);

    // ����������
    ~Logger();

    // �������� ����� �����������
    void log(LogLevel level, const std::string& message,
        const std::string& annotation = "");

    // ������� ������ ��� ������ �������
    void info(const std::string& message, const std::string& annotation = "");
    void warning(const std::string& message, const std::string& annotation = "");
    void error(const std::string& message, const std::string& annotation = "");
    void debug(const std::string& message, const std::string& annotation = "");

    // ������ ��� ���������� �������
    void setConsoleOutput(bool enable);
    void setFileOutput(bool enable);

    // �������� ���������
    bool isFileOpen() const;
};