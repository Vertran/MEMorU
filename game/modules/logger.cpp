#include "logger.h"

// Конструктор
Logger::Logger(const std::string& filename, bool console, bool file)
    : writeToConsole(console), writeToFile(file) {

    if (writeToFile) {
        logFile.open(filename, std::ios::app);
        if (!logFile.is_open()) {
            std::cerr << "Не удалось открыть файл лога: " << filename << std::endl;
            writeToFile = false;
        }
    }
}

// Деструктор
Logger::~Logger() {
    if (logFile.is_open()) {
        logFile.close();
    }
}

// Получение текущего времени в формате "08.07.2025; 14:15:40"
std::string Logger::getCurrentTime() {
    auto now = std::chrono::system_clock::now();
    auto time_t = std::chrono::system_clock::to_time_t(now);

    std::stringstream ss;
    ss << std::put_time(std::localtime(&time_t), "%d.%m.%Y; %H:%M:%S");
    return ss.str();
}

// Преобразование уровня лога в строку
std::string Logger::levelToString(LogLevel level) {
    switch (level) {
    case LogLevel::INFO:    return "INFO";
    case LogLevel::WARNING: return "WARNING";
    case LogLevel::ERROR:   return "ERROR";
    case LogLevel::DEBUG:   return "DEBUG";
    default:               return "UNKNOWN";
    }
}

// Основной метод логирования
void Logger::log(LogLevel level, const std::string& message,
    const std::string& annotation) {

    std::stringstream logEntry;
    logEntry << "[" << levelToString(level) << "] "
        << "[" << getCurrentTime() << "] "
        << message;

    if (!annotation.empty()) {
        logEntry << "\n" << annotation;
    }

    std::string logString = logEntry.str();

    // Вывод в консоль
    if (writeToConsole) {
        std::cout << logString << std::endl;
    }

    // Запись в файл
    if (writeToFile && logFile.is_open()) {
        logFile << logString << std::endl;
        logFile.flush(); // Принудительно записать на диск
    }
}

//Logger leveling

void Logger::info(const std::string& message, const std::string& annotation) {
    log(LogLevel::INFO, message, annotation);
}

void Logger::warning(const std::string& message, const std::string& annotation) {
    log(LogLevel::WARNING, message, annotation);
}

void Logger::error(const std::string& message, const std::string& annotation) {
    log(LogLevel::ERROR, message, annotation);
}

void Logger::debug(const std::string& message, const std::string& annotation) {
    log(LogLevel::DEBUG, message, annotation);
}

// Методы для управления выводом
void Logger::setConsoleOutput(bool enable) {
    writeToConsole = enable;
}

void Logger::setFileOutput(bool enable) {
    writeToFile = enable;
}

// Проверка состояния файла
bool Logger::isFileOpen() const {
    return logFile.is_open();
}