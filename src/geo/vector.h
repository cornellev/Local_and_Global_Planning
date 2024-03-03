// Copyright (C) 2024 Ethan Uppal. All rights reserved.

#pragma once

#include <cmath>

/** An element of in 2-dimensional Euclidean space. */
struct Vector {
    Vector(double x, double y): x(x), y(y) {}

    double x;
    double y;

    Vector operator+(const Vector& other) const {
        return Vector(x + other.x, y + other.y);
    }

    Vector operator-(const Vector& other) const {
        return Vector(x - other.x, y - other.y);
    }

    Vector operator-() const {
        return Vector(-x, -y);
    }

    Vector operator*(double scalar) const {
        return Vector(x * scalar, y * scalar);
    }

    friend Vector operator*(double scalar, const Vector& v) {
        return Vector(scalar * v.x, scalar * v.y);
    }

    Vector operator/(double scalar) const {
        return Vector(x / scalar, y / scalar);
    }

    Vector& operator+=(const Vector& other) {
        x += other.x;
        y += other.y;
        return *this;
    }

    Vector& operator*=(double scalar) {
        x *= scalar;
        y *= scalar;
        return *this;
    }

    double dist(const Vector& other) {
        double dx = x - other.x;
        double dy = y - other.y;
        return std::sqrt(dx * dx + dy * dy);
    }

    double length() {
        return std::sqrt(x * x + y * y);
    }

    void normalize() {
        double length_computed = length();
        if (length_computed != 0) {
            x /= length_computed;
            y /= length_computed;
        }
    }
};
