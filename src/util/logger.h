// Copyright (C) 2023 Ethan Uppal. All rights reserved.

#pragma once

#include <iostream>

/** A wrapper around output logging. */
class Logger {
    /** The output stream to log to. */
    std::ostream& out;

public:
    /** The global logger instance. */
    static Logger& main() {
        static Logger instance(std::cerr);
        return instance;
    }

    /** Constructs a new Logger that logs to `out`. */
    Logger(std::ostream& out): out(out) {}

    /** Logs `val`. */
    template<typename T>
    Logger& operator<<(T val) {
#ifndef RELEASE_BUILD
        out << val;
#endif
        return *this;
    }
};

// See Logger::main
#define Log Logger::main()
